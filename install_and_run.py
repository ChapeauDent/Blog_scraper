import subprocess
import sys
import os

# Liste des bibliothèques requises
required_packages = [
    "requests",
    "beautifulsoup4",
    "tk"
]

def install_packages(packages):
    for package in packages:
        print(f"Installation de {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    install_packages(required_packages)
    print("\n✅ Toutes les bibliothèques sont installées.")

    # Exécute le script scraper si présent
    script_file = "blog_scraper.py"
    if os.path.exists(script_file):
        print(f"\n▶️ Exécution de {script_file}...\n")
        subprocess.run([sys.executable, script_file])
    else:
        print(f"❌ Le fichier {script_file} est introuvable dans ce dossier.")

except Exception as e:
    print(f"\n❌ Une erreur est survenue : {e}")
