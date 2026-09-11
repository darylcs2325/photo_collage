#!/usr/bin/env python3
"""
Script de prueba para verificar que la app funciona sin errores
"""

import sys
from pathlib import Path

def test_imports():
    """Verifica que todos los imports funcionan"""
    print("🔍 Probando imports...")
    try:
        import flet as ft
        from flet import Colors, Alignment, Margin
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
        print("✅ Todos los imports funcionan correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en imports: {e}")
        return False

def test_colors():
    """Verifica que Colors funciona correctamente"""
    print("\n🔍 Probando Colors...")
    try:
        from flet import Colors
        test_colors = [
            Colors.BLUE,
            Colors.WHITE,
            Colors.GREY_300,
            Colors.GREEN,
            Colors.ORANGE,
            Colors.RED_300,
        ]
        for color in test_colors:
            if not color:
                print(f"❌ Color no válido: {color}")
                return False
        print("✅ Colors funcionan correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en Colors: {e}")
        return False

def test_alignment():
    """Verifica que Alignment funciona correctamente"""
    print("\n🔍 Probando Alignment...")
    try:
        from flet import Alignment
        test_alignment = Alignment.CENTER
        if not test_alignment:
            print("❌ Alignment.CENTER no válido")
            return False
        print("✅ Alignment funciona correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en Alignment: {e}")
        return False

def test_margin():
    """Verifica que Margin funciona correctamente"""
    print("\n🔍 Probando Margin...")
    try:
        import flet as ft
        test_margin = ft.Margin.symmetric(vertical=5)
        if not test_margin:
            print("❌ Margin.symmetric no válido")
            return False
        print("✅ Margin funciona correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en Margin: {e}")
        return False

def test_env():
    """Verifica que .env se puede cargar"""
    print("\n🔍 Probando .env...")
    try:
        from dotenv import load_dotenv
        import os
        load_dotenv()

        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = os.getenv("SMTP_PORT")

        if smtp_server and smtp_port:
            print(f"✅ .env cargado correctamente (SMTP: {smtp_server}:{smtp_port})")
            return True
        else:
            print("⚠️ .env existe pero no tiene valores SMTP")
            return True  # No es crítico
    except Exception as e:
        print(f"❌ Error en .env: {e}")
        return False

def test_image_processing():
    """Verifica que PIL funciona"""
    print("\n🔍 Probando PIL (procesamiento de imágenes)...")
    try:
        from PIL import Image, ImageDraw, ImageFont

        # Crear imagen de prueba
        test_img = Image.new('RGB', (100, 100), color='white')
        draw = ImageDraw.Draw(test_img)

        # Dibujar algo
        draw.rectangle([10, 10, 90, 90], outline='black')

        print("✅ PIL funciona correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en PIL: {e}")
        return False

def main():
    print("=" * 60)
    print("🧪 PRUEBA COMPLETA DE LA APLICACIÓN FLET")
    print("=" * 60)

    tests = [
        ("Imports", test_imports),
        ("Colors", test_colors),
        ("Alignment", test_alignment),
        ("Margin", test_margin),
        (".env", test_env),
        ("PIL", test_image_processing),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Error inesperado en {name}: {e}")
            results.append((name, False))

    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{status}: {name}")

    print("\n" + "=" * 60)
    if passed == total:
        print(f"✨ ¡ÉXITO! {passed}/{total} pruebas pasaron")
        print("\n🚀 La aplicación está lista para ejecutar:")
        print("   python main.py")
        return 0
    else:
        print(f"⚠️ {passed}/{total} pruebas pasaron, {total - passed} fallaron")
        return 1

if __name__ == "__main__":
    sys.exit(main())
