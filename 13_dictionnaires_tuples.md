# Dictionnaires et tuples

## Dictionnaires

Les **dictionnaires** se révèlent très pratiques lorsque vous devez manipuler des structures complexes à décrire et que les listes présentent leurs limites. Les dictionnaires sont des collections non ordonnées d'objets, c'est-à-dire qu'il n'y a pas de notion d'ordre  (*i.e.* pas d'indice). On accède aux **valeurs** d'un dictionnaire par des **clés**. Ceci semble un peu confus ? Regardez l'exemple suivant :
```
>>> ani1 = {}
>>> ani1["nom"] = "girafe"
>>> ani1["taille"] = 5.0
>>> ani1["poids"] = 1100
>>> ani1
{'nom': 'girafe', 'taille': 5.0, 'poids': 1100}
```

En premier, on définit un dictionnaire vide avec les accolades `{}` (tout comme on peut le faire pour les listes avec `[]`). Ensuite, on remplit le dictionnaire avec différentes clés (`"nom"`, `"taille"`, `"poids"`) auxquelles on affecte des valeurs (`"girafe"`, `5.0`, `1100`). Vous pouvez mettre autant de clés que vous voulez dans un dictionnaire (tout comme vous pouvez ajouter autant d'éléments que vous voulez dans une liste).

open-box-rem

Un dictionnaire est affiché sans ordre particulier.

close-box-rem

On peut aussi initialiser toutes les clés et les valeurs d'un dictionnaire en une seule opération :
```
>>> ani2 = {"nom":"singe", "poids":70, "taille":1.75}
```
Mais rien ne nous empêche d'ajouter une clé et une valeur supplémentaire :
```
>>> ani2["age"] = 15
```

Pour récupérer la valeur associée à une clé donnée, il suffit d'utiliser la syntaxe suivante `dictionnaire["cle"]`. Par exemple :
```
>>> ani1["taille"]
5.0
```

open-box-rem

Toutes les clés de dictionnaire utilisées jusqu'à présent étaient des chaînes de caractères. Rien n'empêche d'utiliser d'autres types d'objets comme des entiers ou des *floats*, cela peut parfois s'avérer très utile.

Néanmoins, nous vous conseillons, autant que possible, d'utiliser systématiquement des chaînes de caractères pour vos clés de dictionnaire.

close-box-rem


### Itération sur les clés pour obtenir les valeurs

Il est possible d'obtenir toutes les valeurs d'un dictionnaire à partir de ses clés :
```
>>> ani2 = {'nom':'singe', 'poids':70, 'taille':1.75}
>>> for key in ani2:
...     print(key, ani2[key])
...
poids 70
nom singe
taille 1.75
```


### Méthodes `.keys()` et `.values()`

Les méthodes `.keys()` et `.values()` renvoient, comme vous pouvez vous en doutez, les clés et les valeurs d'un dictionnaire :
```
>>> ani2.keys()
dict_keys(['poids', 'nom', 'taille'])
>>> ani2.values()
dict_values([70, 'singe', 1.75])
```

Les mentions `dict_keys` et `dict_values` indiquent que nous avons affaire à des objets un peu particuliers. Si besoin, nous pouvons les transformer en liste avec la fonction `list()` :
```
>>> ani2.values()
dict_values(['singe', 70, 1.75])
>>> list(ani2.values())
['singe', 70, 1.75]
```


### Existence d'une clé

Pour vérifier si une clé existe dans un dictionnaire, on peut utiliser le test d’appartenance avec l'instruction `in` :
```
>>> if "poids" in ani2:
...     print("La clé 'poids' existe pour ani2")
...
La clé 'poids' existe pour ani2
>>> if "age" in ani2:
...     print("La clé 'age' existe pour ani2")
...
>>>
```

Dans le second test (lignes 5 à 7), le message n'est pas affiché car la clé `age` n'est pas présente dans le dictionnaire `ani2`.


### Liste de dictionnaires

En créant une liste de dictionnaires qui possèdent les mêmes clés,
on obtient une structure qui ressemble à une base de données :
```
>>> animaux = [ani1, ani2]
>>> animaux
[{'nom': 'girafe', 'poids': 1100, 'taille': 5.0}, {'nom': 'singe',
'poids': 70, 'taille': 1.75}]
>>>
>>> for ani in animaux:
...     print(ani['nom'])
...
girafe
singe
```

Vous constater ainsi que les dictionnaires permettent de gérer des structures complexes de manière plus explicite que les listes.


## Tuples

Les **tuples** correspondent aux listes à la différence qu'ils sont **non modifiables**. On a vu dans le chapitre 11 *Plus sur les listes* que les listes pouvaient être modifiées par références, notamment lors de la copie de listes. Les tuples s'affranchissent de ce problème puisqu'ils sont non modifiables. Pratiquement, ils utilisent les parenthèses au lieu des crochets :
```
>>> x = (1,2,3)
>>> x
(1, 2, 3)
>>> x[2]
3
>>> x[0:2]
(1, 2)
>>> x[2] = 15
Traceback (innermost last):
File "<stdin>", line 1, in ?
TypeError: object doesn't support item assignment
```

L'affectation et l'indiçage fonctionnent comme avec les listes. Mais si on essaie de modifier un des éléments du tuple, Python renvoie un message d'erreur. Si vous voulez ajouter un élément (ou le modifier), vous devez créer un autre tuple :
```
>>> x = (1,2,3)
>>> x + (2,)
(1, 2, 3, 2)
```

open-box-rem

Pour utiliser un tuple d'un seul élément, vous devez utiliser une syntaxe avec une virgule `(element,)`, ceci pour éviter une ambiguïté avec une simple expression.

Autre particularité des tuples, il est possible d'en créer de nouveaux sans les parenthèses, dès lors que ceci ne pose pas d'ambiguïté avec une autre expression :
```
>>> x = (1,2,3)
>>> x
(1, 2, 3)
>>> x = 1,2,3
>>> x
(1, 2, 3)
```
Toutefois, nous vous conseillons d'utiliser systématiquement les parenthèses afin d'éviter les confusions.

close-box-rem

Enfin, on peut utiliser la fonction `tuple(sequence)` qui fonctionne exactement comme la fonction `list()`, c'est-à-dire qu'elle prend en argument un objet séquentiel et renvoie le tuple correspondant (opération de *casting*) :
```
>>> tuple([1,2,3])
(1, 2, 3)
>>> tuple("ATGCCGCGAT")
('A', 'T', 'G', 'C', 'C', 'G', 'C', 'G', 'A', 'T')
```

open-box-rem

Les listes, les dictionnaires et les tuples sont des objets qui peuvent contenir des collections d'autres objets. On peut donc construire des listes qui contiennent des dictionnaires, des tuples ou d'autres listes, mais aussi des dictionnaires contenant des tuples, des listes, etc.

close-box-rem

Pratiquement, nous avons déjà croisé les tuples avec la fonction `enumerate()` dans le chapitre 5 *Boucles et comparaisons* qui renvoie l'indice de l'élément et l'élément d'une liste, ainsi dans le chapitre 9 *Fonctions* lorsqu'on voulait qu'une fonction renvoie plusieurs valeurs (par exemple dans l'instruction `return x,y`, le couple `x,y` est un tuple).


## Exercices

*Conseil* : pour ces exercices, écrivez des scripts dans des fichiers, puis exécutez-les dans un *shell*.


### Composition en acides aminés

En utilisant un dictionnaire, déterminez le nombre d’occurrences de chaque acide aminé dans la séquence `AGWPSGGASAGLAILWGASAIMPGALW`. Le dictionnaire ne doit contenir que les acides aminés présents dans la séquence.


### Mots de 2 lettres

Soit la séquence nucléotidique suivante :  
`ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG`

En utilisant un dictionnaire, créez un programme qui répertorie tous les mots de 2 lettres qui existent dans la séquence (`AC`, `CC`, `CT`, `AG`, etc.) ainsi que leur nombre d’occurrences, puis qui les affiche à l'écran. Voici un exemple de sortie attendue :
```
CT : 8
TC : 2
GC : 7
[...]
```


### Mots de 3 lettres

Faites de même avec des mots de 3 lettres.


### Mots de 2 lettres dans le génome de *Saccharomyces cerevisiae*

En vous basant sur les scripts précédents, extrayez les mots de 2 lettres et leurs occurrences dans le génome du chromosome I de la levure du boulanger *Saccharomyces cerevisiae* (fichier [`NC_001133.fna`](https://python.sdv.univ-paris-diderot.fr/data-files/NC_001133.fna)).

Le génome complet est fourni au format FASTA. Vous trouverez des explications sur ce format et des exemples de code dans l'annexe A *Quelques formats de données rencontrés en biologie*.


### Mots de *n* lettres et fichiers FASTA

Créez un script `extract-words.py` qui prend en arguments le nom d'un fichier Fasta suivi d'un entier compris entre 1 et 4. Ce script doit extraire du fichier Fasta tous les mots (ainsi que leur nombre d’occurrences) du nombre de lettres passées en option.


### Mots de *n* lettres du génome d'*E. Coli*

Appliquez ce script sur le génome d'*Escherichia coli* : fichier [`NC_000913.fna`](https://python.sdv.univ-paris-diderot.fr/data-files/NC_000913.fna). Attention, le génome complet est fourni au format fasta.

Cette méthode vous paraît-elle efficace sur un génome assez gros comme celui d'*E. Coli* ? Comment pourrait-on en améliorer la rapidité ?


### Dictionnaire et carbone alpha

À partir du fichier PDB [1BTA](http://www.rcsb.org/pdb/files/1BTA.pdb), construisez un dictionnaire qui contient 4 clés se référant au premier carbone alpha : le numéro du résidu, puis les coordonnées atomiques *x*, *y* et *z*.


### Dictionnaire et PDB

Sur le même modèle que ci-dessus, créez une liste de dictionnaires pour chacun des carbones alpha de la protéine.


### Barycentre d'une protéine

À l'aide de cette liste, calculez les coordonnées *x*, *y* et *z* du barycentre de ces carbones alpha.
