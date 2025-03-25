@echo off
echo ========================================
echo Blog Scraper - Lanceur automatique
echo ========================================

REM Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé.
    echo Veuillez l'installer depuis : https://www.python.org/downloads/
    pause
    exit /b
)

REM Lance le script Python d'installation
echo ✅ Python est installé. Lancement de l'installation...
python install_and_run.py

echo ----------------------------------------
echo Fin du programme.
pause
