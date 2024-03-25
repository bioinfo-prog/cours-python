### Triangle de Pascal (exercice +++)

À part la première ligne, chaque ligne du triangle de Pascal est composée d'une série de nombres dont le premier et le dernier nombre est 1.

Chaque ligne est calculée à partir de la précédente de la façon suivante :

```text
1       1
        |
      1 + 1
        |
1       2       1
        |       |
      1 + 2   2 + 1
        |       |
1       3       3       1
        |       |       |
      1 + 3   3 + 3   3 + 1
        |       |       |
1       4       6       4       1
[...]
```

Voici un exemple de code pour construire le triangle de Pascal :

```python
triangle = []

for n in range(10):
    # Le premier nombre de chaque ligne est 1.
    ligne_actuelle = [1]
    if n > 0:
        ligne_avant = triangle[n-1]
        for indice in range(1, len(ligne_avant)):
            ligne_actuelle.append(ligne_avant[indice-1]+ligne_avant[indice])
        # Le dernier nombre de chaque ligne est 1.
        ligne_actuelle.append(1)
    triangle.append(ligne_actuelle)

with open("pascal.out", "w") as fichier:
    for ligne in triangle:
        for nombre in ligne:
            fichier.write(f"{nombre} ")
        fichier.write("\n")
```

Résultat obtenu dans le fichier `pascal.out` :

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
```
