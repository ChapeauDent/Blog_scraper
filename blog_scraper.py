import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

# --- Fenêtre pop-up pour demander l'URL ---
root = tk.Tk()
root.withdraw()  # Ne pas afficher la fenêtre principale

site_url = simpledialog.askstring("Saisie URL", "Entrez l'URL du site à scraper :")

if not site_url:
    messagebox.showinfo("Annulé", "Aucune URL fournie. Script interrompu.")
    exit()

visited = set()

def get_all_links(base_url, max_depth=2, current_depth=0):
    if current_depth > max_depth or base_url in visited:
        return set()

    print(f"Scraping: {base_url}")
    visited.add(base_url)

    try:
        response = requests.get(base_url, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"Erreur : {e}")
        return set()

    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for link_tag in soup.find_all("a", href=True):
        href = link_tag["href"]
        full_url = urljoin(base_url, href)

        parsed = urlparse(full_url)
        if parsed.netloc == urlparse(base_url).netloc:
            if full_url not in visited:
                links.add(full_url)

    for link in links.copy():
        links.update(get_all_links(link, max_depth, current_depth + 1))

    return links

urls = get_all_links(site_url)

print("\nToutes les URLs trouvées :")
for url in sorted(urls):
    print(url)

def extract_title_description(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"[404 ignorée] {url}")
        else:
            print(f"Erreur HTTP : {e}")
        return {"url": url, "title": "", "description": ""}
    except Exception as e:
        print(f"Erreur lors de la récupération de {url} : {e}")
        return {"url": url, "title": "", "description": ""}

    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})

    title = title_tag.text.strip() if title_tag else ""
    description = meta_desc_tag["content"].strip() if meta_desc_tag and "content" in meta_desc_tag.attrs else ""

    return {"url": url, "title": title, "description": description}

clean_data = []
for url in sorted(urls):
    data = extract_title_description(url)
    if data["title"] or data["description"]:
        clean_data.append(data)
    time.sleep(1)

with open("blog_data_clean.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["url", "title", "description"], delimiter=";")
    writer.writeheader()
    for row in clean_data:
        writer.writerow(row)

print(f"\nNettoyage terminé. {len(clean_data)} pages valides enregistrées dans 'blog_data_clean.csv'")
