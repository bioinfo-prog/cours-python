# Dictionnaires et tuples

Dans ce chapitre, nous allons voir deux nouveaux types d'objet qui s'avèrent extrêmement utiles : les dictionnaires et les tuples. Comme les listes vues dans le chapitre 4, les dictionnaires et tuples contiennent une collection d'autres objets. Toutefois, nous verrons que ces trois types sont régis par des règles différentes pour accéder à leur contenu, ainsi que dans leur fonctionnement.

## Dictionnaires

### Définition

open-box-def

Un **dictionnaire** contient une collections d'objets Python auxquels on accède à l'aide d'une **clé** de correspondance plutôt qu'un indice. Ainsi, il ne s'agit pas d'objets séquentiels comme les listes, mais plutôt d'objets dits de correspondance (*mapping objects* en anglais) ou tableaux associatifs.

close-box-def

Ceci étant défini, comment fonctionnent-ils exactement ? Regardons un exemple :

```python
>>> ani1 = {}
>>> ani1["nom"] = "girafe"
>>> ani1["taille"] = 5.0
>>> ani1["poids"] = 1100
>>> ani1
{'nom': 'girafe', 'taille': 5.0, 'poids': 1100}
```

Ligne 1. On définit un dictionnaire vide avec les accolades `{}` (tout comme on peut le faire pour les listes avec `[]`). Lignes 2 à 4, on remplit le dictionnaire avec différentes clés (`"nom"`, `"taille"`, `"poids"`) auxquelles on affecte des valeurs (`"girafe"`, `5.0`, `1100`). 

Ligne 5. On affiche le contenu du dictionnaire. Les accolades nous montre qu'il s'agit bien d'un dictionnaire, et pour chaque élément séparé par une virgule on a une association du type `clé: valeur`. On voit que les clés sont des chaînes de caractères (ce qui sera souvent le cas), et les valeurs peuvent être n'importe quel objet Python.

Une fois le dictionnaire créé, on récupére la valeur associée à une clé donnée avec une syntaxe du type `dictionnaire["clé"]`. Par exemple :

```python
>>> ani1["nom"]
'girafe'
>>> ani1["taille"]
5.0
```

On se souvient que pour accéder à l'élément d'une liste, il fallait utiliser un indice (par exemple, `liste[2]`). Ici, l'utilisation d'une clé - qui est souvent une chaîne de caractères - rend les choses plus explicites.

Vous pouvez mettre autant de couples clé / valeur que vous voulez dans un dictionnaire (tout comme vous pouvez ajouter autant d'éléments que vous voulez dans une liste).

open-box-rem

Jusqu'à la version 3.6 de Python, un dictionnaire était affiché sans ordre particulier. L'ordre d'affichage des éléments n'était pas forcément le même que celui dans lequel il avait été rempli. De même lorsqu'on itérait dessus, l'ordre n'était pas garanti. Depuis Python 3.7 (inclus), ce comportement a changé, un dictionnaire est toujours affiché dans le même ordre que celui utilisé pour le remplir. De même, si on itère sur un dictionnaire, cet ordre est respecté. Ce détail provient de l'implémentation interne des dictionnaires dans Python, mais cela nous concerne peu. Ce qui importe, c'est de se rappeler qu'on accède aux éléments par leur clé, et non par leur position lorsque le dictionnaire est affiché. Donc cet ordre n'a pas d'importance spéciale sauf dans de rares cas.

close-box-rem

On peut aussi initialiser toutes les clés et les valeurs d'un dictionnaire en une seule opération :

```python
>>> ani2 = {"nom": "singe", "poids": 70, "taille": 1.75}

```
Mais rien ne nous empêche d'ajouter une clé et une valeur supplémentaire :

```python
>>> ani2["age"] = 15
>>> ani2
{'nom': 'singe', 'poids': 70, 'taille': 1.75, 'age': 15}
```

Après ce premier tour d'horizon, on voit tout de suite l'avantage des dictionnaires. Pouvoir retrouver des éléments par des noms (clés) plutôt que par des indices.

Les humains retiennent mieux les noms que les chiffres. Ainsi, les dictionnaires se révèlent très pratiques lorsque vous devez manipuler des structures complexes à décrire et que les listes présentent leurs limites. L'usage des dictionnaires rend en général le code plus lisible. Par exemple, si nous souhaitions stocker les coordonnées $(x, y, z)$ d'un point dans l'espace, nous pourrions utiliser `coors = [0, 1, 2]` pour la version liste et `coors = {"x": 0, "y": 1, "z": 2}` pour la version dictionnaire. Quelqu'un qui lit le code comprendra tout de suite que `coors["z"]` contient la coordonnée $z$, ce sera moins intuitif avec `coors[2]`.

open-box-adv

Nous verrons dans le chapitre 14 *Conteneurs* que plusieurs types d'objets sont utilisables en tant que clé de dictionnaire. Malgré cela, nous conseillons de n'utiliser que des chaînes de caractères lorsque vous débutez.

close-box-adv

### Itération sur les clés pour obtenir les valeurs

Si on souhaite voir toutes les associations clés / valeurs, on peut itérer sur un dictionnaire de la manière suivante :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> for key in ani2:
...     print(key, ani2[key])
...
poids 70
nom singe
taille 1.75
```

Par défaut, l'itération sur un dictionnaire se fait sur les clés. Dans cet exemple, la variable d'itération `key` prend successivement la valeur de chaque clé, `ani2[key]` donne la valeur correspondant à chaque clé.

### Méthodes `.keys()` et `.values()`

Les méthodes `.keys()` et `.values()` renvoient, comme vous vous en doutez, les clés et les valeurs d'un dictionnaire :

```python
>>> ani2.keys()
dict_keys(['poids', 'nom', 'taille'])
>>> ani2.values()
dict_values([70, 'singe', 1.75])
```

Les mentions `dict_keys` et `dict_values` indiquent que nous avons à faire à des objets un peu particuliers. Ils ne sont pas indexables (on ne peut pas retrouver un élément par indice, par exemple `dico.keys()[0]` renverra une erreur). Si besoin, nous pouvons les transformer en liste avec la fonction `list()` :

```python
>>> ani2.values()
dict_values(['singe', 70, 1.75])
>>> list(ani2.values())
['singe', 70, 1.75]
```

Toutefois, on peut itérer dessus dans une boucle (on dit qu'ils sont itérables) :

```python
>>> for cle in ani2.keys():
...     print(cle)
...
nom
poids
taille
```

### Méthode `.items()`

La méthode `.items()` renvoie un nouvel objet `dict_items` :

```python
>>> dico = {0: "t", 1: "o", 2: "t", 3: "o"}
>>> dico.items()
dict_items([(0, 't'), (1, 'o'), (2, 't'), (3, 'o')])
```

On ne peut pas retrouver un élément par son indice dans un objet `dict_items`, toutefois on peut itérer dessus :

```python
>>> dico.items()[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> for key, val in dico.items():
...    print(key, val)
...
0 t
1 o
2 t
3 o
```

Notez la syntaxe particulière qui ressemble à la fonction `enumerate()` vue au chapitre 5 *Boucles et comparaisons*. On itère à la fois sur `key` et sur `val`. Nous aurons l'explication de ce mécanisme dans la rubrique sur les tuples ci-dessous.


### Existence d'une clé ou d'une valeur

Pour vérifier si une clé existe dans un dictionnaire, on peut utiliser le test d’appartenance avec l'opérateur `in` qui renvoie un booléen :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> "poids" in ani2
True
>>> if "poids" in ani2:
...     print("La clé 'poids' existe pour ani2")
...
La clé 'poids' existe pour ani2
>>> "age" in ani2
False
>>> if "age" in ani2:
...     print("La clé 'age' existe pour ani2")
...
```

Dans le second test (lignes 10 à 12), le message n'est pas affiché car la clé `age` n'est pas présente dans le dictionnaire `ani2`.

Si on souhaite tester si une valeur existe dans un dictionnaire, on peut utiliser l'opérateur `in` avec l'objet renvoyé par la méthode `.values()` :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> ani2.values()
dict_values(['singe', 70, 1.75])
>>> "singe" in ani2.values()
True
```

### Méthode `.get()`

Par défaut, si on demande la valeur associée à une clé qui n'existe pas, Python renvoie une erreur :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> ani2["age"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```

La méthode `.get()` s'affranchit de ce problème. Elle extrait la valeur associée à une clé mais ne renvoie pas d'erreur si la clé n'existe pas :

```python
>>> ani2.get("nom")
'singe'
>>> ani2.get("age")
>>> 
```

Ici la valeur associée à la clé `nom` est `singe` mais la clé `age` n'existe pas. 
On peut également indiquer à `.get()` une valeur par défaut si la clé n'existe pas :

```python
>>> ani2.get("age", 42)
42
```

### Liste de dictionnaires

En créant une liste de dictionnaires qui possèdent les mêmes clés, on obtient une structure qui ressemble à une base de données :

```python
>>> animaux = [ani1, ani2]
>>> animaux
[{'nom': 'girafe', 'poids': 1100, 'taille': 5.0}, {'nom': 'singe',
'poids': 70, 'taille': 1.75}]
>>>
>>> for ani in animaux:
...     print(ani["nom"])
...
girafe
singe
```

Vous constatez ainsi que les dictionnaires permettent de gérer des structures complexes de manière plus explicite que les listes.


## Tuples

### Définition

open-box-def

Les **tuples** (« n-uplets » en français) sont des **objets séquentiels** correspondant aux listes mais ils sont toutefois **non modifiables**. On dit aussi qu'ils sont **immuables**. Vous verrez ci-dessous que nous les avons déjà croisés à plusieurs reprises !

close-box-def

Pratiquement, on utilise les parenthèses au lieu des crochets pour les créer :

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t[2]
3
>>> t[0:2]
(1, 2)
>>> t[2] = 15
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

L'affectation et l'indiçage fonctionnent comme avec les listes. Mais si on essaie de modifier un des éléments du tuple (en ligne 10), Python renvoie un message d'erreur car les tuples sont non modifiables. Si vous voulez ajouter un élément (ou le modifier), vous devez créer un nouveau tuple :

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> t = t + (2,)
>>> t
(1, 2, 3, 2)
```

Cet exemple montre que les tuples sont peu adaptés lorsqu'on a besoin d'ajouter, retirer, modifier des éléments. La création d'un nouveau tuple à chaque étape s'avère lourde et il n'y a aucune méthode pour faire cela puisque les tuples sont non modifiables. Pour ce genre de tâche, les listes sont clairement mieux adaptées.

open-box-rem

Pour créer un tuple d'un seul élément comme ci-dessus, utilisez une syntaxe avec une virgule `(element,)`, pour éviter une ambiguïté avec une simple expression. Par exemple `(2)` équivaut à l'entier `2`, `(2,)` est un tuple avec l'élément `2`.

close-box-rem

Autre particularité des tuples, il est possible de les créer sans les parenthèses, dès lors que ceci ne pose pas d'ambiguïté avec une autre expression :

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> t = 1, 2, 3
>>> t
(1, 2, 3)
```

Toutefois, afin d'éviter les confusions, nous vous conseillons d'utiliser systématiquement les parenthèses lorsque vous débutez.

Les opérateurs `+` et `*` fonctionnent comme pour les listes (concaténation et duplication) :

```python
>>> (1, 2) + (3, 4)
(1, 2, 3, 4)
>>> (1, 2) * 4
(1, 2, 1, 2, 1, 2, 1, 2)
```

Enfin, on peut utiliser la fonction `tuple(sequence)` qui fonctionne exactement comme la fonction `list()`, c'est-à-dire qu'elle prend en argument un objet et renvoie le tuple correspondant (opération de *casting*) :

```python
>>> tuple([1,2,3])
(1, 2, 3)
>>> tuple("ATGCCGCGAT")
('A', 'T', 'G', 'C', 'C', 'G', 'C', 'G', 'A', 'T')
>>> tuple(range(5))
(0, 1, 2, 3, 4)
```

open-box-rem

Comme la fonction `list()`, la fonction `tuple()` prend en argument un objet séquentiel (un objet contenant une séquence d'autres objets). Elle ne fonctionne pas avec les entiers, *floats* ou booléens. Par exemple, `tuple(2)` renvoie une erreur.

close-box-rem


### Affectation multiple

Les tuples sont souvent utilisés pour l'**affectation multiple**, c'est-à-dire, affecter des valeurs à plusieurs variables en même temps :

```python
>>> x, y, z = 1, 2, 3
>>> x
1
>>> y
2
>>> z
3
```

Attention, le nombre de variables et de valeurs doit être cohérents à gauche et à droite de l'opérateur `=` :

```python
>>> x, y = 1, 2, 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

On pourra noter qu'il est possible de faire de l'affectation multiple avec les listes également : `[x, y, z] = [1, 2, 3]`. Toutefois, cette syntaxe est alourdie par la présence des crochets. On préfèrera donc la syntaxe avec les tuples sans parenthèses.

open-box-rem

Nous avons appelé l'opération `x, y, z = 1, 2, 3` affectation multiple pour signifier que l'on affectait des valeurs à plusieurs variables en même temps. Toutefois, vous pourrez rencontrer aussi l'expression *tuple unpacking* que l'on pourrait traduire par « désempaquetage de tuple ». De même, il existe le *list unpacking*.

close-box-rem

Ce terme *tuple unpacking* provient du fait que l'on peut décomposer un tuple initial de $n$ éléments en autant de variables différentes en une seule instruction. Si on crée un tuple de trois éléments :

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
```

On peut « désempaqueter » le tuple en une instruction :

```python
>>> x, y, z = t
```

Cela serait possible également avec l'indiçage, mais il faudrait utiliser autant d'instruction que d'éléments :

```python
>>> x = t[0]
>>> y = t[1]
>>> z = t[2]
```

Dans les 2 cas, `x` vaudra `1`, `y` vaudra `2` et  `z` vaudra `3`. 

open-box-adv

La syntaxe `x, y, z = t` pour désempaqueter un tuple est plus élégante, plus lisible et plus compacte. Elle sera donc à privilégier.

close-box-adv

L'affectation multiple est un mécanisme très puissant et important en Python. Nous verrons qu'il est particulièrement utile avec les fonctions dans les chapitres 10 *Fonctions* et 13 *Plus sur les fonctions*.

### Itérations sur plusieurs valeurs à la fois

Pratiquement, nous avons déjà croisé les tuples avec la fonction `enumerate()` dans le chapitre 5 *Boucles et comparaisons*. Cette dernière permettait d'itérer en même temps sur les indices et les éléments d'une liste :

```python
>>> for indice, element in enumerate([75, -75, 0]):
...     print(indice, element)
...
0 75
1 -75
2 0
>>> for bidule in enumerate([75, -75, 0]):
...     print(bidule, type(bidule))
...
(0, 75) <class 'tuple'>
(1, -75) <class 'tuple'>
(2, 0) <class 'tuple'>
```

Lignes 7 à 12. En fin de compte, la fonction `enumerate()` itère sur une série de tuples. Pouvoir séparer `indice` et `element` dans la boucle est possible du fait que Python autorise l'affectation multiple du style `indice, element = 0, 75` (voir rubrique précédente). 

Dans le même ordre d'idée, nous avons vu précédemment la méthode `.dict_items()` qui permettait d'itérer sur des couples clé / valeur d'un dictionnaire :

```python
>>> dico = {"pinson": 2, "merle": 3}
>>> for cle, valeur in dico.items():
...     print(cle, valeur)
...
pinson 2
merle 3
>>> for bidule in dico.items():
...     print(bidule, type(bidule))
...
('pinson', 2) <class 'tuple'>
('merle', 3) <class 'tuple'>
```

La méthode `.dict_items()` itère comme `enumerate()` sur une série de tuples.

Ainsi, on peut itérer sur 3 valeurs en même temps à partir d'une liste de tuples de 3 éléments :

```python
>>> liste = [(5, 6, 7), (6, 7, 8), (7, 8, 9)]
>>> for x, y, z in liste:
...     print(x, y, z)
...
5 6 7
6 7 8
7 8 9
```

On pourrait concevoir la même chose sur 4 ou 5 éléments, voire plus. La seule contrainte est d'avoir une correspondance systématique entre le nombre de variables d'itération (par exemple 3 variables dans l'exemple ci-dessus avec `x, y, z`) et la longueur de chaque sous-*tuple* de la liste sur laquelle on itère (chaque sous-*tuple* a 3 éléments ci-dessus).

### Remarque finale

Les listes, dictionnaires, tuples et chaînes de caractères sont tous des objets contenant une collection d'autres objets. En Python, on peut construire des listes qui contiennent des dictionnaires, des tuples ou d'autres listes, mais aussi des dictionnaires contenant des tuples, des listes, etc. Les combinaisons sont infinies !

## Exercices

*Conseil* : pour ces exercices, créez des scripts puis exécutez-les dans un *shell*.

### Prédire la sortie

Soit les 2 lignes de code suivantes: 

```python
dico = {"nom": "Joe", "age": 24, "taille": 181}
var="nom"
```

Prédisez le comportement de chaque instruction ci-dessous, sans les recopier dans un script ni dans l'interpréteur Python :

Que renvoie les instructions suivants ?

- `print(dico["age"])`
- `print(dico[var])`
- `print(dico[24])`
- `print(dico["var"])`
- `print(dico["taille"])`

Quelles sont celles qui donnent une erreur et pourquoi ?

### Moyennes des notes

Soit le dictionnaire suivant donnant les notes d'un étudiant :

```python
dico_notes = {"math": 14, "programmation": 12, "anglais": 16, "biologie": 10, "sport": 19}
```

Calculez la moyenne de ses notes de deux manières différentes. Calculez à nouveau la moyenne sans la note de biologie.

### Composition en acides aminés

En utilisant un dictionnaire, déterminez le nombre d’occurrences de chaque acide aminé dans la séquence `AGWPSGGASAGLAILWGASAIMPGALW`. Le dictionnaire ne doit contenir que les acides aminés présents dans la séquence. Interdit d'utiliser autant d'instructions `if` que d'acides aminés différents. Pensez au test d'appartenance !

