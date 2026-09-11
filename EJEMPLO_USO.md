# 📸 Ejemplo de Uso - Photo Collage Creator

## Caso de Uso: Crear collage de viaje y enviarlo

Imagina que tomaste 3 fotos durante un viaje a la playa y quieres crear un collage con comentarios para enviar a tus amigos.

## Paso 1: Preparar Imágenes

Tienes estas fotos:
```
📸 playa_1.jpg - Puesta de sol
📸 playa_2.jpg - Grupo de amigos
📸 playa_3.jpg - Atardecer
```

## Paso 2: Ejecutar la Aplicación

```bash
# Windows CMD
run.bat

# Windows PowerShell
.\run.ps1

# O directamente
.\venv\Scripts\Activate.ps1
python main.py
```

**Resultado**: Se abre una ventana con la interfaz de la app.

## Paso 3: Agregar Imágenes

### Primera Foto:
1. Haz clic en **"➕ Agregar Imagen"**
2. Selecciona `playa_1.jpg`
3. En el campo "Comentario", escribe:
   ```
   Hermosa puesta de sol en la playa 🌅
   ```
4. La foto aparece en la lista con thumbnail

### Segunda Foto:
1. Haz clic de nuevo en **"➕ Agregar Imagen"**
2. Selecciona `playa_2.jpg`
3. Comentario:
   ```
   Con mis amigos disfrutando el día
   ```

### Tercera Foto:
1. **"➕ Agregar Imagen"** → `playa_3.jpg`
2. Comentario:
   ```
   Colores increíbles en el cielo
   ```

**Estado actual**: 3 fotos en la lista con sus comentarios.

## Paso 4: Vista Previa del Collage

Haz clic en **"👁️ Vista Previa Collage"**

**Resultado**: Se abre un diálogo mostrando el collage tal como se verá:

```
┌─────────────────────────────────────────────────┐
│ [Foto 1]  [Foto 2]  [Foto 3]                   │
│                                                 │
│ Hermosa puesta de  Con mis amigos  Colores    │
│ sol en la playa    disfrutando el  increíbles │
│ 🌅                 día              en el cielo│
└─────────────────────────────────────────────────┘
```

Si no te gusta, puedes:
- **Cerrar** el diálogo
- **Editar** comentarios (sin cerrar)
- **Eliminar** fotos que no quieras
- **Agregar** más fotos

## Paso 5: Configurar Correos

Completa estos campos:

```
Tu correo (para envío): tu_email@gmail.com
Correo destinatario: amigo@gmail.com
```

## Paso 6: Enviar por Correo

Haz clic en **"📧 Enviar por Correo"**

### Proceso:
1. **"Generando collage..."** - Crea la imagen PNG
2. **"Enviando correo..."** - Conecta a Gmail
3. **✅ Correo enviado exitosamente** - ¡Listo!

### Lo que envía:
1. **Email**: Un archivo `.png` con el collage
2. **Asunto**: `Tu Collage de Fotos - 11/09/2026`
3. **Cuerpo**:
   ```
   Adjunto encontrarás tu collage de fotos con comentarios.

   • playa_1.jpg: Hermosa puesta de sol en la playa 🌅
   • playa_2.jpg: Con mis amigos disfrutando el día
   • playa_3.jpg: Colores increíbles en el cielo
   ```

## Paso 7: Verificación en Correo Destinatario

El amigo recibe:

```
De: tu_email@gmail.com
Para: amigo@gmail.com
Asunto: Tu Collage de Fotos - 11/09/2026

Adjunto encontrarás tu collage de fotos con comentarios.

• playa_1.jpg: Hermosa puesta de sol en la playa 🌅
• playa_2.jpg: Con mis amigos disfrutando el día
• playa_3.jpg: Colores increíbles en el cielo

[Adjunto: collage_20260911_145230.png]
```

El amigo hace clic en la imagen y ve el collage completo.

## Paso 8: Crear Otro Collage (Opcional)

Haz clic en **"🗑️ Limpiar Todo"** para:
- Eliminar todas las fotos
- Limpiar comentarios
- Limpiar campos de correo
- Empezar de nuevo

## Resultados Esperados

### ✅ Éxito:
- Mensaje verde: "✅ Correo enviado exitosamente"
- El archivo PNG se genera y envía
- El destinatario recibe el correo en su bandeja

### ❌ Error Común 1: "Error de autenticación"
**Causa**: Contraseña incorrecta en `.env`
**Solución**:
1. Ve a https://myaccount.google.com/apppasswords
2. Genera una nueva contraseña
3. Cópiala en `.env`: `SENDER_PASSWORD=nueva_contraseña`
4. Intenta enviar de nuevo

### ❌ Error Común 2: "Las imágenes no se ven"
**Causa**: Las imágenes están corrutas o en formato no soportado
**Solución**:
- Usa JPG o PNG
- Verifica que las imágenes no estén dañadas
- Intenta con otra imagen

### ❌ Error Común 3: "Configure SENDER_PASSWORD en .env"
**Causa**: El archivo `.env` está vacío
**Solución**: Sigue el paso de configuración en QUICK_START.md

## Personalización Avanzada

### Cambiar tamaño de fotos:
Edita `config.py`:
```python
MAX_IMAGE_HEIGHT = 400  # En lugar de 300
```

### Cambiar fondo del collage:
Edita `config.py`:
```python
COLLAGE_BACKGROUND_COLOR = "lightgray"  # En lugar de "white"
```

### Cambiar tamaño de fuente de comentarios:
Edita `config.py`:
```python
COMMENT_FONT_SIZE = 16  # En lugar de 14
```

## Variaciones de Uso

### 📱 Para Fotos de Eventos:
- Bodas: Fotos de la ceremonia, recepción, detalles
- Cumpleaños: Fotos del festejo, pastel, amigos
- Graduación: Fotos de la ceremonia, grupo, diplomas

### 🎨 Para Proyectos Creativos:
- Portfolio: Tus mejores trabajos
- Antes/Después: Comparar estados
- Galería: Colección temática

### 📧 Para Comunicación:
- Actualizaciones de equipo
- Reportes visuales
- Recuerdos compartidos
- Resúmenes de viajes

## Flujo Completo (Resumen)

```
Ejecutar app
    ↓
Agregar foto 1 + comentario
    ↓
Agregar foto 2 + comentario
    ↓
Agregar foto 3 + comentario
    ↓
Vista previa (opcional)
    ↓
Configurar correos
    ↓
Enviar
    ↓
✅ Éxito
```

## Archivos Generados

Después de usar la app, se crean estos archivos:

```
app_chayo/
├── collage_20260911_145230.png    # Tu collage (se elimina después)
└── preview_collage.png             # Preview temporal (se elimina después)
```

Para limpiar manualmente:
```bash
python cleanup.py
```

---

¡Listo! Ahora puedes crear tus propios collages. 🎉
