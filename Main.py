# Christmas lights Kata
import numpy as np

"""initialisaton de la grille, création d'un tableau bidemsionnels 
de 1000*1000 guirlandes, où l'etat des lumières est False = éteint et True = allumé

Avec boucles Python:
grille = [[False] * 1000 for _ in range(1000) ]

def traiter_instruction(action, x1, x2, y1, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            if action == "Turn on":
                grille [y][x] = True
            elif action == "Turn off":
                grille [y][x] = False
            elif action == "Toggle":
                grille [y][x] = not grille[y][x]"""


# Avec le slicing Numpy :
# Création d'une grille de 1000 x 1000 lumières éteintes = False
grid = np.zeros((1000, 1000), dtype=bool)

# Création d'une liste [] d'instructions
instructions = [
    ("turn on", 887, 9, 959, 629),
    ("turn on", 454, 398, 844, 448),
    ("turn off", 539, 243, 559, 965),
    ("turn off", 370, 819, 676, 868),
    ("turn off", 145, 40, 370, 997),
    ("turn off", 301, 3, 808, 453),
    ("turn on", 351, 678, 951, 908),
    ("toggle", 720, 196, 897, 994),
    ("toggle", 831, 394, 904, 860),
]

instruction: tuple[str, int, int, int, int]
for instruction in instructions:
    action = instruction[0]
    x1, y1, x2, y2 = instruction[1], instruction[2], instruction[3], instruction[4]

if action == "turn on":
        grid[x1:x2+1, y1:y2+1] = True
elif action == "turn off":
        grid[x1:x2+1, y1:y2+1] = False
elif action == "toggle":
        grid[x1:x2+1, y1:y2+1] = ~grid[x1:x2+1, y1:y2+1]


lights_on = np.sum(grid)
print("="* 50)
print("RÉSULTAT - GUIRLANDES DE NOËL PARTIE 1 ")
print("="* 50)
print(f"Nombre de lumières allumées : {lights_on}")
print(f"Total de lumières : {grid.size}")
print(f"Lumières éteintes : {grid.size - lights_on}")


# PARTIE 2 : Traiter chaque instruction
grid = np.zeros((1000, 1000), dtype=int)  # dtype=int au lieu de bool !

for instruction in instructions:
    action = instruction[0]
    x1, y1, x2, y2 = instruction[1], instruction[2], instruction[3], instruction[4]

    if action == "turn on":
        # Augmenter la luminosité de +1
        grid[x1:x2 + 1, y1:y2 + 1] += 1

    elif action == "turn off":
        # Diminuer la luminosité de -1 (mais pas en dessous de 0)
        grid[x1:x2 + 1, y1:y2 + 1] -= 1
        grid[x1:x2 + 1, y1:y2 + 1] = np.maximum(grid[x1:x2 + 1, y1:y2 + 1], 0)
        # np.maximum() garantit qu'aucune valeur ne descend sous 0

    elif action == "toggle":
        # Augmenter la luminosité de +2
        grid[x1:x2 + 1, y1:y2 + 1] += 2


# Calculer la luminosité totale
total_brightness = np.sum(grid)

# Afficher les résultats
print("=" * 50)
print("RÉSULTAT - PARTIE 2 : CONTRÔLE DE LUMINOSITÉ")
print("=" * 50)
print(f"Luminosité totale : {total_brightness}")
print(f"Luminosité moyenne par lumière : {np.mean(grid):.2f}")
print(f"Luminosité maximale d'une lumière : {np.max(grid)}")
print(f"Luminosité minimale d'une lumière : {np.min(grid)}")
print(f"Nombre de lumières éteintes (0) : {np.sum(grid == 0)}")
print(f"Nombre de lumières allumées (>0) : {np.sum(grid > 0)}")
print("=" * 50)











