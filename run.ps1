# Script para ejecutar la aplicación Photo Collage

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "📸 Photo Collage Creator" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si el ambiente virtual existe
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "✅ Activando ambiente virtual..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "❌ Ambiente virtual no encontrado. Creando..." -ForegroundColor Red
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    Write-Host "📦 Instalando dependencias..." -ForegroundColor Yellow
    pip install flet pillow python-dotenv
}

Write-Host ""
Write-Host "🚀 Iniciando aplicación..." -ForegroundColor Green
Write-Host ""

# Ejecutar la aplicación
python main.py

Write-Host ""
Write-Host "👋 Aplicación cerrada" -ForegroundColor Yellow
