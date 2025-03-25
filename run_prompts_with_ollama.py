import csv
import requests

MODEL = "mistral"  # ou llama2, llama3, etc.
OLLAMA_URL = "http://localhost:11434/api/generate"

# --- Détection automatique du type d'article ---
def detecter_type_article(titre):
    titre = titre.lower()
    if any(mot in titre for mot in ["étapes", "comment", "tutoriel", "guide"]):
        return "tutoriel"
    if any(mot in titre for mot in ["vs", "comparatif", "lequel", "différences", "meilleur"]):
        return "comparatif"
    if any(mot in titre for mot in ["raisons", "outils", "conseils", "avantages", "chiffres", "liste"]):
        return "liste"
    if any(mot in titre for mot in ["selon nous", "notre avis", "nous pensons", "prise de position"]):
        return "opinion"
    if any(mot in titre for mot in ["conférence", "salon", "événement", "webinar", "séminaire"]):
        return "événement"
    return "liste"  # fallback

# --- Modèles HubSpot associés ---
MODELE_PAR_TYPE = {
    "liste": "Modèle pour rédiger un article de type liste  - HubSpot.md",
    "comparatif": "Modèle pour rédiger un article comparatif - HubSpot.md",
    "tutoriel": "Modèle pour créer un article tutoriel - HubSpot.md",
    "opinion": "Modèle pour créer un article de prise de position - HubSpot.md",
    "événement": "Modèle pour créer un article de couverture d'évènement - HubSpot.md"
}

# --- Chargement CSV ---
def load_csv(filepath):
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [row for row in reader if row["title"] or row["description"]]

# --- Communication avec Ollama ---
def run_prompt(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

# --- Génération d'article ---
def generer_article(depuis_title, sujet, description):
    type_article = detecter_type_article(sujet)
    modele_path = f"./{MODELE_PAR_TYPE[type_article]}"
    with open(modele_path, encoding="utf-8") as f:
        modele = f.read()

    prompt = f"""
Tu es un rédacteur de blog professionnel.

Sujet : {sujet}

Description : {description}

Utilise le modèle suivant pour structurer ton article :

{modele}

Rédige un article complet, bien structuré, en français, au format Markdown.
"""
    resultat = run_prompt(prompt)
    nom_fichier = f"article_genere_{depuis_title}.md"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(resultat)
    print(f"✅ Article généré : {nom_fichier}")

# === MAIN ===
data = load_csv("blog_data_clean.csv")

# Générer un article pour chaque entrée ayant une description
for i, row in enumerate(data):
    if row["description"].strip():
        titre = row["title"].strip() or f"sujet_{i}"
        generer_article(depuis_title=f"{i:02d}", sujet=titre, description=row["description"].strip())