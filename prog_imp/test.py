from bs4 import BeautifulSoup
import csv

INPUT_FILE = "algo/produits.html"
OUTPUT_FILE = "algo/produits.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

rows = []

for li in soup.select("li.ajax_block_product"):

    name_tag = li.select_one(".right_content h3 a")
    name = name_tag.get_text(strip=True) if name_tag else ""

    desc_tag = li.select_one(".right_content p.product_desc")
    desc = desc_tag.get_text(strip=True) if desc_tag else ""

    price_tag = li.select_one(".right_content .price-box .price")
    price = price_tag.get_text(strip=True) if price_tag else ""

    rows.append([name, desc, price])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Nom", "Description", "Prix"])
    writer.writerows(rows)

print(f"OK ! {len(rows)} produits écrits dans {OUTPUT_FILE}")
