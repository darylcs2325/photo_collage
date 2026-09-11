#!/usr/bin/env python3
"""
Prueba final: Verificar que la app se puede inicializar completamente
"""

import sys
import os

def test_full_app():
    """Intenta crear la aplicación completa"""
    print("🧪 Prueba final: Inicializando aplicación...")
    print()

    try:
        # Importar módulo principal
        print("1️⃣ Importando main.py...")
        from main import PhotoCollageApp, main
        print("   ✅ main.py importado correctamente")

        # Crear instancia de la app
        print("\n2️⃣ Creando instancia de PhotoCollageApp...")
        app = PhotoCollageApp()
        print("   ✅ PhotoCollageApp instanciado correctamente")

        # Verificar métodos principales
        print("\n3️⃣ Verificando métodos principales...")
        required_methods = [
            'build_ui',
            'pick_image',
            'add_image_item',
            'create_collage',
            'send_email',
            'show_preview',
        ]

        for method in required_methods:
            if hasattr(app, method):
                print(f"   ✅ {method} existe")
            else:
                print(f"   ❌ {method} NO existe")
                return False

        # Verificar que los datos se pueden manipular
        print("\n4️⃣ Verificando estructura de datos...")
        if hasattr(app, 'images_data'):
            print("   ✅ images_data existe")
            if len(app.images_data) == 0:
                print("   ✅ images_data está vacío (correcto para inicio)")
            else:
                print("   ⚠️ images_data no está vacío")
        else:
            print("   ❌ images_data NO existe")
            return False

        print("\n" + "=" * 60)
        print("✨ ¡ÉXITO! La aplicación está completamente lista")
        print("=" * 60)
        print("\n🚀 Ahora puedes ejecutar:")
        print("   python main.py")
        print("\n O hacer doble clic en:")
        print("   run.bat")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_full_app()
    sys.exit(0 if success else 1)
