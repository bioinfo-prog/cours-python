### Calcul du centre de masse d'une membrane

L'image de gauche de la figure @fig:exo_get_leaflet montre le cliché d'une membrane de POPC (cyan) entourée d'eau (bleu) (coordonnées trouvées [ici](https://zenodo.org/record/153944)). Les atomes de phosphore des groupes phosphates sont représentés en boule de van der Waals brune. Dans cet exercice, on cherche à calculer le centre de masse de la membrane, ainsi que le centre de masse (COM) de chaque monocouche de phosphores. Ces COM sont représentés sous forme de croix dans le graphique de droite de la figure @fig:exo_get_leaflet.

![Cliché d'une membrane de POPC.](img/exo_get_leaflet.png){ #fig:exo_get_leaflet width=95% }

Les coordonnées cartésiennes $(x, y, z)$ de chaque atome de phosphore (en Å) sont stockées dans le fichier [coors_P.dat](https://python.sdv.u-paris.fr/data-files/coors_P.dat), à raison d'un atome par ligne.

Nous vous proposons les étapes suivantes pour résoudre cet exercice à l'aide du module *NumPy* :

1. Récupérez les coordonnées des atomes de phosphore depuis le fichier `coors_P.dat` et stockez-les dans un *array* 2D (matrice) `coors_P`. La dimensionnalité de cette matrice est $n \times 3$, avec $n$ le nombre de phosphores.
2. Calculez le $z$ moyen de tous les phosphores (nombre réel) et stockez-le dans la variable `mean_z`. La méthode `.mean()` vous sera utile.
3. Avec des masques de booléens, récupérez les coordonnées des phosphores de la monocouche du haut dans un *array* 2D `upper`. Faites de même avec la monocouche du bas dans un *array* 2D `lower`.
4. Calculez le centre de masse `COM` de la membrane, ainsi que de la monocouche du haut `COM_upper` et du bas `COM_lower`. Pensez aux méthodes de calcul sur les *arrays* et l'argument `axis`.
5. Une fois tout cela effectué, créez un graphique 3D pour représenter les différents centres de masse. Utilisez la fonction `scatter()` du module *matplotlib* pour l'[affichage en 3D](https://matplotlib.org/3.2.1/gallery/mplot3d/scatter3d.html). Voici un squelette de programme pour vous aider :


```python
# Initialisation du graphique.
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()                       
ax = fig.add_subplot(111, projection="3d")
[...]
# X, Y et Z sont des arrays 1D de n éléments.
# Par exemple X représente tous les x des P de la monocouche upper.
[...]
# Affichage de la couche upper.
ax.scatter(X, Y, Z, c="salmon", marker="o")
# Affichage du COM de la couche upper.
ax.scatter(x, y, z, c="red", marker="x")
[...]
# Affichage des étiquettes des axes et du titre.
ax.set_xlabel("x (Å)")
ax.set_ylabel("y (Å)")
ax.set_zlabel("z (Å)")
ax.set_title("Graphe 3D des phosphores")
plt.show()
```
