# Dictionnaires et tuples

## Dictionnaires

### Définition

Les **dictionnaires** se révèlent très pratiques lorsque vous devez manipuler des structures complexes à décrire et que les listes présentent leurs limites. Les dictionnaires sont des collections non ordonnées d'objets (ceci est vrai jusqu'à la version 3.6 de Python, voir remarque ci-dessous). Il ne s'agit pas d'objets séquentiels comme les listes ou chaînes de caractères, mais plutôt d'objets dits de correspondance (*mapping objects* en anglais) ou tableaux associatifs. En effet, on accède aux **valeurs** d'un dictionnaire par des **clés**. Ceci semble un peu confus ? Regardez l'exemple suivant :

```python
>>> ani1 = {}
>>> ani1["nom"] = "girafe"
>>> ani1["taille"] = 5.0
>>> ani1["poids"] = 1100
>>> ani1
{'nom': 'girafe', 'taille': 5.0, 'poids': 1100}
```

En premier, on définit un dictionnaire vide avec les accolades `{}` (tout comme on peut le faire pour les listes avec `[]`). Ensuite, on remplit le dictionnaire avec différentes clés (`"nom"`, `"taille"`, `"poids"`) auxquelles on affecte des valeurs (`"girafe"`, `5.0`, `1100`). Vous pouvez mettre autant de clés que vous voulez dans un dictionnaire (tout comme vous pouvez ajouter autant d'éléments que vous voulez dans une liste).

open-box-rem

Jusqu'à la version 3.6 de Python, un dictionnaire était affiché sans ordre particulier. L'ordre d'affichage des éléments n'était pas forcément le même que celui dans lequel il avait été rempli. De même lorsqu'on itérait dessus, l'ordre n'était pas garanti. Depuis Python 3.7 (inclus), ce comportement a changé, un dictionnaire est toujours affiché dans le même ordre que celui utilisé pour le remplir. De même, si on itère sur un dictionnaire, cet ordre est respecté. Ce détail provient de l'implémentation interne des dictionnaires dans Python, mais cela nous concerne peu. Ce qui importe, c'est de se rappeler qu'on accède aux éléments par des clés, donc cet ordre n'a pas d'importance spéciale sauf dans de rares cas.

close-box-rem

On peut aussi initialiser toutes les clés et les valeurs d'un dictionnaire en une seule opération :

```python
>>> ani2 = {"nom": "singe", "poids": 70, "taille": 1.75}

```
Mais rien ne nous empêche d'ajouter une clé et une valeur supplémentaire :

```python
>>> ani2["age"] = 15
```

Pour récupérer la valeur associée à une clé donnée, il suffit d'utiliser la syntaxe suivante `dictionnaire["cle"]`. Par exemple :

```python
>>> ani1["taille"]
5.0
```
Après ce premier tour d'horizon, on voit tout de suite l'avantage des dictionnaires. Pouvoir retrouver des éléments par des noms (clés) plutôt que par des indices. Les humains retiennent mieux les noms que les chiffres. Ainsi, l'usage des dictionnaires rend en général le code plus lisible. Par exemple, si nous souhaitions stocker les coordonnées $(x, y, z)$ d'un point dans l'espace : `coors = [0, 1, 2]` pour la version liste, `coors = {"x": 0, "y": 1, "z": 2}` pour la version dictionnaire. Un lecteur comprendra tout de suite que `coors["z"]` contient la coordonnée $z$, ce sera moins intuitif avec `coors[2]`.

### Objets utilisables comme clé

Toutes les clés de dictionnaire utilisées jusqu'à présent étaient des chaînes de caractères. On peut utiliser d'autres types d'objets comme des entiers, des *floats*, voire même des *tuples* (cf. rubrique suivante), cela peut s'avérer parfois très utile. Une règle est toutefois requise, les objets utilisés comme clé doivent être **hachables** (cf. rubrique précédente pour la définition).

Pourquoi les clés doivent être des objets hachables ? C'est la raison d'être des dictionnaires, d'ailleurs ils sont aussi appelés [table de hachage](https://fr.wikipedia.org/wiki/Table_de_hachage) dans d'autres langages comme Perl. Convertir chaque clé en sa valeur de hachage permet un accès très rapide à chacun des éléments du dictionnaire ainsi que des comparaisons de clés entre dictionnaires extrêmement efficaces. Même si on a vu que deux objets pouvaient avoir la même valeur de hachage, par exemple `a = 5` et `b = 5`, on ne peut mettre qu'une seule fois la clé `5`. Ceci assure que deux clés d'un même dictionnaire ont forcément une valeur de hachage différente.

open-box-adv

Malgré les possibilités offertes, nous vous conseillons de n'utiliser que des chaînes de caractères pour vos clés de dictionnaire lorsque vous débutez.

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

### Méthodes `.keys()`, `.values()` et `.items()`

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

Toutefois, ce sont des objets itérables, donc utilisables dans une boucle.

*Conseil* : pour les débutants, vous pouvez sauter cette fin de rubrique.

Enfin, il existe la méthode `.items()` qui renvoie un nouvel objet `dict_items` :

```python
>>> dico = {0: "t", 1: "o", 2: "t", 3: "o"}
>>> dico.items()
dict_items([(0, 't'), (1, 'o'), (2, 't'), (3, 'o')])
```

Celui-ci n'est pas indexable (on ne peut pas retrouver un élément par un indice) mais il est itérable :

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

Notez la syntaxe particulière qui ressemble à la fonction `enumerate()` vue au chapitre 5 *Boucles et comparaisons*. On itère à la fois sur `key` et sur `val`. On verra plus bas que cela peut-être utile pour construire des dictionnaires de compréhension.


### Existence d'une clé ou d'une valeur

Pour vérifier si une clé existe dans un dictionnaire, on peut utiliser le test d’appartenance avec l'opérateur `in` qui renvoie un booléen :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> if "poids" in ani2:
...     print("La clé 'poids' existe pour ani2")
...
La clé 'poids' existe pour ani2
>>> if "age" in ani2:
...     print("La clé 'age' existe pour ani2")
...
```

Dans le second test (lignes 5 à 7), le message n'est pas affiché car la clé `age` n'est pas présente dans le dictionnaire `ani2`.

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

### Tri par clés

On peut utiliser la fonction `sorted()` vue précédemment avec les listes pour trier un dictionnaire par ses clés :

```python
>>> ani2 = {'nom': 'singe', 'taille': 1.75, 'poids': 70}
>>> sorted(ani2)
['nom', 'poids', 'taille']
```

Les clés sont triées ici par ordre alphabétique.

### Tri par valeurs

Pour trier un dictionnaire par ses valeurs, il faut utiliser la fonction `sorted` avec l'argument `key` :

```python
>>> dico = {"a": 15, "b": 5, "c":20}
>>> sorted(dico, key=dico.get)
['b', 'a', 'c']
```

L'argument `key=dico.get` indique explicitement qu'il faut réaliser le tri par les valeurs du dictionnaire. On retrouve la méthode `.get()` vue plus haut, mais sans les parenthèses : `key=dico.get` mais pas `key=dico.get()`. Une fonction ou méthode passée en argument sans les parenthèses est appelée  *callback*, nous reverrons cela en détail dans le chapitre 20 *Fenêtres graphiques et Tkinter*.

Attention, ce sont les clés du dictionnaires qui sont renvoyées, pas les valeurs. Ces clés sont cependant renvoyées dans un ordre qui permet d'obtenir les clés triées par ordre croissant :

```python
>>> dico = {"a": 15, "b": 5, "c":20}
>>> for key in sorted(dico, key=dico.get):
...     print(key, dico[key])
... 
b 5
a 15
c 20
```

Enfin, l'argument `reverse=True` fonctionne également :

```python
>>> dico = {"a": 15, "b": 5, "c":20}
>>> sorted(dico, key=dico.get, reverse=True)
['c', 'a', 'b']
```

open-box-rem

Lorsqu'on trie un dictionnaire par ses valeurs, il faut être sûr que cela soit possible. Ce n'est, par exemple, pas le cas pour le dictionnaire `ani2` car les valeurs sont des valeurs numériques et une chaîne de caractères :

```python
>>> ani2 = {'nom': 'singe', 'poids': 70, 'taille': 1.75}
>>> sorted(ani2, key=ani2.get)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
```

On obtient ici une erreur car Python ne sait pas comparer une chaîne de caractères (`singe`) avec des valeurs numériques (`70` et `1.75`).

close-box-rem


### Clé associée au minimum ou au maximum des valeurs

Les fonctions `min()` et `max()`, que vous avez déjà manipulées dans les chapitres précédents, acceptent également l'argument `key=`. On peut ainsi obtenir la clé associée au minimum ou au maximum des valeurs d'un dictionnaire :

```python
>>> dico = {"a": 15, "b": 5, "c":20}
>>> max(dico, key=dico.get)
'c'
>>> min(dico, key=dico.get)
'b'
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

### Fonction `dict()`

*Conseil* : Pour les débutants vous pouvez sauter cette rubrique.

La fonction `dict()` va convertir l'argument qui lui est passé en dictionnaire. Il s'agit donc d'une fonction de *casting* comme `int()`, `str()`, etc. Toutefois, l'argument qui lui est passé doit avoir une forme particulière : un objet séquentiel contenant d'autres objets séquentiels de 2 éléments. Par exemple, une liste de listes de 2 éléments :

```python
>>> liste_animaux = [["girafe", 2], ["singe", 3]]
>>> dict(liste_animaux)
{'girafe': 2, 'singe': 3}
```

Ou un *tuple* de *tuples* de 2 éléments (cf. rubrique suivante pour la définition d'un *tuple*), ou encore une combinaison liste / *tuple* :

```python
>>> tuple_animaux = (("girafe", 2), ("singe", 3))
>>> dict(tuple_animaux)
{'girafe': 2, 'singe': 3}
>>>
>>> dict([("girafe", 2), ("singe", 3)])
{'girafe': 2, 'singe': 3}
```

Si un des sous-éléments a plus de 2 éléments (ou moins), Python renvoie une erreur :

```python
>>> dict([("girafe", 2), ("singe", 3, 4)])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #1 has length 3; 2 is required
```

## Tuples

### Définition

Les **tuples** (« n-uplets » en français) sont des objets séquentiels correspondant aux listes (itérables, ordonnés et indexables) mais ils sont toutefois **non modifiables**. On verra plus bas qu'ils sont hachables sous certaines conditions. L'intérêt des tuples par rapport aux listes réside dans leur immutabilité. Cela, accèlère considérablement la manière dont Python accède à chaque élément et ils prennent moins de place en mémoire. Par ailleurs, on ne risque pas de modifier un de ses éléments par mégarde. Vous verrez ci-dessous que nous les avons déjà croisés à plusieurs reprises !

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

L'affectation et l'indiçage fonctionnent comme avec les listes. Mais si on essaie de modifier un des éléments du tuple (en ligne 10), Python renvoie un message d'erreur. Ce message est similaire à celui que nous avions rencontré quand on essayait de modifier une chaîne de caractères (cf. chapitre 10). De manière générale, Python renverra un message `TypeError: '[...]' does not support item assignment` lorsqu'on essaie de modifier un élément d'un objet non modifiable.   Si vous voulez ajouter un élément (ou le modifier), vous devez créer un nouveau tuple :

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> id(t)
139971081704464
>>> t = t + (2,)
>>> t
(1, 2, 3, 2)
>>> id(t)
139971081700368
```

La fonction `id()` montre que le tuple créé en ligne 6 est bien différent de celui créé en ligne 4 bien qu'ils aient le même nom. Comme on a vu plus haut, ceci est dû à l'opérateur d'affectation utilisé en ligne 6 (`t = t + (2,)`) qui crée un nouvel objet distinct de celui de la ligne 1. Cet exemple montre que les tuples sont peu adaptés lorsqu'on a besoin d'ajouter, retirer, modifier des éléments. La création d'un nouveau tuple à chaque étape s'avère lourde et il n'y a aucune méthode pour faire cela puisque les tuples sont non modifiables. Pour ce genre de tâche, les listes sont clairement mieux adaptées.

open-box-rem

Pour créer un tuple d'un seul élément comme ci-dessus, utilisez une syntaxe avec une virgule `(element,)`, pour éviter une ambiguïté avec une simple expression. Par exemple `(2)` équivaut à l'entier `2`, `(2,)` est un tuple avec l'élément `2`.

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

close-box-rem

Les opérateurs `+` et `*` fonctionnent comme pour les listes (concaténation et duplication) :

```python
>>> (1, 2) + (3, 4)
(1, 2, 3, 4)
>>> (1, 2) * 4
(1, 2, 1, 2, 1, 2, 1, 2)
```

Enfin, on peut utiliser la fonction `tuple(sequence)` qui fonctionne exactement comme la fonction `list()`, c'est-à-dire qu'elle prend en argument un objet de type container et renvoie le tuple correspondant (opération de *casting*) :

```python
>>> tuple([1,2,3])
(1, 2, 3)
>>> tuple("ATGCCGCGAT")
('A', 'T', 'G', 'C', 'C', 'G', 'C', 'G', 'A', 'T')
```

open-box-rem

Les listes, les dictionnaires et les tuples sont des containers, c'est-à-dire qu'il s'agit d'objets qui contiennent une collection d'autres objets. En Python, on peut construire des listes qui contiennent des dictionnaires, des tuples ou d'autres listes, mais aussi des dictionnaires contenant des tuples, des listes, etc. Les combinaisons sont infinies !

close-box-rem

### Itérations sur plusieurs valeurs à la fois

Pratiquement, nous avons déjà croisé les tuples avec la fonction `enumerate()` dans le chapitre 5 *Boucles et comparaisons*. Cette dernière permettait d'itérer **en même temps** sur les indices et les éléments d'une liste :

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

En fin de compte, la fonction `enumerate()` itère sur une série de *tuples*. Pouvoir séparer `indice` et `element` dans la boucle est possible du fait que Python autorise l'affectation multiple du style `indice, element = 0, 75` (voir rubrique suivante). 

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

De la même façon, on peut itérer sur 3 valeurs en même temps à partir d'une liste de tuples de 3 éléments :

```python
>>> liste = [(5, 6, 7), (6, 7, 8), (7, 8, 9)]
>>> for x, y, z in liste:
...     print(x, y, z)
...
5 6 7
6 7 8
7 8 9
```

On pourrait concevoir la même chose sur 4, 5... éléments. La seule contrainte est d'avoir une correspondance systématique entre le nombre de variables d'itération (par exemple 3 variables dans l'exemple ci-dessus avec `x, y, z`) et la longueur de chaque sous-*tuple* de la liste sur laquelle on itère (chaque sous-*tuple* a 3 éléments ci-dessus).
