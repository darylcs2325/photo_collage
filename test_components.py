#!/usr/bin/env python3
"""
Prueba avanzada: Verificar que todos los componentes Flet se crean correctamente
"""

import sys

def test_flet_components():
    """Prueba creación de componentes Flet"""
    print("Testing Flet Components...\n")

    try:
        import flet as ft
        from flet import Colors, Alignment, ScrollMode, ThemeMode, icons, border, margin, padding

        print("1. Testing Colors...")
        test_colors = {
            "BLUE": Colors.BLUE,
            "WHITE": Colors.WHITE,
            "GREY_300": Colors.GREY_300,
            "GREEN": Colors.GREEN,
            "ORANGE": Colors.ORANGE,
            "RED_300": Colors.RED_300,
        }
        for name, color in test_colors.items():
            assert color is not None, f"{name} is None"
        print("   OK: All colors work\n")

        print("2. Testing basic controls...")
        text = ft.Text("Test", color=Colors.WHITE)
        assert text is not None

        divider = ft.Divider()
        assert divider is not None

        btn = ft.ElevatedButton("Test Button")
        assert btn is not None

        textfield = ft.TextField(label="Test")
        assert textfield is not None
        print("   OK: Basic controls work\n")

        print("3. Testing Container with border...")
        container = ft.Container(
            content=ft.Text("Test"),
            border=border.Border(
                left=border.BorderSide(1, Colors.GREY_300),
                right=border.BorderSide(1, Colors.GREY_300),
                top=border.BorderSide(1, Colors.GREY_300),
                bottom=border.BorderSide(1, Colors.GREY_300)
            ),
            border_radius=8,
            padding=10,
            alignment=Alignment.CENTER
        )
        assert container is not None
        print("   OK: Container with border works\n")

        print("4. Testing margin.Margin.symmetric...")
        m = margin.Margin.symmetric(vertical=5)
        assert m is not None
        print(f"   OK: margin.Margin.symmetric works: {m}\n")

        print("5. Testing Column with scroll...")
        col = ft.Column(scroll=ScrollMode.AUTO)
        assert col is not None
        print("   OK: Column with scroll works\n")

        print("6. Testing Row...")
        row = ft.Row([
            ft.Text("Item1"),
            ft.Text("Item2"),
        ])
        assert row is not None
        print("   OK: Row works\n")

        print("7. Testing IconButton...")
        btn = ft.IconButton(ft.Icon(icons.Icons.DELETE))
        assert btn is not None
        print("   OK: IconButton works\n")

        print("8. Testing FilePicker...")
        fp = ft.FilePicker()
        assert fp is not None
        print("   OK: FilePicker works\n")

        print("9. Testing AlertDialog...")
        dlg = ft.AlertDialog(
            title=ft.Text("Test"),
            content=ft.Text("Content"),
            actions=[ft.TextButton("OK")]
        )
        assert dlg is not None
        print("   OK: AlertDialog works\n")

        print("=" * 60)
        print("SUCCESS! All Flet components work correctly")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_flet_components()
    sys.exit(0 if success else 1)
