# ⚡ Inicio Rápido - Photo Collage Creator

## 1️⃣ Primero: Configurar Gmail (5 minutos)

### Paso A: Habilitar verificación en dos pasos
1. Ve a: https://myaccount.google.com
2. Selecciona "Seguridad" (lado izquierdo)
3. Busca "Verificación en dos pasos" y actívalo
4. Sigue el proceso de verificación

### Paso B: Generar contraseña de aplicación
1. Luego de habilitar 2FA, ve a: https://myaccount.google.com/apppasswords
2. Selecciona:
   - App: "Correo"
   - Dispositivo: "Windows"
3. Google te mostrará una contraseña de 16 caracteres
4. **Cópiala** (ejemplo: `abcd efgh ijkl mnop`)

### Paso C: Configurar la app
1. Abre el archivo `.env` (en la carpeta del proyecto)
2. Reemplaza:
   ```
   SENDER_PASSWORD=tu_contraseña_de_aplicación_aqui
   ```
   con tu contraseña (sin espacios):
   ```
   SENDER_PASSWORD=abcdefghijklmnop
   ```
3. Guarda el archivo

## 2️⃣ Ejecutar la App

### Opción A: Ejecutar archivo (recomendado)
- **Windows**: Haz doble clic en `run.bat`
- **PowerShell**: Ejecuta `.\run.ps1`

### Opción B: Línea de comando
```bash
.\venv\Scripts\Activate.ps1
python main.py
```

## 3️⃣ Usar la App

### Flujo de uso:
1. **Agregar Imágenes** → Haz clic en "➕ Agregar Imagen"
2. **Escribir Comentarios** → Escribe debajo de cada imagen
3. **Vista Previa** → Haz clic en "👁️ Vista Previa Collage"
4. **Completar Correos**:
   - "Tu correo": Tu Gmail
   - "Correo destinatario": A quién enviar
5. **Enviar** → Haz clic en "📧 Enviar por Correo"

## 4️⃣ Compilar para Android (Opcional)

Si quieres crear un APK para instalar en tu celular:

```bash
pip install buildozer cython
buildozer android debug
```

El APK estará en: `bin/photocollage-0.1-debug.apk`

## ⚠️ Solución de Problemas

### "Error de autenticación"
→ Verifica que copiaste bien la contraseña en `.env`
→ La contraseña tiene 16 caracteres sin espacios

### "Permiso denegado"
→ La contraseña podría estar mal
→ Intenta generar una nueva en https://myaccount.google.com/apppasswords

### "No encuentra las imágenes"
→ Asegúrate de que las imágenes sean JPG, PNG, GIF o BMP
→ Verifica que las imágenes no estén dañadas

## 📧 Ejemplo de lo que recibirá el destinatario

**Asunto**: Tu Collage de Fotos - 11/09/2026

**Cuerpo del correo**:
```
Adjunto encontrarás tu collage de fotos con comentarios.

• foto1.jpg: Este es mi comentario sobre la primera foto
• foto2.png: Otro comentario sobre la segunda imagen
```

**Adjunto**: `collage_20260911_145230.png` (imagen del collage)

## 🎨 Personalizar Collage

Para cambiar colores, tamaños, etc., edita `config.py`:

```python
MAX_IMAGE_HEIGHT = 300  # Altura de imágenes (cambiar si quieres más grandes)
IMAGE_GAP = 10  # Espacio entre fotos
COLLAGE_BACKGROUND_COLOR = "white"  # Cambiar a "black", "gray", etc.
COMMENT_FONT_SIZE = 14  # Tamaño de texto de comentarios
```

## ✅ Checklist de Configuración

- [ ] Python 3.8+ instalado
- [ ] Ambiente virtual creado (`venv` carpeta existe)
- [ ] Dependencias instaladas (Flet, Pillow)
- [ ] Gmail con 2FA habilitado
- [ ] Contraseña de aplicación generada
- [ ] `.env` configurado con contraseña
- [ ] `run.bat` o `run.ps1` listo

## 🆘 Necesitas Ayuda?

Si algo no funciona:
1. Ejecuta `python test_setup.py` para verificar la configuración
2. Revisa el archivo `.env` tenga SENDER_PASSWORD correcto
3. Intenta generar nueva contraseña en myaccount.google.com

---

¡Listo! Ahora puedes crear tu primer collage. 📸✨
