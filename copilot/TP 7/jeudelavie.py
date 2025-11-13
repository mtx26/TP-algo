import os

def next_state(grid, i, j):
    """
    Détermine si la cellule (i, j) sera vivante à l'étape suivante.
    """
    n = len(grid)
    m = len(grid[0])
    voisins_vivants = 0

    # Parcourt les 8 voisins
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x == i and y == j) or x < 0 or y < 0 or x >= n or y >= m:
                continue
            if grid[x][y]:
                voisins_vivants += 1

    # Règles du jeu de la vie
    if grid[i][j]:
        return voisins_vivants == 2 or voisins_vivants == 3
    else:
        return voisins_vivants == 3


def next_grid(grid):
    """
    Calcule la nouvelle grille selon les règles.
    """
    n = len(grid)
    m = len(grid[0])
    new_grid = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_grid[i][j] = next_state(grid, i, j)

    return new_grid


def display_grid(grid):
    """
    Affiche la grille proprement à l'écran.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    for row in grid:
        for cell in row:
            print("█" if cell else " ", end="")
        print()
    print()


def simulate_life(grid, t):
    """
    Simule le jeu pendant t étapes, avec une pause entre chaque étape via input().
    """
    current_grid = grid
    for step in range(t):
        display_grid(current_grid)
        print(f"Étape {step + 1}/{t}")
        input("Appuyez sur [Entrée] pour continuer...")
        current_grid = next_grid(current_grid)
    return current_grid


# Exemple de grille initiale (oscillateur)
initial_grid = [
    [False, False, False, False, False],
    [False, False, True,  False, False],
    [False, False, True,  False, False],
    [False, False, True,  False, False],
    [False, False, False, False, False],
]

# Lancement de la simulation
simulate_life(initial_grid, t=10)