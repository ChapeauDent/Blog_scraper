import csv
import requests

MODEL = "mistral"  # ou llama2, llama3, etc.
OLLAMA_URL = "http://localhost:11434/api/generate"

def run_prompt(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

def load_csv(filepath):
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [row for row in reader if row["title"] or row["description"]]

def build_markdown_input(data):
    markdown = ""
    for row in data:
        markdown += f"- {row['title'].strip()}\n  {row['description'].strip()}\n\n"
    return markdown

# === Chargement des données ===
entries = load_csv("blog_data_clean.csv")
content_markdown = build_markdown_input(entries)

# === Prompt 1 : Filtrer les articles de blog ===
prompt_filter = f"""
Tu es un assistant spécialisé dans l’analyse de contenus web.

Voici une liste de titres et descriptions de pages d’un site web. Sélectionne uniquement les éléments qui correspondent à des articles de blog.

Ignore :
- Accueil, contact, à propos
- Produits ou services
- Mentions légales, CGU
- Catégories, filtres, navigation

Formate la sortie en Markdown :
### Titre de l’article
*Description de l’article*

Voici la liste :

{content_markdown}
"""

filtered_result = run_prompt(prompt_filter)

with open("articles_filtrés.md", "w", encoding="utf-8") as f:
    f.write(filtered_result)

print("✅ Fichier articles_filtrés.md généré.")

# === Prompt 2 : Générer des idées d’articles ===
prompt_ideas = f"""
Tu es un expert en rédaction de contenu pour blogs.

Voici une liste de titres et descriptions d’articles existants :

{content_markdown}

Propose 10 nouvelles idées d’articles dans le même style (thématique, ton, audience).

Pour chaque idée :
- Un titre accrocheur
- Une description d’1 à 2 phrases

Formate en Markdown :
### Titre proposé
*Description de l’idée*
"""

ideas_result = run_prompt(prompt_ideas)

with open("nouvelles_idees_articles.md", "w", encoding="utf-8") as f:
    f.write(ideas_result)

print("✅ Fichier nouvelles_idees_articles.md généré.")
