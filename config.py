# Configuración de la Aplicación Photo Collage

# ==================== UI CONFIG ====================
APP_TITLE = "📸 Photo Collage Creator"
APP_WIDTH = 400
APP_HEIGHT = 800

# ==================== IMAGE CONFIG ====================
MAX_IMAGE_HEIGHT = 300  # Altura máxima de las imágenes en el collage (px)
IMAGE_GAP = 10  # Espacio entre imágenes (px)
MAX_PREVIEW_THUMB = 100  # Tamaño máximo del thumbnail en lista

# ==================== COLLAGE CONFIG ====================
COLLAGE_BACKGROUND_COLOR = "white"  # Color de fondo del collage
COMMENT_FONT_SIZE = 14  # Tamaño de fuente para comentarios principales
COMMENT_SMALL_FONT_SIZE = 10  # Tamaño de fuente para comentarios pequeños
COMMENT_COLOR = "black"  # Color del texto de comentarios
COMMENT_MAX_LINES = 3  # Máximo de líneas de comentario por imagen

# ==================== EMAIL CONFIG ====================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
COLLAGE_FILENAME_PREFIX = "collage"

# ==================== ALLOWED FORMATS ====================
ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp"]

# ==================== MESSAGES ====================
MESSAGES = {
    "add_image": "➕ Agregar Imagen",
    "preview": "👁️ Vista Previa Collage",
    "send_email": "📧 Enviar por Correo",
    "clear": "🗑️ Limpiar Todo",
    "loading_image": "Cargando imagen...",
    "generating_collage": "Generando collage...",
    "sending_email": "Enviando correo...",
    "success": "✅ Correo enviado exitosamente",
    "error_no_images": "No hay imágenes para previsualizar",
    "error_email_fields": "Completa los campos de correo",
    "error_no_config": "Configure SENDER_PASSWORD en .env",
}
