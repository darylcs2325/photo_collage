@echo off
REM Script para ejecutar la aplicación Photo Collage

echo.
echo ========================================
echo.
echo     ^<^>^<^>  Photo Collage Creator  ^<^>^<^>
echo.
echo ========================================
echo.

REM Verificar si el ambiente virtual existe
if exist "venv\Scripts\activate.bat" (
    echo Activando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo Ambiente virtual no encontrado. Creando...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Instalando dependencias...
    pip install flet pillow python-dotenv
)

echo.
echo Iniciando aplicacion...
echo.

REM Ejecutar la aplicación
python main.py

echo.
echo Aplicacion cerrada
pause
