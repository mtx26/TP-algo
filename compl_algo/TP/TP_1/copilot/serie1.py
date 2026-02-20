# --- Partie 1 : Structures de données simples ---

# 1. Historique d'actions d'un utilisateur
historique = ["connexion", "visite_page", "deconnexion"]

# 2. Constantes d'une application
CONSTANTES = frozenset({3.14, 2.718, 1.618})

# 3. Coordonnées (x, y) d'un point fixe
coordonnees = (10, 20)

# 4. Options sélectionnées par un utilisateur
options = {"mode_sombre", "notifications_actives"}

# 5. Registre d'emprunt de livre
registre = {"Le Nom de la Rose": "Alice", "Dune": "Bob"}

# 6. ADN d'un organisme
adn = "ATCGGCTA"


# --- Partie 2 : Combinaisons de structures de données ---

# 1. Base de données de recettes (sans doublons)
recettes = {
    ("farine", "oeufs", "lait", "sucre"),
    ("pâtes", "oeufs", "lardons", "parmesan")
}

# 2. Notes des étudiants
notes = {
    ("Dupont", "Jean"): {"Mathématiques": 15, "Physique": 14},
    ("Martin", "Alice"): {"Mathématiques": 18, "Histoire": 16}
}

# 3. Programmes télévisés par catégorie
programmes = (
    ("sport", frozenset({"Match de foot", "Tennis"})),
    ("documentaire", frozenset({"Planète Terre", "Histoire ancienne"}))
)


# --- 1.2 Capitaine Edward ---

# 3. Liste de listes
map_list = [
    [0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 40, 0, 0],
    [20, 0, 0, 0, 0]
]

# 4. Dictionnaire de coordonnées
map_dict = {
    (0, 4): 10,
    (3, 2): 40,
    (4, 0): 20
}

# 5. get_treasure
def get_treasure(treasure_map, coords):
    return treasure_map.get(coords, 0)

# 6. add_treasure
def add_treasure(treasure_map, coords, amount):
    treasure_map[coords] = treasure_map.get(coords, 0) + amount

# 7. set_treasure
def set_treasure(treasure_map, coords, amount):
    if amount == 0:
        if coords in treasure_map:
            del treasure_map[coords]
    else:
        treasure_map[coords] = amount


# --- 1.3 Combinaison de cartes ---

# 8. add_map
def add_map(map1, map2):
    result = map1.copy()
    for coords, amount in map2.items():
        result[coords] = result.get(coords, 0) + amount
        if result[coords] == 0:
            del result[coords]
    return result


# --- 9. Code Golf ---

# Tâche 1 : Carrés des nombres pairs
print([x**2 for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0])

# Tâche 2 : Carrés communs de nombres impairs
print(list(set(x**2 for x in [1, 2, 3, 3, 5, 7, 9] if x % 2 != 0) & set(y**2 for y in [3, 4, 7, 5, 3, 7, 11] if y % 2 != 0)))

# Tâche 3 : Conversion en (min, sec), < 10 min, ordre décroissant
print(sorted([(t // 60, t % 60) for t in [620, 450, 800, 390, 720, 550] if t < 600], reverse=True))

# Tâche 4 : Nombres cachés, multiples de 3, mis au cube
import re; print([int(n)**3 for s in ["abc42de", "hello9world", "xyz8pq", "27abc", "100foo", "1a2b3c"] for n in re.findall(r'\d+', s) if int(n) % 3 == 0])