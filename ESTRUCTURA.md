# 📁 Estructura del Proyecto - Photo Collage Creator

```
app_chayo/
│
├── 📄 main.py                 # Aplicación principal (EJECUTA ESTO)
├── 📄 config.py               # Configuración personalizable
├── 📄 test_setup.py           # Script para verificar instalación
├── 🔧 .env                    # Credenciales (CONFIGURA ESTO)
│
├── 📋 QUICK_START.md          # Guía de inicio rápido (LEE ESTO PRIMERO)
├── 📋 README.md               # Documentación completa
├── 📋 ESTRUCTURA.md           # Este archivo
│
├── 🚀 run.bat                 # Ejecutor para Windows (CMD)
├── 🚀 run.ps1                 # Ejecutor para Windows (PowerShell)
│
├── 📱 buildozer.spec          # Configuración para compilar APK
│
└── 🐍 venv/                   # Ambiente virtual Python
    ├── Scripts/               # Ejecutables de Python
    ├── Lib/                   # Librerías instaladas
    └── ...
```

## 📄 Archivos Principales

### `main.py`
**Descripción**: La aplicación completa.

**Funciones principales**:
- Interfaz de usuario (UI) con Flet
- Gestión de imágenes
- Generación de collages
- Envío de correos

**Cómo usarlo**:
```bash
python main.py
```

### `config.py`
**Descripción**: Configuraciones personalizables de la app (sin modificar `main.py`).

**Qué puedes cambiar**:
- Dimensiones de la aplicación
- Tamaño de imágenes en collage
- Colores y fuentes
- Servidor SMTP

### `.env`
**Descripción**: Variables de entorno (contraseñas y credenciales).

**¡IMPORTANTE!** Debe ser configurado con:
- `SENDER_PASSWORD`: Tu contraseña de aplicación de Gmail

**Nunca compartir este archivo** con otros.

### `test_setup.py`
**Descripción**: Script de prueba para verificar que todo está instalado.

**Cuándo usarlo**:
- Si tienes dudas sobre si algo falta
- Antes de reportar un problema

**Cómo usarlo**:
```bash
python test_setup.py
```

## 🚀 Archivos de Ejecución

### `run.bat`
Ejecutor para **Windows (CMD)**.
- Haz doble clic
- Activa ambiente virtual automáticamente
- Instala dependencias si faltan

### `run.ps1`
Ejecutor para **Windows (PowerShell)**.
- Requiere PowerShell
- Más características que `.bat`

## 📚 Archivos de Documentación

### `QUICK_START.md`
**Mejor para**: Usuarios nuevos
- Setup de Gmail en 5 minutos
- Pasos para ejecutar
- Solución de problemas comunes

### `README.md`
**Mejor para**: Referencia completa
- Características detalladas
- Instalación paso a paso
- Compilación para Android
- Todas las opciones

### `ESTRUCTURA.md`
Este archivo. Explica la organización del proyecto.

## 🔧 Archivos de Configuración

### `buildozer.spec`
Especificación para compilar APK para Android.

**Cuándo usarlo**:
```bash
pip install buildozer cython
buildozer android debug
```

Genera: `bin/photocollage-0.1-debug.apk`

## 🐍 Ambiente Virtual (`venv`)

Carpeta con todas las librerías Python instaladas.

**Librerías incluidas**:
- `flet`: Framework UI
- `pillow`: Procesamiento de imágenes
- `python-dotenv`: Lectura de `.env`

**Nunca editar manualmente**. Creado automáticamente con:
```bash
python -m venv venv
```

## 🔄 Flujo de Uso Típico

```
1. Usuario ejecuta run.bat/run.ps1
       ↓
2. Se activa ambiente virtual automáticamente
       ↓
3. Se ejecuta main.py
       ↓
4. Interfaz Flet se abre en navegador
       ↓
5. Usuario agrega fotos + comentarios
       ↓
6. Genera preview del collage
       ↓
7. Completa correos
       ↓
8. Envía por correo
       ↓
9. Mensaje de éxito/error
```

## 📊 Flujo de Datos

```
[Usuario selecciona imágenes]
         ↓
[main.py lee archivos]
         ↓
[Almacena en ImageWithComment objects]
         ↓
[Usuario escribe comentarios]
         ↓
[Presiona Vista Previa]
         ↓
[Pillow genera collage.png]
         ↓
[Presiona Enviar Correo]
         ↓
[Credentials de .env]
         ↓
[SMTP conecta a Gmail]
         ↓
[Envía correo con adjunto]
```

## 🔐 Seguridad

### Archivos sensibles:
- `.env` → Contiene credenciales (NUNCA compartir)

### Archivos seguros para compartir:
- `main.py`
- `config.py`
- `*.md`
- `run.bat` / `run.ps1`

### Antes de compartir:
1. Elimina `.env`
2. Elimina `venv/`
3. Elimina archivos `.png` temporales
4. Distribuy solo: `main.py`, `config.py`, `run.bat/ps1`, `*.md`, `.env.example`

## 🎯 Próximos Pasos

1. **Leer**: `QUICK_START.md`
2. **Configurar**: `.env` con credenciales
3. **Ejecutar**: `run.bat` o `run.ps1`
4. **Usar**: Agregar fotos y comentarios
5. **Enviar**: Collage por correo

## 📞 Soporte

Si necesitas verificar instalación:
```bash
python test_setup.py
```

Si necesitas personalizar:
```bash
# Edita config.py
# Luego ejecuta: python main.py
```

---

✨ Proyecto completado y listo para usar
