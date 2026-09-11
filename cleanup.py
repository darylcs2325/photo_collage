#!/usr/bin/env python3
"""
Script para limpiar archivos temporales generados por la aplicación
"""

import os
import glob
from pathlib import Path

def cleanup():
    """Elimina archivos temporales y collages generados"""

    print("🧹 Limpiando archivos temporales...")

    files_to_remove = [
        "preview_collage.png",
        "collage_*.png",
        "__pycache__",
        "*.pyc",
        ".DS_Store"
    ]

    removed_count = 0

    for pattern in files_to_remove:
        # Archivos específicos
        if "*" not in pattern:
            if os.path.exists(pattern):
                try:
                    os.remove(pattern)
                    print(f"  ✅ Eliminado: {pattern}")
                    removed_count += 1
                except Exception as e:
                    print(f"  ❌ Error al eliminar {pattern}: {e}")
        else:
            # Patrones glob
            for file in glob.glob(pattern):
                try:
                    if os.path.isfile(file):
                        os.remove(file)
                        print(f"  ✅ Eliminado: {file}")
                        removed_count += 1
                except Exception as e:
                    print(f"  ❌ Error al eliminar {file}: {e}")

    print()
    print(f"✨ Limpieza completada. {removed_count} archivo(s) eliminado(s)")

if __name__ == "__main__":
    cleanup()
