# 📸 Photo Collage & Email Creator

Una aplicación Flet para crear collages de fotos con comentarios y enviarlos por correo. Diseñada para dispositivos móviles.

## 🚀 Características

- ✅ Agregar múltiples imágenes
- ✅ Añadir comentarios personalizados a cada foto
- ✅ Vista previa del collage antes de enviar
- ✅ Generar collage automático con las imágenes en fila
- ✅ Enviar collage por correo electrónico
- ✅ Interfaz mobile-friendly
- ✅ Soporte para múltiples formatos de imagen (JPG, PNG, GIF, BMP)

## 📋 Requisitos Previos

- Python 3.8+
- pip

## 🔧 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd D:\Scripts\Proyectos\app_chayo
```

### 2. Crear ambiente virtual (ya está hecho)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias (ya están instaladas)

```bash
pip install flet pillow python-dotenv
```

## 🔐 Configuración de Correo (IMPORTANTE)

### Para Gmail:

1. Ve a tu cuenta de Google: https://myaccount.google.com
2. En la sección "Seguridad", habilita **Verificación en dos pasos**
3. Ve a https://myaccount.google.com/apppasswords
4. Selecciona "Correo" y "Windows"
5. Google te generará una **contraseña de aplicación** (16 caracteres)
6. Abre el archivo `.env` y reemplaza:
   ```
   SENDER_PASSWORD=tu_contraseña_de_aplicación_aqui
   ```
   con la contraseña que Google te generó

### Para otros proveedores de correo:

Actualiza en `.env`:
```
SMTP_SERVER=tu_servidor_smtp
SMTP_PORT=587
SENDER_PASSWORD=tu_contraseña
```

## 🎮 Cómo Usar

### Ejecutar la aplicación:

```bash
# Asegúrate de estar en el ambiente virtual
.\venv\Scripts\Activate.ps1

# Ejecutar
python main.py
```

### En la aplicación:

1. **Agregar Imágenes**: Haz clic en "➕ Agregar Imagen"
2. **Añadir Comentarios**: Escribe un comentario debajo de cada imagen
3. **Vista Previa**: Haz clic en "👁️ Vista Previa Collage" para ver cómo se verá
4. **Completar Datos**:
   - "Tu correo (para envío)": Tu dirección de Gmail
   - "Correo destinatario": A quién enviar el collage
5. **Enviar**: Haz clic en "📧 Enviar por Correo"
6. **Limpiar**: Usa "🗑️ Limpiar Todo" para empezar de nuevo

## 📱 Para Compilar como APK (Android)

Si deseas crear un APK para instalar en celulares Android:

```bash
# Instalar buildozer
pip install buildozer cython

# Navegar al directorio del proyecto
cd D:\Scripts\Proyectos\app_chayo

# Crear especificaciones de compilación
buildozer android debug

# La compilación tardará varios minutos
# El APK estará en: bin/app_chayo-0.1-debug.apk
```

## 🎨 Características del Collage

- Las imágenes se colocan en una fila horizontal
- Se redimensionan a máximo 300px de alto
- Se añaden espacios de 10px entre cada imagen
- Los comentarios aparecen debajo de cada imagen
- El fondo del collage es blanco

## 🐛 Solución de Problemas

### "Error de autenticación en correo"
- Verifica que la contraseña de aplicación en `.env` sea correcta
- Asegúrate de habilitar la verificación de dos pasos en Google
- No uses la contraseña normal de Gmail

### "No se pueden cargar las imágenes"
- Verifica que las imágenes sean JPG, PNG, GIF o BMP
- Asegúrate de que el archivo no esté dañado
- Intenta con una imagen diferente

### "El collage se ve muy pequeño"
- Asegúrate de que tus imágenes tengan resolución decente
- Las imágenes se redimensionan a máximo 300px de alto

## 📧 Estructura del Correo Enviado

El correo incluirá:
- Un mensaje personalizado con los comentarios de cada foto
- El collage como archivo adjunto (.png)
- La fecha de creación en el asunto

## 🔄 Próximas Mejoras Posibles

- [ ] Soporte para orientación vertical/horizontal
- [ ] Editar el orden de las imágenes
- [ ] Agregar fondos personalizados al collage
- [ ] Cambiar tamaño y color de fuente
- [ ] Guardar collage en galería sin enviar
- [ ] Soporte para múltiples layouts (grid, circular, etc.)

## 📄 Licencia

Uso libre para fines personales y educativos.

## 👨‍💻 Autor

Creado con ❤️ usando Flet y Python
