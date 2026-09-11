import flet as ft
from flet import Colors, Alignment, ScrollMode, ThemeMode, icons, border, margin, padding
from PIL import Image, ImageDraw, ImageFont
import io
import os
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from dotenv import load_dotenv
from tkinter import filedialog
from tkinter import Tk

load_dotenv()

class ImageWithComment:
    def __init__(self, path, comment=""):
        self.path = path
        self.comment = comment
        self.image_name = Path(path).name

class PhotoCollageApp:
    def __init__(self):
        self.images_data = []
        self.MAX_PREVIEW_WIDTH = 100

    def build_ui(self, page: ft.Page):
        page.title = "Photo Collage & Email"
        page.theme_mode = ThemeMode.LIGHT
        page.window.width = 400
        page.window.height = 800

        # Header
        header = ft.Container(
            content=ft.Text("📸 Photo Collage Creator",
                          size=24,
                          weight="bold",
                          color=Colors.WHITE),
            bgcolor=Colors.BLUE,
            padding=20,
            alignment=Alignment.CENTER
        )

        # Add image button
        add_image_btn = ft.Button(
            "➕ Agregar Imagen",
            width=350,
            height=50,
            on_click=self.pick_image
        )

        # Email input
        email_input = ft.TextField(
            label="Tu correo (para envío)",
            width=350,
            value=""
        )

        # Recipient email input
        recipient_email = ft.TextField(
            label="Correo destinatario",
            width=350,
            value=""
        )

        # Images list container
        self.images_scroll = ft.Column(scroll=ScrollMode.AUTO)

        images_list_container = ft.Container(
            content=ft.Column([
                ft.Text("Tus imágenes:", size=16, weight="bold"),
                self.images_scroll
            ]),
            border=border.Border(
                left=border.BorderSide(1, Colors.GREY_300),
                right=border.BorderSide(1, Colors.GREY_300),
                top=border.BorderSide(1, Colors.GREY_300),
                bottom=border.BorderSide(1, Colors.GREY_300)
            ),
            border_radius=8,
            padding=10,
            height=300
        )

        # Preview button
        preview_btn = ft.Button(
            "👁️ Vista Previa Collage",
            width=350,
            height=45,
            bgcolor=Colors.GREEN,
            color=Colors.WHITE,
            on_click=lambda e: self.show_preview(page)
        )

        # Send email button
        send_btn = ft.Button(
            "📧 Enviar por Correo",
            width=350,
            height=45,
            bgcolor=Colors.ORANGE,
            color=Colors.WHITE,
            on_click=lambda e: self.send_email(page, email_input.value, recipient_email.value)
        )

        # Clear button
        clear_btn = ft.Button(
            "🗑️ Limpiar Todo",
            width=350,
            height=45,
            bgcolor=Colors.RED_300,
            on_click=self.clear_all
        )

        # Status message
        self.status_text = ft.Text("", color=Colors.GREEN, size=12)

        # Main content
        main_content = ft.Container(
            content=ft.Column([
                header,
                ft.Divider(),
                add_image_btn,
                ft.Container(height=10),
                images_list_container,
                ft.Container(height=10),
                email_input,
                recipient_email,
                preview_btn,
                send_btn,
                clear_btn,
                self.status_text
            ],
            spacing=10,
            scroll=ScrollMode.AUTO
            ),
            padding=10
        )

        # Store references for later use
        self.page = page
        self.email_input = email_input
        self.recipient_email = recipient_email

        page.add(main_content)

    def pick_image(self, e):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[
                ("Imágenes", "*.jpg *.jpeg *.png *.gif *.bmp"),
                ("JPG", "*.jpg *.jpeg"),
                ("PNG", "*.png"),
                ("GIF", "*.gif"),
                ("BMP", "*.bmp"),
                ("Todos", "*.*")
            ]
        )
        root.destroy()

        if file_path:
            self.add_image_item(file_path)
            self.page.update()

    def add_image_item(self, image_path):
        img_data = ImageWithComment(image_path)
        self.images_data.append(img_data)

        # Comment input
        comment_field = ft.TextField(
            label="Comentario",
            multiline=True,
            min_lines=2,
            max_lines=3,
            width=300,
            on_change=lambda e: self.update_comment(len(self.images_data) - 1, e.control.value)
        )

        # Remove button
        remove_btn = ft.IconButton(
            ft.Icon(icons.Icons.DELETE),
            icon_size=20,
            tooltip="Eliminar",
            on_click=lambda e: self.remove_image(len(self.images_data) - 1)
        )

        # Image preview thumbnail
        try:
            img = Image.open(image_path)
            img.thumbnail((self.MAX_PREVIEW_WIDTH, self.MAX_PREVIEW_WIDTH))
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="PNG")
            img_base64 = __import__('base64').b64encode(img_bytes.getvalue()).decode()
            img_widget = ft.Image(src_base64=img_base64, width=100, height=100)
        except Exception as ex:
            img_widget = ft.Text(f"Error: {str(ex)}", color=Colors.RED)

        item = ft.Container(
            content=ft.Row([
                img_widget,
                ft.Column([
                    ft.Text(Path(image_path).name, size=10, weight="bold"),
                    comment_field
                ], expand=True),
                remove_btn
            ]),
            border=border.Border(
                left=border.BorderSide(1, Colors.GREY_300),
                right=border.BorderSide(1, Colors.GREY_300),
                top=border.BorderSide(1, Colors.GREY_300),
                bottom=border.BorderSide(1, Colors.GREY_300)
            ),
            border_radius=8,
            padding=8,
            margin=margin.Margin.symmetric(vertical=5)
        )

        self.images_scroll.controls.append(item)
        self.page.update()

    def update_comment(self, index, comment):
        if 0 <= index < len(self.images_data):
            self.images_data[index].comment = comment

    def remove_image(self, index):
        if 0 <= index < len(self.images_data):
            self.images_data.pop(index)
            self.images_scroll.controls.pop(index)
            self.page.update()

    def create_collage(self):
        if not self.images_data:
            return None

        # Load images
        images = []
        comments = []
        max_height = 0

        for img_data in self.images_data:
            try:
                img = Image.open(img_data.path)
                # Resize to max height of 300px
                if img.height > 300:
                    ratio = 300 / img.height
                    new_width = int(img.width * ratio)
                    img = img.resize((new_width, 300), Image.Resampling.LANCZOS)
                images.append(img)
                max_height = max(max_height, img.height)
                comments.append(img_data.comment)
            except Exception as ex:
                print(f"Error loading image: {ex}")
                continue

        if not images:
            return None

        # Calculate total width and create canvas
        total_width = sum(img.width for img in images) + (len(images) - 1) * 10  # 10px gap
        canvas_height = max_height + 150  # Space for comments

        collage = Image.new('RGB', (total_width, canvas_height), color='white')
        draw = ImageDraw.Draw(collage)

        try:
            font = ImageFont.truetype("arial.ttf", 14)
            font_small = ImageFont.truetype("arial.ttf", 10)
        except:
            font = ImageFont.load_default()
            font_small = font

        # Paste images
        x_offset = 0
        for i, img in enumerate(images):
            collage.paste(img, (x_offset, 0))
            x_offset += img.width + 10

        # Add comments below
        y_offset = max_height + 10
        x_offset = 0
        for i, (img, comment) in enumerate(zip(images, comments)):
            if comment:
                # Draw text with word wrap
                words = comment.split()
                lines = []
                current_line = ""
                for word in words:
                    test_line = f"{current_line} {word}".strip()
                    bbox = draw.textbbox((0, 0), test_line, font=font_small)
                    if bbox[2] - bbox[0] > img.width - 4:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                    else:
                        current_line = test_line
                if current_line:
                    lines.append(current_line)

                # Draw lines
                y = y_offset
                for line in lines[:3]:  # Max 3 lines per comment
                    draw.text((x_offset + 2, y), line, fill='black', font=font_small)
                    y += 12

            x_offset += img.width + 10

        return collage

    def show_preview(self, e):
        collage = self.create_collage()
        if not collage:
            self.update_status("No hay imágenes para previsualizar", "error")
            return

        # Save preview temporarily
        preview_path = "preview_collage.png"
        collage.save(preview_path)

        # Show in a dialog
        dlg = ft.AlertDialog(
            title=ft.Text("Vista Previa del Collage"),
            content=ft.Image(src=preview_path, width=350, height=600),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: self.close_dialog(dlg))
            ]
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def close_dialog(self, dlg):
        dlg.open = False
        self.page.update()

    def send_email(self, page, sender_email, recipient_email):
        if not self.images_data:
            self.update_status("Agrega imágenes primero", "error")
            return

        if not sender_email or not recipient_email:
            self.update_status("Completa los campos de correo", "error")
            return

        try:
            self.update_status("Generando collage...", "info")
            collage = self.create_collage()

            if not collage:
                self.update_status("Error al crear collage", "error")
                return

            # Save collage
            collage_path = f"collage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            collage.save(collage_path)

            # Get SMTP credentials from environment
            smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("SMTP_PORT", "587"))
            sender_password = os.getenv("SENDER_PASSWORD")

            if not sender_password:
                self.update_status("Configure SENDER_PASSWORD en .env", "error")
                return

            self.update_status("Enviando correo...", "info")

            # Create email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = f"Tu Collage de Fotos - {datetime.now().strftime('%d/%m/%Y')}"

            # Email body
            body = "Adjunto encontrarás tu collage de fotos con comentarios.\n\n"
            for img_data in self.images_data:
                if img_data.comment:
                    body += f"• {img_data.image_name}: {img_data.comment}\n"

            message.attach(MIMEText(body, "plain"))

            # Attach collage
            with open(collage_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {collage_path}")
                message.attach(part)

            # Send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)

            self.update_status("Correo enviado exitosamente", "success")

        except Exception as ex:
            self.update_status(f"Error: {str(ex)}", "error")

    def update_status(self, message, status_type="info"):
        color_map = {
            "success": Colors.GREEN,
            "error": Colors.RED,
            "info": Colors.BLUE
        }
        self.status_text.value = message
        self.status_text.color = color_map.get(status_type, Colors.GREY)
        self.page.update()

    def clear_all(self, e):
        self.images_data.clear()
        self.images_scroll.controls.clear()
        self.email_input.value = ""
        self.recipient_email.value = ""
        self.status_text.value = ""
        self.page.update()

def main(page: ft.Page):
    app = PhotoCollageApp()
    app.build_ui(page)

if __name__ == "__main__":
    ft.app(target=main)
