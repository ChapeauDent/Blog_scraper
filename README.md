# 🐝 Blog Scraper & Générateur d’Idées d’Articles avec IA locale (Ollama)

Ce projet permet de :

1. 📥 Scraper toutes les pages internes d’un site (type blog)
2. ✨ Extraire les balises `<title>` et `<meta name="description">`
3. 🧠 Filtrer automatiquement les articles pertinents via une IA locale (Ollama)
4. 💡 Générer de nouvelles idées d’articles similaires
5. 📝 Exporter le tout au format `.md` prêt pour la rédaction

---

## 🧰 Prérequis

### 1. Installer Python (si ce n’est pas déjà fait)

- 🔗 https://www.python.org/downloads/
- ✅ Pendant l’installation : cochez "Add Python to PATH"
- ▶️ Cliquez sur "Install Now"

Vérifiez avec :
```bash
python --version
```

---

### 2. Installer Ollama (IA locale)

- 🔗 https://ollama.com
- Téléchargez et installez pour Windows, macOS ou Linux
- Ensuite, dans un terminal, lancez :

```bash
ollama pull mistral
```

*(ou `llama3`, `llama2`, `gemma`, etc.)*

---

## 🚀 Lancer le projet

### 📁 Structure du dossier

Placez tous ces fichiers dans un même dossier :

```
blog_scraper/
├── blog_scraper.py               # Scraper du site
├── install_and_run.py            # Installation + exécution du scraper
├── launch_scraper.bat            # Double-clic sous Windows
├── run_prompts_with_ollama.py    # Génère les fichiers Markdown avec l'IA
├── launch_ollama_prompts.bat     # Double-clic pour l’IA locale
└── README.md                     # Ce fichier
```

---

### 🟩 Étapes en un clic (Windows)

1. Double-cliquez sur `launch_scraper.bat`
2. Entrez l’URL du site à scraper dans la fenêtre pop-up
3. Attendez la génération du fichier `blog_data_clean.csv`
4. Ensuite, exécutez (dans un terminal) :

```bash
python run_prompts_with_ollama.py
```

💥 Deux fichiers Markdown seront générés :
- `articles_filtrés.md` → uniquement les contenus de blog
- `nouvelles_idees_articles.md` → idées d’articles à rédiger

---

## 🧠 Prompts utilisés avec Ollama

### 🧩 Prompt 1 — Filtrer les articles de blog

```
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
```

---

### 💡 Prompt 2 — Générer de nouvelles idées d’articles

```
Tu es un expert en rédaction de contenu pour blogs.

Voici une liste de titres et descriptions d’articles existants. Propose 10 nouvelles idées d’articles dans le même style (thématique, ton, audience).

Pour chaque idée :
- Un titre accrocheur
- Une description d’1 à 2 phrases

Format Markdown :
### Titre proposé
*Description de l’idée*
```

---

## 🔚 Résultat final

Vous obtiendrez automatiquement :

- 🗂️ `blog_data_clean.csv` → données extraites du site
- 📝 `articles_filtrés.md` → uniquement les contenus de type blog
- 💡 `nouvelles_idees_articles.md` → idées fraîches à rédiger

---

## ❓ Support

- 🧪 Vérifiez que Ollama est bien lancé (`ollama run mistral`)
- 📦 Vérifiez que `requests`, `beautifulsoup4` et `tkinter` sont installés
- 💡 Vous pouvez relancer `python install_and_run.py` à tout moment

Bon scraping, bonne inspiration ! 🍯✍️
