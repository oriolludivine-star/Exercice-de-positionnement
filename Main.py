# Christmas lights Kata
import numpy as np
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
print(f"Nombre de lumières allumées: {lights_on}")


# PARTIE 2 : Calculer le niveau de luminosité
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

total_brightness = np.sum(grid)
print("=" * 50)
print("RÉSULTAT - PARTIE 2: CONTRÔLE DE LUMINOSITÉ")
print(f"Luminosité totale: {total_brightness}")
print("=" * 50)












