#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias están correctamente instaladas
"""

import sys
import importlib
from pathlib import Path

def check_module(module_name, display_name=None):
    """Verifica si un módulo está instalado"""
    if display_name is None:
        display_name = module_name

    try:
        importlib.import_module(module_name)
        print(f"✅ {display_name} instalado correctamente")
        return True
    except ImportError:
        print(f"❌ {display_name} NO está instalado")
        return False

def check_file(file_path, display_name):
    """Verifica si un archivo existe"""
    if Path(file_path).exists():
        print(f"✅ {display_name} encontrado")
        return True
    else:
        print(f"❌ {display_name} NO encontrado")
        return False

def main():
    print("=" * 50)
    print("🔍 Verificando configuración de Photo Collage")
    print("=" * 50)
    print()

    all_good = True

    # Verificar Python version
    print(f"Python version: {sys.version}")
    if sys.version_info >= (3, 8):
        print("✅ Python version compatible")
    else:
        print("❌ Se requiere Python 3.8 o superior")
        all_good = False
    print()

    # Verificar módulos
    print("📦 Verificando módulos:")
    modules_to_check = [
        ("flet", "Flet"),
        ("PIL", "Pillow"),
        ("dotenv", "python-dotenv"),
        ("smtplib", "smtplib (built-in)"),
    ]

    for module, display in modules_to_check:
        if not check_module(module, display):
            all_good = False
    print()

    # Verificar archivos
    print("📁 Verificando archivos del proyecto:")
    files_to_check = [
        ("main.py", "main.py"),
        (".env", ".env"),
        ("config.py", "config.py"),
    ]

    for file_path, display in files_to_check:
        if not check_file(file_path, display):
            all_good = False
    print()

    # Verificar configuración .env
    print("⚙️ Verificando configuración .env:")
    if check_file(".env", ".env"):
        with open(".env", "r") as f:
            content = f.read()
            if "tu_contraseña_de_aplicación_aqui" in content:
                print("⚠️ ADVERTENCIA: Aún debes configurar SENDER_PASSWORD en .env")
            elif "SENDER_PASSWORD=" in content:
                print("✅ SENDER_PASSWORD configurado")
    print()

    # Resumen
    print("=" * 50)
    if all_good:
        print("✅ ¡Todo listo! Puedes ejecutar: python main.py")
    else:
        print("❌ Hay problemas. Revisa los errores arriba.")
        print()
        print("Para instalar las dependencias:")
        print("  pip install flet pillow python-dotenv")
    print("=" * 50)

if __name__ == "__main__":
    main()
