@echo off
echo ========================================
echo 🧠 Génération IA avec Ollama (Mistral)
echo ========================================

REM Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé.
    echo Veuillez l'installer depuis : https://www.python.org/downloads/
    pause
    exit /b
)

REM Vérifie si Ollama est en cours d'exécution
curl http://localhost:11434 >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Ollama ne semble pas être lancé.
    echo Lancez Ollama avec : ollama run mistral (ou un autre modèle)
    pause
    exit /b
)

REM Lancer le script Python
echo ✅ Python et Ollama détectés.
echo ▶️ Lancement de run_prompts_with_ollama.py...
python run_prompts_with_ollama.py

echo ----------------------------------------
echo ✅ Génération terminée. Appuyez sur une touche pour quitter.
pause
