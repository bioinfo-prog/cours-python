### Calcul du centre de masse d'une membrane

Dans cet exercice, on doit avoir bien en tête la forme des données. On va utiliser un *array* 2D, c'est-à-dire une matrice, contenant les coordonnées des $n$ phosphores présents dans le fichier :

```text
x_1  y_1  z_1
x_2  y_2  z_2
[...]
x_n  y_n  z_n
```

Voici le code proposé que nous commentons ci-dessous :

```python
import numpy as np
import matplotlib.pyplot as plt
# Pour faire un scatter plot en 3D.
from mpl_toolkits.mplot3d import Axes3D

#======================
# Calculs.
#======================
# Récupérer les coordonnées des P en array 2D.
coors_P = np.loadtxt("coors_P.dat")
# coors_P est une matrice (2D array) n*3 : n phosph * 3 coors (x, y, z).

# Calculer le z moyen pour tous les P.
mean_z = coors_P[:,2].mean()

# Selectionner les coordonnées upper leaflet.
coors_upper = coors_P[coors_P[:,2] > mean_z]

# Selectionner les coordonnées lower leaflet.
coors_lower = coors_P[coors_P[:,2] < mean_z]

# Calculer le COM.
COM = coors_P.mean(axis=0)
COM_upper = coors_upper.mean(axis=0)
COM_lower = coors_lower.mean(axis=0)

#======================
# Graphique en 3D.
#======================
# Initialiser le graphique.
fig = plt.figure()                       
ax = fig.add_subplot(111, projection="3d")

# Afficher le upper leaflet.
X, Y, Z = coors_upper.T
ax.scatter(X, Y, Z, c="salmon", marker="o")
x, y, z = COM_upper
ax.scatter(x, y, z, c="red", marker="x")

# Afficher le lower leaflet.
X, Y, Z = coors_lower.T
ax.scatter(X, Y, Z, c="cyan", marker="o")
x, y, z = COM_lower
ax.scatter(x, y, z, c="blue", marker="x")

# Afficher le COM.
x, y, z = COM
ax.scatter(x, y, z, c="green", marker="x")

# Ajouter les étiquettes pour les axes et le titre.
ax.set_xlabel("x (Å)")
ax.set_ylabel("y (Å)")
ax.set_zlabel("z (Å)")
ax.set_title("Graphe 3D des phosphores")
```

Voici quelques commentaires à propos des lignes de code « délicates » :

- Ligne `mean_z = coors_P[:,2].mean()`. On récupère la colonne d'indice 2 (c'est-à-dire la 3ème colonne) contenant les coordonnées $z$ des phosphates, soit un *array* 1D, sur lequel on calcule la moyenne avec la méthode `.mean()`.

- Ligne `coors_upper = coors_P[coors_P[:,2] > mean_z]`. L'expression `coors_P[:,2] > mean_z` renvoie un *array* 1D de booléens. Il ressemblera à `array([True,  True, ..., False, False])` et aura autant d'éléments que le nombre de lignes de `coors_P`. On se souvient par ailleurs qu'un indiçage unique d'un *array* 2D, du type `coors_P[i]` sélectionne la lignes d'indice `i`. Ainsi, l'*array* 1D de booléen va sélectionner **toutes les lignes** de `coors_P` qui nous intéressent et `coors_upper` sera un *array* 2D.

Pour bien comprendre cette subtilité, prenons un exemple simple avec l'*array* 2D $4 \times 5$ suivant :

```python
a = np.resize(range(25), (4, 5)).T
a
```

```text
array([[ 0,  5, 10, 15],
       [ 1,  6, 11, 16],
       [ 2,  7, 12, 17],
       [ 3,  8, 13, 18],
       [ 4,  9, 14, 19]])
```

L'indiçage unique sélectionne une ligne :

```python
a[1]
```

```text
array([ 1,  6, 11, 16])
```

Si on utilise une tranche, on sélectionne plusieurs lignes :

```python
a[1:3]
```

```text
array([[ 1,  6, 11, 16],
       [ 2,  7, 12, 17]])
```

Maintenant imaginons que nous souhaitions sélectionner les lignes pour lesquelles l'élément de la colonne d'indice 1 est pair, on récupère l'*array* 1D suivant :

```python
a[:,1] % 2 == 0
```

```text
array([False,  True, False,  True, False])
```

Les booléens à `True` satisfont la condition. Si on utilise cet *array* 1D comme indice, on récupère les lignes correspondantes (d'indice 1 et 3) :

```python
a[a[:,1] % 2 == 0]
```

```text
array([[ 1,  6, 11, 16],
       [ 3,  8, 13, 18]])
```

Finalement, l'*array* 1D de booléens agit un peu comme une tranche dans le sens où on sélectionne seulement une partie des lignes, sauf qu'ici elles ne sont pas forcément consécutives et elles satisfont la condition `a[:,1] % 2 == 0`.

- Ligne `COM = coors_P.mean(axis=0)`. Ici on utilise la méthode `.mean()`, calcul de la moyenne, en précisant l'axe 0. `coors_P` est un *array* 2D de la forme :

```text
x_1  y_1  z_1
x_2  y_2  z_2
[...]
x_n  y_n  z_n
```

L'axe 0 signifie que le calcul de la moyenne est fait le long de l'axe 0, c'est-à-dire le long des lignes : on calcule la moyenne sur $x_1, x_2, ..., x_n$, $y_1, y_2, ..., y_n$, et $z_1, z_2, ..., z_n$. Ainsi, on récupère une valeur par colonne sous forme d'un *array* 1D contenant les $x, y, z$ moyens. 

Si on avait précisé `axis=1` le calcul aurait été fait le long des colonnes, c'est-à-dire : la moyenne sur $x_1, y_1, z_1$, puis $x_2, y_2, z_2$, ..., et enfin $x_n, y_n, z_n$. On aurait récupéré un *array* 1D avec une valeur moyenne par ligne.

Pour toutes ces opérations « délicates », il est vivement conseillé de s'entrainer dans l'interpréteur pour bien comprendre toutes les subtilités de *NumPy*. La puissance de ce module permet d'écrire des lignes de code extrêmement compactes pour faire des choses complexes. Il est donc essentiel de soigner la documentation et les commentaires pour ne pas perdre le lecteur du code !
