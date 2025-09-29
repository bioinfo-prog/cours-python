# Remarques complémentaires

Dans ce chapitre, nous présentons un certain nombre de points en vrac qui ne rentraient pas forcément dans les autres chapitres ou qui étaient trop avancés au moment où les chapitres étaient abordés. Outre quelques points mineurs, nous abordons les grandes différences entre Python 2 et Python 3, les anciennes méthodes de formatage des chaînes de caractères, les fonctions lambda, les itérateurs, la gestion des exceptions, les passage d'arguments avancés dans les fonctions et les décorateurs. Certains de ces points sont réellement avancés et nécessiteront d'avoir assimilé d'autres notions avant de les aborder.

## Différences Python 2 et Python 3

Python 3 est la version de Python qu'il faut utiliser.

Néanmoins, Python 2 a été employé pendant de nombreuses années par la communauté scientifique et vous serez certainement confrontés à un programme écrit en Python 2. Voici quelques éléments pour vous en sortir :

### Le mot-clé `print` / la fonction `print()`

En Python 2 `print` est un mot-clé du langage (en anglais *statement*) au même titre que `for`, `if`, `def`, etc. Il s'utilise ainsi sans parenthèse. Par exemple :

```python
>>> print 12
12
>>> print "girafe"
girafe
```

Par contre, en Python 3, `print()` est une fonction. Ainsi, si vous n'utilisez pas de parenthèse, Python vous renverra une erreur :

```python
>>> print 12
  File "<stdin>", line 1
    print 12
           ^
SyntaxError: Missing parentheses in call to 'print'
```

### Division d'entiers

En Python 3, la division de deux entiers, se fait *naturellement*, c'est-à-dire que l'opérateur `/` renvoie systématiquement un *float*. Par exemple :

```python
>>> 3 / 4
0.75
```
Il est également possible de réaliser une division entière avec l'opérateur `//` :
```
>>> 3 // 4
0
```

La division entière renvoie finalement la partie entière du nombre `0.75`, c'est-à-dire `0`.

Attention ! En Python 2, la division de deux entiers avec l'opérateur `/` correspond à la division entière, c'est-à-dire le résultat arrondi à l'entier inférieur. Par exemple :

```python
>>> 3 / 5
0
>>> 4 / 3
1
```

Faites très attention à cet aspect si vous programmez encore en Python 2, c'est une source d'erreur récurrente.


### La fonction `range()`

En Python 3, la fonction `range()` renvoie un objet de type *range* (voir les chapitres 5 *Boucles et comparaisons* et 14 *Conteneurs*) :

```python
>>> range(3)
range(0, 3)
```

Comme on a vu au chapitre 5 *Boucles et comparaisons*, ces objets sont itérables produisant successivement les nombres `0`, puis `1` puis `2` sur notre exemple :

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

En Python 2, la fonction `range()` renvoie une liste. Par exemple :

```python
>>> range(3)
[0, 1, 2]
>>> range(2, 6)
[2, 3, 4, 5]
```

La création de liste avec `range()` était pratique, mais très peu efficace en mémoire lorsque l'argument donné à `range()` était un grand nombre.

D'ailleurs la fonction `xrange()` est disponible en Python 2 pour faire la même chose que la fonction `range()` en Python 3. Attention, ne vous mélangez pas les pinceaux !

```python
>>> range(3)
[0, 1, 2]
>>> xrange(3)
xrange(3)
```

open-box-rem

Pour générer une liste d'entiers avec la fonction `range()` en Python 3, vous avez vu dans le chapitre 4 *Listes* qu'il suffisait de l'associer avec la fonction `list()`. Par exemple :

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

close-box-rem

open-box-adv

Pour une comparaison exhaustive entre `xrange()` en Python 2 et `range()` en Python 3, vous pouvez lire ce très bon [article](https://treyhunner.com/2018/02/python-3-s-range-better-than-python-2-s-xrange/) tiré du blog de Trey Hunner.

close-box-adv

### Fonction `zip()`

En Python 2, la fonction `zip()` renvoie une liste de tuples, alors qu'en Python 3 elle renvoie un **itérateur** :

```python
>>> # Python2.
>>> zip(range(4), range(10, 14))
[(0, 10), (1, 11), (2, 12), (3, 13)]
```

```python
>>> # Python3.
>>> zip(range(4), range(10, 14))
<zip object at 0x7f11423ffd80>
```

Vous pouvez lire la rubrique *Itérables, itérateurs, générateurs et module itertools* un peu plus bas dans ce chapitre pour en savoir plus sur les itérateurs.

### Encodage et utf-8

En Python 3, vous pouvez utiliser des caractères accentués dans les commentaires ou dans les chaînes de caractères.

Ce n'est pas le cas en Python 2. Si un caractère accentué est présent dans votre code, cela occasionnera une erreur de ce type lors de l'exécution de votre script :

```text
SyntaxError: Non-ASCII character '\xc2' in file xxx on line yyy, but no encoding
declared; see http://python.org/dev/peps/pep-0263/ for details
```

Pour éviter ce genre de désagrément, ajoutez la ligne suivante en tout début de votre script :

```python
# coding: utf-8
```

Si vous utilisez un shebang (voir rubrique précédente), il faudra mettre la ligne `# coding: utf-8` sur la deuxième ligne ([la position est importante](http://www.python.org/dev/peps/pep-0263/)) de votre script :

```python
#! /usr/bin/env python
# coding: utf-8
```

open-box-rem

L'encodage utf-8 peut aussi être déclaré de cette manière :

```python
# -*- coding: utf-8 -*-
```

mais c'est un peu plus long à écrire.

close-box-rem


## Anciennes méthodes de formatage des chaînes de caractères

Dans les premières versions de Python jusqu'à la 2.6, il fallait utiliser l'opérateur `%`, puis de la version 2.7 jusqu'à la 3.5 il était plutôt conseillé d'utiliser la méthode `.format()`. Même si les *f-strings* sont devenues la manière conseillée pour mettre en place l'écriture formatée, ces deux anciennes manières, sont encore pleinement compatibles avec les versions modernes de Python.

Même si elle fonctionne encore, la première manière avec l'opérateur `%` est maintenant clairement déconseillée pour un certain nombre de [raisons](https://docs.python.org/fr/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting). Néanmoins, nous rappelons ci-dessous son fonctionnement, car il se peut que vous tombiez dessus dans d'anciens livres ou si vous lisez de vieux programmes Python.

La deuxième manière avec la méthode `.format()` est encore utilisée et reste tout à fait valide. Elle est clairement plus puissante et évite un certain nombre de désagréments par rapport à l'opérateur `%`. Vous la croiserez sans doute de temps en temps dans des programmes et ouvrages plus ou moins récents. Heureusement elle a un fonctionnement relativement proche des *f-strings*, donc vous ne serez pas totalement perdus !

Enfin, nous indiquons à la fin de cette rubrique nos conseils sur quelle méthode utiliser.

### L'opérateur `%`

On a vu avec les entiers que l'opérateur `%` ou *modulo* renvoyait le reste d'une division entière. Cet opérateur existe aussi pour les chaînes de caractères mais il met en place l'écriture formatée. En voici un exemple :

```python
>>> x = 32
>>> nom = "John"
>>> print("%s a %d ans" % (nom, x))
John a 32 ans
>>> nb_G = 4500
>>> nb_C = 2575
>>> prop_GC = (nb_G + nb_C)/14800
>>> print("On a %d G et %d C -> prop GC = %.2f" % (nb_G, nb_C, prop_GC))
On a 4500 G et 2575 C -> prop GC = 0.48
```

La syntaxe est légèrement différente. Le symbole `%` est d'abord appelé dans la chaîne de caractères (dans l'exemple ci-dessus `%d`, `%d` et `%.2f`) pour :

- Désigner l'endroit où sera placée la variable dans la chaîne de caractères.
- Préciser le type de variable à formater, `d` pour un entier (`i` fonctionne également) ou `f` pour un *float*.
- Éventuellement pour indiquer le format voulu. Ici `.2` signifie une précision de deux décimales.

Le signe `%` est rappelé une seconde fois (`% (nb_G, nb_C, prop_GC)`) pour indiquer les variables à formater.

### La méthode `.format()`

Depuis la version 2.7 de Python, la méthode `.format()` a apporté une nette amélioration pour mettre en place l'écriture formatée. Celle-ci fonctionne de la manière suivante :

```python
>>> x = 32
>>> nom = "John"
>>> print("{} a {} ans".format(nom, x))
John a 32 ans
>>> nb_G = 4500
>>> nb_C = 2575
>>> prop_GC = (nb_G + nb_C)/14800
>>> print("On a {} G et {} C -> prop GC = {:.2f}".format(nb_G, nb_C, prop_GC))
On a 4500 G et 2575 C -> prop GC = 0.48
```

- Dans la chaîne de caractères, les accolades vides `{}` précisent l'endroit où le contenu de la variable doit être inséré.
- Juste après la chaîne de caractères, l'instruction `.format(nom, x)` fournit la liste des variables à insérer, d'abord la variable `nom` puis la variable `x`. 
- On peut éventuellement préciser le formatage en mettant un caractère deux-points `:` puis par exemple ici `.2f` qui signifie deux chiffres après la virgule.
- La méthode `.format()` agit sur la chaîne de caractères à laquelle elle est attachée par le point.

Tout ce que nous avons vu avec les *f-strings* sur la manière de formater l'affichage d'une variable (après les `:` au sein des accolades) est identique avec la méthode `.format()`. Par exemple `{:.2f}`, `{:0>6d}`, `{:.6e}`, etc., fonctionneront de la même manière. La différence notable est qu'on ne met pas directement le nom de la variable au sein des accolades. Comme pour l'opérateur `%`, c'est l'emplacement dans les arguments passés à la méthode `.format()` qui dicte quelle variable doit être remplacée. Par exemple, dans `"{} {} {}".format(bidule, machin, truc)`, les premières accolades remplaceront la variable `bidule`, les deuxièmes la variable `machin`, les troisièmes la variable `truc`.

Le formatage avec la méthode `.format()` se rapproche de la syntaxe des *f-strings* (accolades, deux-points), mais présente l'inconvénient -- comme avec l'opérateur `%` -- de devoir mettre la liste des variables tout à la fin, alourdissant ainsi la syntaxe. En effet, dans l'exemple avec la proportion de GC, la ligne équivalente avec une *f-string* apparait tout de même plus simple à lire :

```python
>>> print(f"On a {nb_G} G et {nb_C} C -> prop GC = {prop_GC:.2f}")
On a 4500 G et 2575 C -> prop GC = 0.48
```

open-box-adv

Pour conclure, ces deux anciennes façons de formater une chaîne de caractères avec l'opérateur `%` ou la méthode `.format()` vous sont présentées à titre d'information. La première avec l'opérateur `%` est clairement déconseillée. La deuxième avec la méthode `.format()` est encore tout à fait valable. Si vous débutez Python, nous vous conseillons fortement d'apprendre et d'utiliser les *f-strings*. C'est ce que vous rencontrerez dans la suite de ce cours. Si vous connaissez déjà Python et que vous utilisez la méthode `.format()`, nous vous conseillons de passer aux *f-strings*. Depuis que nous les avons découvertes, aucun retour n'est envisageable pour nous tant elles sont puissantes et plus claires à utiliser ! 

close-box-adv

open-box-more

Enfin, si vous souhaitez aller plus loin, voici deux articles (en anglais) très bien faits sur le site *RealPython* : sur l'[écriture formatée](https://realpython.com/python-string-formatting) et sur les [*f-strings*](https://realpython.com/python-f-strings/)

close-box-more

## Fonctions lambda

### Définition 

open-box-def

Une **fonction lambda** est une fonction qui s'écrit sur une ligne. En Python, il s'agit du moyen d'implémenter une [fonction anonyme](https://en.m.wikipedia.org/wiki/Anonymous_function) (en anglais *anonymous function*), c'est-à-dire, une fonction qui est la plupart du temps non reliée à un nom (d'où le terme anonyme). Une fonction lambda s'utilise en général à la volée. On parle aussi d'expressions lambda utilisées pour fabriquer des fonctions lambda. 

close-box-def

Voici un premier exemple :

```python
>>> lambda x: x**2
<function <lambda> at 0x7fcbd9c58b80>
>>> (lambda x: x**2)(4)
16
>>> (lambda x: x**2)(10)
100
```

- **Ligne 1.** On a ici une expression lambda typique définissant une fonction lambda. La syntaxe est (dans l'ordre) : le mot-clé (*statement*) lambda, zero ou un ou plusieurs argument(s), deux-points, une expression utilisant ou pas les arguments. 
- **Ligne 2.** Python confirme qu'il s'agit d'une fonction.
- **Lignes 3 à 6.** Pour utiliser la fonction lambda, pour l'instant, on la met entre parenthèses et on utilise un autre jeu de parenthèses pour l'appeler et éventuellement passer des arguments.

open-box-warn

Une fonction lambda ne s'écrit que sur une ligne. Si vous essayez de l'écrire sur plusieurs lignes, Python lèvera une exception  `SyntaxError: invalid syntax`.

close-box-warn

Comme pour les fonctions classiques, le nombre d'arguments est variable et doit être cohérent avec l'appel :

```python
>>> (lambda: 1/2)()
0.5
>>> (lambda x, y: x + y)(1, 2)
3
>>> (lambda x, y: x + y)(4, 5)
9
>>> (lambda: 1/2)(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes 0 positional arguments but 1 was given
>>> (lambda x, y: x + y)(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() missing 1 required positional argument: 'y'
```

- **Ligne 1.** Fonction lambda à zéro argument.
- **Lignes 3 et 5.** Fonction lambda à deux arguments.
- **Lignes 7 à 10.** Le nombre d'argument(s) est incorrect et génère une erreur. Dans cet exemple, on passe un argument alors que la fonction lambda créée ici n'en prend pas.
- **Lignes 11 à 14.** Le nombre d'argument(s) est incorrect et génère une erreur. Dans cet exemple, on passe un argument alors que la fonction lambda créée ici en prend deux.

### Assignation d'une fonction lambda à un nom ?

Bien que cela soit déconseillé, il est possible d'assigner une fonction lambda à un nom de variable :

```python
>>> carre = lambda x: x**2
>>> carre(3)
9
```

L'équivalent avec une fonction classique serait :

```python
>>> def carre(x):
...     return x**2
...
>>> carre(9)
81
```

Dans les deux cas l'appel est identique, mais la fonction lambda requière une syntaxe à une ligne lors de sa définition.

Même si on peut le faire, les dévelopeurs déconseillent toutefois d'assigner une fonction lambda à un nom dans la [PEP8](https://peps.python.org/pep-0008/). Une des raisons est que si une erreur est générée, l'interpréteur ne renvoie pas le numéro de ligne dans la *Traceback* :

```python
>>> inverse = lambda: 1/0
>>> inverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
ZeroDivisionError: division by zero
```

**Ligne 5.** L'indication de la ligne pour l'erreur dans la fonction lambda  (*line 1*) correspond à celle de l'appel et non pas de la définition. 

Alors qu'avec une fonction classique :

```
>>> def inverse():
...     return 1/0
...
>>> inverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in inverse
ZeroDivisionError: division by zero
```

**Ligne 5**. Cette fois-ci, la *Traceback* indique bien la bonne ligne (*line 2*) dans la fonction.

open-box-adv

Pour cette raison, n'assignez pas une fonction lambda à un nom, mais utilisez la seulement à la volée (voir ci-dessous). Une autre raison est que cela peut nuire à la lisibilité. Si une fonction lambda s'écrit en une ligne, c'est bien pour qu'on puisse la lire quand elle est utilisée.

close-box-adv

### Utilité des fonctions lambda

Jusqu'à maintenant nous avons défini les fonctions lambda et montré ce qu'il ne fallait pas faire. Vous vous posez sans doute la question, mais à quoi servent-elles vraiment ? Nous vous montrons ici deux utilisations principales.

La première est qu'elles sont utiles pour implémenter des concepts de [programmation fonctionnelle](https://fr.wikipedia.org/wiki/Programmation_fonctionnelle). Dans ce paradigme de programmation, on cherchera à « emboiter » les fonctions les unes dans les autres. Nous avions déjà croisé cette idée avec la fonction `map()` dans le chapitre 11 *Plus sur les chaînes de caractères*. Celle-ci permet d'appliquer une fonction à tous les éléments d'un objet itérable. Par exemple, convertir en entier les différents éléments d'une chaîne de caractères :

```python
>>> ligne = "3 5   -10"
>>> list(map(int, ligne.split()))
[3, 5, -10]
```

**Ligne 2.** On a converti l'objet *map* en liste pour voir ce qu'il contenait.

L'utilisation impliquant une fonction lambda permet par exemple d'appliquer une opération à tous les éléments d'une liste :

```python
>>> liste1 = [3, 5, -10]
>>> list(map(lambda x: x**2, liste1))
[9, 25, 100]
>>> list(map(lambda x: 1/x, liste1))
[0.3333333333333333, 0.2, -0.1]
```

**Lignes 2 et 4.** La fonction lambda permet de lire clairement quelle opération on réalise plutôt que de se référer à une fonction classique se trouvant à un autre endroit. Ainsi, cela améliore la lisibilité.

Cela vous rappelle peut-être ce qu'on a rencontré avec les objets *NumPy* et les opérations vectorielles :

```python
>>> import numpy as np
>>> array1 = np.arange(10)
>>> array1
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> array1 * 2
array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
>>>
>>> liste1 = list(range(10))
>>> liste1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(map(lambda x: x*2, liste1))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**Ligne 5.** Nativement, l'opération `array1 * 2` se fait vectoriellement (élément par élément) avec un *array NumPy*.

**Ligne 11.** La fonction `map()` applique l'opération `* 2` de la lambda sur tous les éléments de la liste. Ainsi, on obtient le même effet que sur l'*array NumPy*.

Bien que cela s'avère pratique, nous verrons dans la rubrique suivante sur les itérateurs qu'il existe une syntaxe plus Pythonique avec les listes de compréhensions et les expressions génératrices. 

La deuxième grande utilité des fonctions lambda concerne leur utilisation pour faire des tris puissants. Dans le chapitre 14 *Conteneurs*, nous avions vu les tris de dictionnaires par valeurs :

```python
>>> dico = {"a": 15, "b": 5, "c":20}
>>> sorted(dico, key=dico.get)
['b', 'a', 'c']
```

**Ligne 2.** On passe à l'argument par mot-clé `key` la *callback* `dico.get` (cette méthode renvoie initialement les valeurs d'un dictionnaire). Cela permet finalement de trier par ce que renvoie cette méthode, à savoir les valeurs.

Cet argument par mot-clé peut prendre d'autres *callback*, par exemple `len`. Dans l'exemple suivant, on prend 10 mots au hasard dans le dictionnaire et on les trie par leur longueur :

```python
>>> mots = ['étudier', 'pie-grièche', 'figurerait', 'retraitait', 'allégerais', 
            'distribuent', 'affilierait', 'ramassa', 'galettes', 'connu']
>>> sorted(mots, key=len)
['connu', 'étudier', 'ramassa', 'galettes', 'figurerait', 'retraitait', 
'allégerais', 'pie-grièche', 'distribuent', 'affilierait']
```

Bien sûr, on peut utiliser aussi une fonction lambda. Celle-ci va nous permettre de passer une fonction de tri à la volée au moment de l'appel de la fonction `sorted()`. Par exemple, si on reprend le même exemple que le dictionnaire mais sous forme d'une liste de tuples :

```python
liste1 = [('a', 15), ('b', 5), ('c', 20)]
```

Comment trier en fonction du deuxième élément de chaque tuple ? Réponse, avec une fonction lambda bien sûr ! Regardez :

```python
>>> sorted(liste1, key=lambda x: x[1])
[('b', 5), ('a', 15), ('c', 20)]
```

Autre exemple, on souhaite trier une liste d'entiers aléatoires non pas par leur valeur, mais par le résultat de la fonction `x**2` :

```python
>>> liste1 = [-5, 2, 5, 8, 6, 3, -9, 4, -10, 2]
>>> sorted(liste1, key=lambda x: x**2)
[2, 2, 3, 4, -5, 5, 6, 8, -9, -10]
```

Pour comprendre comment le tri est opéré en **ligne 3**, voici la liste initiale et une autre liste avec les carrés :

```python
>>> liste1
[-5, 2, 5, 8, 6, 3, -9, 4, -10, 2]
>>> [x**2 for x in liste1]
[25, 4, 25, 64, 36, 9, 81, 16, 100, 4]
```

Le tri de `liste1` ci-dessus est bien effectué en fonction des valeurs montrées en **ligne 4**.

L'agument par mot-clé `key` existe dans d'autres fonctions ou méthodes. Bien sûr il existe dans la méthode `.sort()` qui trie les listes sur place. Mais aussi, dans les fonctions natives `min()` et `max()`. Enfin, on le croise dans la fonction `groupby()` du module itertools (voir rubrique suivante). Dans tous ces cas, on peut utiliser une fonction lambda pour l'argument `key`. 

Par exemple, dans le code suivant :

```python
>>> liste = ['baccalauréat', 'abaissera', 'barricadé', 'zouave', 'tabac', 
             'typographie', 'dactylographes', 'éclipse']
>>> min(liste)
'abaissera'
>>> max(liste)
'éclipse'
>>> min(liste, key=lambda x: x.count("a"))
'éclipse'
>>> max(liste, key=lambda x: x.count("a"))
'baccalauréat'
```

- **Ligne 1.** On prend une liste de mots du dictionnaire. 
- **Lignes 2 et 4**. Les fonctions `min()` et `max ()` considèrent l'ordre ASCII par défaut. Elles renvoient le premier et dernier élément de la liste après un tel tri.
- **Lignes 6 et 8**. Comprenez-vous la règle que nous avons utilisée avec la lambda ?

Regardons comment se passe le tri :

```python
>>> liste.sort(key=lambda x: x.count("a"))
>>> liste
['éclipse', 'zouave', 'typographie', 'barricadé', 'tabac', 'dactylographes', 
'abaissera', 'baccalauréat']
```

Vous l'aurez sans doute compris, avec notre fonction lambda, nous avons trié en fonction du nombre de lettres `a` dans chaque mot !

### Conclusion

Nous avons vu que les fonctions lambda permettaient des définitions de fonction rapidement sur une ligne. Il faut absolument éviter de les assigner à un nom. Elles ont toute leur utilité lorsqu'on les utilise avec `map()` pour appliquer une opération à tous les éléments d'un conteneur, ou pour des tris puissants avec `sorted()`.

open-box-more

Pour aller plus loin, vous pouvez consulter ces quelques articles : [Dataquest](https://www.dataquest.io/blog/tutorial-lambda-functions-in-python/), [Trey Hunner](https://www.pythonmorsels.com/lambda-expressions/), [RealPython](https://realpython.com/python-lambda/) et [Dan Bader](https://dbader.org/blog/python-lambda-functions).

close-box-more

## Itérables, itérateurs, générateurs et module itertools

### Itérables et itérateurs

Dans le chapitre 14 *Conteneurs*, nous avons défini le mot **itérable** lorsque nous avions un objet de type conteneur sur lequel on pouvait itérer (comme les listes, tuples, dictionnaires, etc.). En général, nous le faisions avec une boucle `for`. Voyons ce qu'est maintenant un itérateur.

open-box-def

Un **itérateur** est un objet Python qui permet d'itérer sur une suite de valeurs avec la fonction `next()` jusqu'à temps qu'elles soient épuisées. Si on itère sur une partie des valeurs seulement, l'itérateur garde en mémoire là où il s'est arrêté. Si on le resollicite avec un `next()` il repartira de l'élément suivant. Une règle est toutefois importante : les valeurs ne peuvent être parcourues qu'une seule fois.

close-box-def

On peut générer un itérateur avec la fonction `iter()` à partir de n'importe quel conteneur :

```python
>>> animaux = ["chien", "chat", "souris"]
>>> iterateur = iter(animaux)
>>> iterateur
<list_iterator object at 0x7f917e907a30>
```

Une fois l'itérateur généré, on peut accéder à l'élément suivant avec la fonction `next()` :

```python
>>> next(iterateur)
'chien'
>>> next(iterateur)
'chat'
>>> next(iterateur)
'souris'
>>> next(iterateur)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Quand il n'y a plus de valeurs sur lesquelles itérer, la fonction `next()` lève une exception `StopIteration`. En général, on n'utilisera pas les itérateurs de cette manière, mais plutôt avec une boucle `for` ce qui évitera cette levée d'exception :

```python
>>> iterateur = iter(animaux)
>>> for elt in iterateur:
...     print(elt)
...
chien
chat
souris
```

On peut transformer un objet de type itérateur en un objet de type séquentiel, par exemple en tuple :

```python
>>> iterateur = iter(animaux)
>>> tuple(iterateur)
('chien', 'chat', 'souris')
```

Le point important est qu'une fois toutes les valeurs parcourues, l'itérateur est épuisé et ne renvoie plus rien :

```python
>>> iterateur = iter(animaux)
>>> tuple(iterateur)
('chien', 'chat', 'souris')
>>> tuple(iterateur)
()
```

Ainsi, on ne pourra parcourir l'ensemble des valeurs d'un itérateur qu'une fois. 

À ce stade, on pourrait se dire que la construction d'un itérateur à partir d'une liste ci-dessus est inutile puisqu'on peut itérer directement sur la liste avec une boucle `for`. Toutefois, lorsqu'on réalise une telle boucle, il y a un itérateur qui est généré implicitement même si on ne s'en rend pas compte. Pour prouver cela, essayons la fonction `next()` avec une liste :

```python
>>> next(animaux)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
```

Ceci n'est pas possible car une liste n'est pas un itérateur. Alors pourquoi peut-on itérer dessus avec une boucle `for` ? Et bien, c'est parce que l'objet de type liste possède une méthode *dunder* spéciale nommée `.__iter__()`. Celle-ci génère un itérateur à partir d'elle-même permettant d'itérer sur ses éléments. L'objet itérateur ainsi généré possèdera une autre méthode *dunder* spéciale `.__next__()` permettant de passer à l'élément suivant lorsqu'on itère dessus. 

open-box-rem

Pour rappel, les méthodes *dunder* des classes ont été définies dans la rubrique 24.2.2 *Méthodes magiques ou dunder methods* du chapitre 24 *Avoir plus la classe avec les objets*.

close-box-rem

Lorsque vous construirez votre propre objet itérable, il faudra écrire une classe contenant ces deux méthodes *dunder* et l'objet sera *de facto* un itérateur et itérable. Pour vous donnez une première idée, voici une classe minimale créant un objet itérateur sur les lettres de l'alphabet :

```python
class Alphabet:
    def __init__(self):
        self.current = 97 # ASCII code for a.

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 122: # ASCII code for z.
            raise StopIteration
        letter = chr(self.current)
        self.current += 1
        return letter
```

- **Ligne 3**. Dans le constructeur, on crée un attribut d'instance `self.current` qui gardera l'état de l'itérateur. On l'initialise à 97 correspondant au code ASCII de la lettre `a`.
- **Lignes 5 et 6**. La méthode *dunder* `.__iter__()` est très simple à écrire. Elle renvoie `self` correspondant à l'itérateur lui-même. Si cette méthode n'est pas présente, l'objet n'est pas itérable.
- **Lignes 8 à 13**. La méthode *dunder* `.__next__()` s'occupe de passer à l'élément suivant et de garder une mémoire de là où l'itérateur est arrivé. Cela se passe en quatre étapes : i) levée d'une exception `StopIteration` si on est arrivé au bout, ii) détermination de la lettre actuelle, iii) incrémenter le `self.current` de 1 pour l'itération suivante et iv) retourner la lettre actuelle.

Si on sauve cette classe dans un fichier `iterator.py`, voici comment on pourrait l'utiliser :

```python
>>> import iterator
>>> iter_alphabet = iterator.Alphabet()
>>> iter_alphabet
<iterator.Alphabet object at 0x7f308edc70b0>
>>> for lettre in iter_alphabet:
...     print(lettre)
...
a
b
[...]
y
z
>>> list(iter_alphabet)
[]
```

À nouveau, une fois l'itérateur épuisé, il ne renvoie plus rien. Bien sûr, cela représente un exemple très simple et la plupart du temps on créera ses propres classes itérateurs en implémentant de nombreuses fonctionnalités et méthodes supplémentaires. Pour créer un itérateur basique comme celui-ci sur l'alphabet, il est plus commode d'utiliser les générateurs (voir rubrique *Générateurs* ci-dessous).

open-box-more

Pour aller plus loin sur comment fonctionne les itérateurs, vous pouvez lire ces articles de [Dan Bader](https://dbader.org/blog/python-iterators), [Trey Hunner](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/) et du [site *RealPython*](https://realpython.com/python-iterators-iterables/). Concernant la sémantique, cet [article](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/) de Trey Hunner explique pourquoi les objets *range* ne sont pas des itérateurs.

close-box-more

### Autres fonctions *builtins* renvoyant des itérateurs 

Dans les chapitres précédents, nous avons déjà croisé des itérateurs sans le savoir, car nous ne vous l'avons pas toujours précisé explicitement ! Dans le chapitre 5 *Boucles* avec la fonction `enumerate()`, dans le chapitre 11 *Plus sur les chaînes de caractères* avec la fonction `map()` et dans le chapitre 12 *Plus sur les listes* avec la fonction `zip()`. Ces trois fonctions renvoient des itérateurs qui sont épuisés une fois utilisés :

```python
>>> animaux = ["chien", "chat", "souris"]
>>> obj_enum = enumerate(animaux)
>>> obj_enum
<enumerate object at 0x7f917ebf93a0>
>>> tuple(obj_enum)
((0, 'chien'), (1, 'chat'), (2, 'souris'))
>>> tuple(obj_enum)
()
```

```python
>>> line = "9 11 25 92 49 98 62 72 63 74"
>>> obj_map = map(int, line.split())
>>> obj_map
<map object at 0x7f029e47b9a0>
>>> min(obj_map)
9
>>> list(obj_map)
[]
```

```python
>>> obj_zip = zip(range(5), range(5, 10))
>>> list(obj_zip)
[(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
>>> list(obj_zip)
[]
```

Lorsque ces fonctions avaient été évoquées, nous n'avions pas vu ce problème d'épuisement car elles étaient utilisées directement dans une boucle. Par exemple :

```python
>>> for i, j in zip(range(5), range(5, 10)):
...     print(i, j)
...
0 5
1 6
2 7
3 8
4 9
```

Ainsi, l'itérateur était généré à chaque fois qu'on lançait la boucle et n'était utilisé qu'une seule fois.

Une derniere fonction renvoyant un itérateur qui existe nativement dans les fonctions *builtins* de Python est `reversed()`. Celle-ci prend en argument un objet de type séquence (liste, tuple, chaîne de caractère ou *range*) et renvoie un itérateur parcourant la séquence en sens inverse :

```python
>>> reversed(range(5))
<range_iterator object at 0x7f8b34227780>
>>> rev_iterateur = reversed(range(5))
>>> for i in rev_iterateur:
...     print(i)
...
4
3
2
1
0
>>> list(rev_iterateur)
[]
```

Pour finir, examinons les propriétés des itérateurs que nous avions vues pour les conteneurs. Un objet itérateur est bien sûr iterable et ordonné, par contre il n'est pas indexable. Il ne supporte pas la fonction `len()`, supporte l'opérateur `in` et il est hachable.

```python
>>> animaux = ["chien", "chat", "souris"]
>>> iterateur = iter(animaux)
>>> len(iterateur)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'list_iterator' has no len()
>>> iterateur[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list_iterator' object is not subscriptable
>>> "chien" in iterateur
True
>>> hash(iterateur)
8741535406492
```

open-box-warn

L'utilisation de l'opérateur `in` pour un test d'appartenance sur un itérateur épuise ce dernier (au même titre que l'utilisation de l'itérateur dans une boucle où avec la fonction `list()`) :

```python
>>> line = "9 11 25 92 49 98 62 72 63 74"
>>> obj_map = map(int, line.split())
>>> 9 in obj_map
True
>>> 9 in obj_map
False
```

**Ligne 3**, on fait un premier test qui parcourt l'itérateur et renvoie `True`. Même si la valeur `9` était présente initialement, le deuxième test, **ligne 5**, renvoie `False` car l'itérateur est épuisé.

close-box-warn

### Module itertools

Il existe de nombreuses fonctions générant des itérateurs. Le module [`itertools`](https://docs.python.org/fr/3.12/library/itertools.html) en est particulièrement riche. Nous n'allons pas faire une liste exhaustive du contenu de ce module, mais nous parlerons de quelques fonctions qui nous paraissent utiles, notamment [`product()`](https://docs.python.org/fr/3.12/library/itertools.html#itertools.product). Son fonctionnement fait penser au [produit extérieur](https://en.wikipedia.org/wiki/Outer_product) (*outer product* en anglais) de l'algèbre tensorielle. Nous montrerons également la fonction [`groupby()`](https://docs.python.org/fr/3.12/library/itertools.html#itertools.groupby) permettant de faire des regroupements puissants. Enfin, nous évoquerons rapidement les itérateurs infinis comme la fonction `count()` à la fin de la rubrique.

#### Fonction `product()`

La fonction `product()` prend (au moins) deux conteneurs en argument et génère toutes les combinaisons possibles d'association :

```python
>>> import itertools
>>> predateurs = ["lion", "requin", "tigre"]
>>> proies = ["souris", "oiseau", "gazelle"]
>>> for pred, proie in itertools.product(predateurs, proies):
...     print(pred, proie)
...
lion souris
lion oiseau
lion gazelle
requin souris
requin oiseau
requin gazelle
tigre souris
tigre oiseau
tigre gazelle
```

Il est possible de passer plus de deux conteneurs à la fonction, par exemple : 

```python
>>> ma_liste = [1, 2]
>>> list(itertools.product(ma_liste, ma_liste, ma_liste))
[(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]
```

On a ici toutes les combinaisons possibles entre les trois objets `ma_liste` passés en argument. 

Avec deux conteneurs en argument, cette fonction `product()` revient à faire une double boucle sur les deux conteneurs. Elle est donc particulièrement adaptée pour parcourir toutes les éléments d'un tableau. Par exemple, la commande suivante parcourera toutes les cases d'un échiquier :

```python
>>> parcours_echiquier = itertools.product("abcdefgh", "12345678")
>>> parcours_echiquier
<itertools.product object at 0x7f192e412040>
>>> for col, ligne in parcours_echiquier:
...     print(col, ligne)
...
a 1
a 2
[...]
h 7
h 8
```

Mais attention, la fonction `product()` est un itérateur. Donc quand elle est épuisée, on ne peut plus l'utiliser :

```python
>>> list(parcours_echiquier)
[]
```

Une utilisation particulièrement utile de `product()` en bioinformatique peut être de générer toutes les séquences d'ADN possibles (mots) de deux lettres :

```python
>>> bases = "atgc"
>>> list(itertools.product(bases, bases))
[('a', 'a'), ('a', 't'), ('a', 'g'), ('a', 'c'), ('t', 'a'), ('t', 't'), ('t', 'g'), 
 ('t', 'c'), ('g', 'a'), ('g', 't'), ('g', 'g'), ('g', 'c'), ('c', 'a'), ('c', 't'), 
 ('c', 'g'), ('c', 'c')]
```

De même, `itertools.product(bases, bases, bases)` itérera sur tous les mots de trois lettres possibles. Ou encore, si on définit une chaîne de caractères contenant les vingt acides aminés comme suit `aas = "acdefghiklmnpqrstvwy"`, `itertools.product(aas, aas)` produira tous les dipeptides possibles. 

#### Fonction `groupby()`

La fonction  `groupby()` permet de faire des regroupements puissants. Pour vous montrer son fonctionnement, nous allons prendre un exemple. Nous partons d'une liste de mots que nous triions par longueur avec l'argument `key` auquel on passe la *callback* `len` (voir chapitre 12 *Plus sur les listes*) :

```python
>>> mots = ["bar", "babar", "bam", "ba", "bababar", "barre", "bla", "barbare"]
>>> mots.sort(key=len)
>>> mots
['ba', 'bar', 'bam', 'bla', 'babar', 'barre', 'bababar', 'barbare']
```

La fonction `groupby()` crée un itérateur particulier :

```python
>>> itertools.groupby(mots, key=len)
<itertools.groupby object at 0x7f467a6d0ca0>
>>> list(itertools.groupby(mots, key=len))
[(2, <itertools._grouper object at 0x7f467a8cf700>), 
 (3, <itertools._grouper object at 0x7f467a58c0d0>),
 (5, <itertools._grouper object at 0x7f467a58c100>), 
 (7, <itertools._grouper object at 0x7f467a58c040>)]
```

- **Lignes 1 et 3.** Il est important de passer à l'argument `key` la même fonction *callback* que lors du tri initial.
- **Lignes 4 à 7.** En transformant cet itérateur en liste, on voit qu'il génère une liste de tuples. Le premier élément de chaque tuple est un entier correspondant à une longueur de mot, le second élément est un itérateur. Que contient ce dernier ?

```python
>>> for longueur, iterateur in itertools.groupby(mots, key=len):
...     print(longueur, list(iterateur))
...
2 ['ba']
3 ['bar', 'bam', 'bla']
5 ['babar', 'barre']
7 ['bababar', 'barbare']
```

**Lignes 4 à 7.** La conversion de cet itérateur en liste montre qu'il contient tous les mots de même longueur. 

Comme vu dans une rubrique précédente, on peut passer une fonction lambda à l'argument `key` :

```python
>>> mots.sort(key=lambda chaine: chaine.count("a"))
>>> mots
['ba', 'bar', 'bam', 'bla', 'barre', 'babar', 'barbare', 'bababar']
>>> itertools.groupby(mots, key=lambda chaine: chaine.count("a"))
<itertools.groupby object at 0x7f467a6d0ca0>
>>> list(itertools.groupby(mots, key=lambda chaine: chaine.count("a")))
[(1, <itertools._grouper object at 0x7f467a58c490>), 
 (2, <itertools._grouper object at 0x7f467a58c100>), 
 (3, <itertools._grouper object at 0x7f467a58c040>)]
>>> for nb_a, iterateur in itertools.groupby(mots, key=lambda chaine: chaine.count("a")):
...     print(nb_a, list(iterateur))
...
1 ['ba', 'bar', 'bam', 'bla', 'barre']
2 ['babar', 'barbare']
3 ['bababar']
```

Ici on a regroupé les mots suivant le nombre de lettres `a` qu'ils contiennent.

open-box-adv

Avant de faire un regroupement avec`groupby()`, pensez à trier la liste initiale avec `.sort()` ou `sorted()` en utilisant la même fonction (ou fonction lambda) passée à l'argument `key`.

close-box-adv

open-box-rem

Il existe aussi une méthode `.groupby()` qui procède à des regroupements sur les *dataframes* pandas. Son mode de fonctionnement est assez différent par rapport à la fonction `groupby()` du module itertools. Vous pouvez consulter le chapitre 22 *Modules pandas* pour en savoir un peu plus.

close-box-rem

### Générateurs

open-box-def

Un **générateur** est un type d'itérateur particulier. On peut créer un générateur très facilement avec le mot-clé `yield` ou avec les expression génératrices (*generator expressions* en anglais) qui ont une syntaxe similaire à celle des listes de compréhension.

close-box-def

La création d'un générateur avec le mot-clé `yield` consiste à créer une fonction utilisant ce mot-clé. À partir de ce moment là, la fonction renvoie un générateur. Avant de voir un exemple, imaginons une fonction qui crée et renvoie une liste :

```python
>>> def cree_alphabet():
...     alphabet = []
...     for i in range(97, 123):
...         alphabet.append(chr(i))
...     return alphabet
...
>>> alphabet = cree_alphabet()
>>> alphabet
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

Pour créer un générateur équivalent, il suffira de remplacer le `.append()` par un `yield` et d'enlever le `return` :

```python
>>> def alphabet_generator():
...     for i in range(97, 123):
...         yield chr(i)
...
>>> gen = alphabet_generator()
>>> gen
<generator object alphabet_generator at 0x7fe1dffe39f0>
>>> for lettre in gen:
...     print(lettre)
...
a
b
c
[...]
y
z
>>>
>>> list(gen)
[]
```

Comme pour tous les itérateurs, une fois tous les éléments parcourus le générateur est épuisé. Notez que le `yield` n'est pas une fonction mais un mot-clé, on n'utilise donc pas de parenthèses. Ce mot-clé `yield` n'a de sens que dans une fonction et ne s'utilise que pour créer des générateurs.

La technique avec une expression génératrice ressemble à la syntaxe des listes de compréhension (voir la rubrique *Listes de compréhension* du chapitre 12 *Plus sur les listes*), mais on l'entoure de parenthèses à la place des crochets :

```python
>>> [n**2 for n in range(10)] # Liste de compréhension.
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> (n**2 for n in range(10)) # Expression génératrice.
<generator object <genexpr> at 0x7f917feb39f0>
>>> gen = (n**2 for n in range(10))
>>> for n in gen:
...     print(n)
...
0
[...]
81
```

À nouveau, le générateur est épuisé après avoir itéré dessus :

```python
>>> for nb in gen:
...     print(nb)
...
>>>
```

open-box-more

Un générateur est un itérateur, mais l'inverse n'est pas vrai. Pour comprendre toutes les subtilités liées à cette comparaison, vous pouvez consulter cette [page](https://www.datacamp.com/tutorial/python-iterators-generators-tutorial) sur le site *Datacamp*.

close-box-more

open-box-adv

Comme vous le voyez, créer un générateur est extrêmement aisé avec le mot-clé `yield` ou les expressions génératrices par rapport à l'écriture d'une classe itérateur (voir ci-dessus). Ainsi nous vous conseillons d'utiliser plutôt les générateurs lorsque vous souhaitez créer des itérateurs simples.

close-box-adv

### Pourquoi utiliser des itérateurs ?

À ce stade, vous vous posez peut-être la question « Pourquoi utiliser des itérateurs  ? ». Nous donnons quelques réponses dans cette rubrique.

#### Consommation de resources optimisée

La première raison fondamentale est la consommation de resources. Lorsque vous créez un itérateur, Python ne va pas construire l'ensemble des éléments dans la mémoire, mais plutôt préparer la « moulinette » qui réalisera les itérations. Résultat, le processsus est très peu consommateur de mémoire même en créant un itérateur itérant sur un très grand nombre d'éléments. Par ailleurs, Python crée les éléments au fur et à mesure et à la demande. C'est pour cela qu'on parle parfois « [d'évaluation paresseuse ou fainéante](https://en.m.wikipedia.org/wiki/Lazy_evaluation) » dans le sens où la valeur suivante d'un itérateur n'est pas pré-calculée mais plutôt évaluée quand on lui demande. [Trey Hunner](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/) parle ainsi d'objets itérables « paresseux ».

Un itérateur sera par ailleurs très rapide car en interne il fait appel à des routines optimisées en C. Mais aussi, l'utilisation de fonctions Python qui sont elles aussi optimisées (par exemple `sum()`) rend les itérateurs particulièrement efficaces. 

Afin de quantifier cela, on propose de mesurer le temps d'exécution de trois petits morceaux de code faisant une somme de tous les entiers de 1 à 100000 (cent mille) avec un générateur, une boucle Python classique et une liste de compréhension. Pour faire une telle mesure, nous utilisons le module [timeit](https://docs.python.org/fr/3/library/timeit.html) qui est particulièrement bien optimisé pour cela. Voici un exemple d'utilisation de `timeit` :

```python
$ python -m timeit "sum(n**2 for n in range(100000))"
50 loops, best of 5: 3.76 msec per loop
```

On peut lancer `timeit` directement à la ligne de commande Unix avec l'option `-m` suivie de l'instruction Python à exécuter entre guillemets. Python va effectuer plusieurs fois l'instruction (ici 50 fois) et donnera une approximation au plus juste du temps d'exécution de celle-ci. Le nombre d'exécutions de l'instruction dépendra du temps pris par celle-ci et sera entièrement déterminé par Python.

En revenant à notre problématique, voici les résultats de notre somme de 1 à 100000 (testé sur un ordinateur portable relativement récent avec la version Python 3.12 ) :

```bash
$ python -m timeit "sum(n**2 for n in range(100000))"
50 loops, best of 5: 3.76 msec per loop
$ python -m timeit "somme=0" "for n in range(100000): somme += n**2"
50 loops, best of 5: 3.59 msec per loop
$ python -m timeit "sum([n**2 for n in range(100000)])"
50 loops, best of 5: 4.89 msec per loop
```

- **Ligne 1.** On utilise un générateur et la fonction `sum()` pour calculer cette somme. Notez que lorsqu'un générateur est utilisé dans une fonction, les parenthèses ne sont pas obligatoires. Cela simplifie la syntaxe par rapport à `sum((n**2 for n in range(nb)))`.
- **Ligne 3.** On utilise une boucle Python classique pour calculer cette somme. Notez que pour pouvoir utiliser `timeit` sur une ligne, on est obligé de passer deux arguments entre guillemets (initialisation de la variable `somme` et boucle).
- **Ligne 5.** On utilise une liste de compréhension pour calculer cette somme.

La méthode avec les générateurs est à peu près équivalente à l'utilisation d'une boucle classique où on accumule la somme, preuve que les deux méthodes sont bien optimisées. De manière spectaculaire, la liste de compréhension est bien plus lente (presque 1 ms de plus).  Ceci vient du fait qu'il faut créer la liste de tous les éléments en mémoire, ce qui est contre-productif. Le générateur ou la boucle classique se contentent d'itérer et sont bien plus économes.

Dernier point, un test réalisé avec la version Python 3.13 sortie en octobre 2024 conduit aux mêmes observations. 

#### Itérateurs infinis

Bien que la taille de la mémoire d'un ordinateur soit finie, il est possible de créer des itérateurs infinis ! Par exemple, la fonction [`count()`](https://docs.python.org/3/library/itertools.html#itertools.count) du module itertools itère de 0 (lorsqu'on l'appelle sans argument) jusqu'à l'infini :

```python
>>> iterateur = itertools.count()
>>> import itertools
>>> iterateur = itertools.count()
>>> for i in iterateur:
...      print(i)
...
0
1
2
3
[Boucle infinie]
```

Attention de ne pas transformer cet itérateur en liste ou tuple sous peine de saturer la mémoire de l'ordinateur et de le faire planter !

Dans le même module les fonctions [`cycle()`](https://docs.python.org/3/library/itertools.html#itertools.cycle) et [`repeat()`](https://docs.python.org/3/library/itertools.html#itertools.repeat) sont également des itérateurs infinis.

#### Meilleure lisibilité

De manière générale, l'utilisation d'itérateurs peut améliorer la lisibilité de vos programmes. Cet [article](https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/#How_iterators_can_improve_your_code) fait remarquer que le simple fait de créer un itérateur et de le nommer donne un sens à ce qu'il contient. En reprenant notre exemple sur la somme des carrés :

```python
tous_les_carres = (n**2 for n in range(nb))
somme = sum(tous_les_carres)
```

Si on compare à la boucle `for` :

```python
somme = 0
for n in range(nb):
    somme += n**2
```

On voit que ce que représente l'objet `tous_les_carres` n'existe tout simplement pas avec la boucle `for` ! Par ailleurs, outre l'avantage de rapidité, l'utilisation de la fonction `sum()` rend la lecture très claire.

Dernier point, les itérateurs et notamment les générateurs, donnent un moyen de faire de la [programmation fonctionnelle](https://fr.wikipedia.org/wiki/Programmation_fonctionnelle) en Python. Sans rentrer dans les considérations théoriques, nous avons déjà vu l'idée générale lorsque nous avons abordé le *method chaining* sur les chaînes de caractères ou sur les *dataframes* pandas. Initialement, la programmation fonctionnelle en Python utilisait la fonction `map()` (ainsi que les fonctions `filter()` et `reduce()` non abordées ici). Mais depuis l'arrivée des générateurs, on préfère ces derniers qui sont considérés plus Pythoniques. Regardons un exemple où nous transformons une chaîne de caractères en entiers puis nous calculons la somme. D'abord avec un générateur :

```python
>>> ligne = "9 11 25 92 49 98 62 72 63 74"
>>> sum(int(nb) for nb in ligne.split())
555
>>>
```

Ensuite avec la fonction `map()` :

```python
>>> line = "9 11 25 92 49 98 62 72 63 74"
>>> sum(map(int, line.split()))
555
```

Ne trouvez-vous pas que la version avec le générateur est plus lisible ?

Comme proposé par [Dan Bader](https://dbader.org/blog/python-iterator-chains), on peut chainer les générateurs :

```python
>>> import math
>>> ligne = "9 11 25 92 49 98 62 72 63 74"
>>> nombres = (int(nb) for nb in ligne.split())
>>> inverses = (nb**-1 for nb in nombres)
>>> cos_inverses = (math.cos(nb) for nb in inverses)
>>> sum(cos_inverse)
9.988141056338993
```

Une chose à noter dans cet exemple est que lorsqu'on crée un générateur à partir d'un autre générateur, le générateur initial n'est pas déclenché. Par exemple, en **Ligne 4** pour `inverses` le générateur `nombres` n'est pas encore déclenché, ou en **Ligne 5** pour `cos_inverses` le générateur `inverses` n'est pas déclenché non plus. Tous les générateurs seront déclenchés en chaine lorsqu'on exécutera la **Ligne 6**.

open-box-adv

En écrivant un générateur par ligne, le code est bien lisible. Evitez une syntaxe en une ligne qui s'avérera illisible : `(math.cos(nb) for nb in (nb**-1 for nb in (int(nb) for nb in ligne.split())))`

close-box-adv

## Gestion des exceptions

Les langages de programmation comme Python contiennent un [système de gestion des **exceptions**](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions). Qu'est-ce qu'une exception ? Sur la [page anglaise de Wikipedia](https://en.wikipedia.org/wiki/Exception_handling), une exception est définie comme une anomalie de l'exécution d'un programme requérant une action spéciale, en général l'arrêt de l'exécution. Le plus souvent, **une exception correspond à une erreur** que Python rencontre lorsqu'il tente d'exécuter les lignes de code qu'on lui soumet. Par exemple, un problème de syntaxe, une variable ou objet qui prend une valeur aberrante (par exemple diviser par 0, parcourir une liste au-delà du nombre d'éléments, etc.). 

Le système de gestion des exceptions évite que votre programme « plante » en prévoyant vous-même les sources d'erreurs éventuelles.

Voici un exemple dans lequel on demande à l'utilisateur d'entrer un nombre entier, puis on affiche ce nombre.

```python
>>> nb = int(input("Entrez un nombre entier : "))
Entrez un nombre entier : 23
>>> print(nb)
23
```

La fonction `input()` demande à l'utilisateur de saisir une chaîne de caractères. Cette chaîne de caractères est ensuite transformée en nombre entier avec la fonction `int()`.

Si l'utilisateur ne rentre pas un nombre, voici ce qui se passe :

```python
>>> nb = int(input("Entrez un nombre entier : "))
Entrez un nombre entier : ATCG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ATCG'
```

L'erreur provient de la fonction `int()` qui n'a pas pu convertir la chaîne de caractères `"ATCG"` en nombre entier, ce qui est parfaitement normal. En termes plus techniques, on dira que « Python a levé une exception de type `ValueError` ». Eh oui il y a de nombreux types d'exceptions différents (voir plus bas) ! Le nom de l'exception apparaît toujours comme le premier mot de la dernière ligne du message d'erreur. Si nous lancions ces lignes de code sous forme de script (du style `python script.py`), cet exemple conduirait à l'arrêt de l'exécution du programme.

Le jeu d'instructions `try` / `except` permet de tester l'exécution d'une commande et d'intervenir en cas de levée d'exception.

```python
>>> try:
...     nb = int(input("Entrez un nombre entier : "))
... except:
...     print("Vous n'avez pas entré un nombre entier !")
...
Entrez un nombre entier : ATCG
Vous n'avez pas entré un nombre entier !
```

Dans cet exemple, l'exception levée par la fonction `int()` (qui ne peut pas convertir `"ATCG"` en nombre entier) est interceptée et déclenche l'affichage du message d'avertissement.

On peut ainsi redemander sans cesse un nombre entier à l'utilisateur, jusqu'à ce que celui-ci en rentre bien un.

```python
>>> while True:
...     try:
...         nb = int(input("Entrez un nombre entier : "))
...         print("Le nombre est", nb)
...         break
...     except:
...         print("Vous n'avez pas entré un nombre entier !")
...         print("Essayez encore")
...
Entrez un nombre entier : ATCG
Vous n'avez pas entré un nombre entier !
Essayez encore
Entrez un nombre entier : toto
Vous n'avez pas entré un nombre entier !
Essayez encore
Entrez un nombre entier : 3.2
Vous n'avez pas entré un nombre entier !
Essayez encore
Entrez un nombre entier : 55
Le nombre est 55
```

Notez que dans cet exemple, l'instruction `while True` est une boucle infinie car la condition `True` est toujours vérifiée. L'arrêt de cette boucle est alors forcé par la commande `break` lorsque l'utilisateur a effectivement entré un nombre entier.

La gestion des exceptions est très utile dès lors que des données extérieures entrent dans un programme Python, que ce soit directement par l'utilisateur (avec la fonction `input()`) ou par des fichiers. Cela est fondamental si vous distribuez votre code à la communauté : si les utilisateurs ne connaissent pas Python, un message comme `Vous n'avez pas entré un nombre entier !` reste plus clair que `ValueError: invalid literal for int() with base 10: 'ATCG'`.

Vous pouvez par exemple vérifier qu'un fichier a bien été ouvert.

```python
>>> nom = "toto.pdb"
>>> try:
...     with open(nom, "r") as fichier:
...         for ligne in fichier:
...             print(ligne)
... except:
...     print("Impossible d'ouvrir le fichier", nom)
```

Si une erreur est déclenchée, c'est sans doute que le fichier n'existe pas à l'emplacement indiqué sur le disque ou que vous n'avez pas les droits pour le lire.

Il est également possible de spécifier le type d'erreur à gérer. Le premier exemple que nous avons étudié peut s'écrire :

```python
>>> try:
...     nb = int(input("Entrez un nombre entier : "))
... except ValueError:
...     print("Vous n'avez pas entré un nombre entier !")
...
Entrez un nombre entier : ATCG
Vous n'avez pas entré un nombre entier !
```

Ici, on intercepte une exception de type `ValueError`, ce qui correspond bien à un problème de conversion avec `int()`. 

Attention, si vous précisez le type d'exception comme `ValueError`, le `except ValueError` n'empêchera pas la levée d'une autre exception.

```python
>>> try:
...     nb = int(variable)
... except ValueError:
...     print("Vous n'avez pas entré un nombre entier !")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'variable' is not defined. Did you mean: 'callable'?
```

Ici l'exception levée est de type `NameError`, car `variable` n'existe pas. Alors que si vous mettez `except` tout court, cela intercepte n'importe quelle exception.

```python
>>> try:
...    nb = int(variable)
... except:
...    print("Vous n'avez pas entré un nombre entier !")
...
Vous n'avez pas entré un nombre entier !
>>>
```

Vous voyez qu'ici cela pose un nouveau problème : le message d'erreur ne correspond pas à l'exception levée !

open-box-adv

- Nous vous conseillons vivement de toujours préciser le type d'exception dans vos `except`. Cela évite d'intercepter une exception que vous n'aviez pas prévue. Il est possible d'intercepter plusieurs types d'exceptions en passant un tuple à `except`, par exemple : `except (Exception1, Exception2)`. 
- Par ailleurs, ne mettez pas trop de lignes dans le bloc du `try`. Dans un tel cas, il peut être très pénible de trouver la ligne qui a conduit à l'exécution du `except`. Pire encore, il se peut que des lignes que vous aviez prévues ne soient pas exécutées ! Donc gardez des choses simples dans un premier temps, comme par exemple tester les conversions de type ou vérifier qu'un fichier existe bien et que vous pouvez l'ouvrir.

close-box-adv

Il existe de nombreux types d'exception comme `RuntimeError`, `TypeError`, `NameError`, `IOError`, etc. Vous pouvez aller voir la [liste complète](https://docs.python.org/fr/3.12/library/exceptions.html#exceptions.TypeError) sur le site de Python. Nous avions déjà croisé des noms d'exception au chapitre 23 (*Avoir la classe avec les objets*) en regardant ce que contient le module `builtins`.

```python
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
[...]
'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError'
[...]
```

Leur présence dans le module `builtins` signifie qu'elles font partie du langage lui même, au même titre que les fonctions de base comme `range()`, `list()`, etc. 

Avez-vous aussi remarqué que leur nom commence toujours par une majuscule et qu'il peut en contenir plusieurs à la façon *CamelCase* ? Si vous avez bien lu le chapitre 16 *Bonnes pratiques en programmation Python*, avez-vous deviné pourquoi ? Et bien, c'est parce que **les exceptions sont des classes**. C'est très intéressant car il est ainsi possible d'utiliser l'héritage pour créer ses propres exceptions à partir d'exceptions pré-existantes. Nous ne développerons pas cet aspect, mais en guise d'illustration, regardez ce que renvoit  un `help()` de l'exception `OverflowError`.

```python
>>> help(OverflowError)
[...]
class OverflowError(ArithmeticError)
 |  Result too large to be represented.
 |
 |  Method resolution order:
 |      OverflowError
 |      ArithmeticError
 |      Exception
 |      BaseException
 |      object
```

L'exception `OverflowError` hérite de `ArithmeticError`, c'est-à-dire qu'`OverflowError` a été conçue à partir de `ArithmeticError` et en hérite de tous ses attributs.

Un autre aspect très important que nous avons croisé au chapitre 24 *Avoir plus la classe avec les objets* est la possibilité de lever vous-même une exception avec le mot-clé `raise`. Nous avions vu le code suivant :

```
if valeur < 0:
    raise ValueError("Z'avez déjà vu une masse négative ?")
```

La ligne 2 lève une exception `ValueError` lorsque la variable `valeur` est négative. L'instruction `raise` est bien pratique lorsque vous souhaitez stopper l'exécution d'un programme si une variable ne se trouve pas dans le bon intervalle ou ne contient pas la bonne valeur. Vous avez sans doute compris maintenant pourquoi on parlait de « levée » d'exception...

Enfin, on peut aussi être très précis dans le message d'erreur. Observez la fonction `download_page()` qui, avec le module *urllib*, télécharge un fichier sur internet.

```python
import urllib.request

def download_page(address):
    error = ""
    page = ""
    try:
        data = urllib.request.urlopen(address)
        page = data.read()
    except IOError as e:
        if hasattr(e, 'reason'):
            error =  "Cannot reach web server: " + str(e.reason)
        if hasattr(e, 'code'):
            error = f"Server failed {e.code:d}"
    return page, error

data, error = download_page("https://files.rcsb.org/download/1BTA.pdb")

if error:
    print(f"Erreur rencontrée : {error}")
else:
    with open("proteine.pdb", "w") as prot:
        prot.write(data.decode("utf-8"))
    print("Protéine enregistrée")
```

La variable `e` est une instance de l'exception `IOError`. Certains de ses attributs sont testés avec la fonction `hasattr()` pour ainsi affiner le message renvoyé (ici contenu dans la variable `error`).

Si tout se passe bien, la page est téléchargée est stockée dans la variable `data`, puis enregistrée sur le disque dur.



## Shebang et /usr/bin/env python3

Lorsque l'on programme sur un système Unix (Mac OS X ou Linux par exemple), on peut exécuter directement un script Python, sans appeler explicitement la commande `python`.

Pour cela, deux opérations sont nécessaires :

**Étape 1.** Préciser la localisation de l'interpréteur Python en indiquant dans la première ligne du script :
   
```python
#! /usr/bin/env python
```

Par exemple, si le script *test.py* contenait :

```python
print("Hello World !")
```

il va alors contenir :

```python
#!/usr/bin/env python

print("Hello World !")
```

**Étape 2.**. Rendre le script Python exécutable en lançant l'instruction :

```bash
$ chmod +x test.py
```

open-box-rem

La ligne `#! /usr/bin/env python` n'est pas considérée comme un commentaire
par Python, ni comme une instruction Python d'ailleurs . Cette ligne a une signification
particulière pour le système d'exploitation Unix.

close-box-rem

Pour exécuter le script, il suffit alors de taper son nom précédé des deux caractères **./** (afin de préciser au *shell* où se trouve le script) :

```bash
$ ./test.py
Hello World !
```

open-box-def

Le [**shebang**](http://fr.wikipedia.org/wiki/Shebang) correspond aux caractères `#!` qui se trouvent au début de la première ligne du script `test`.

Le *shebang* est suivi du chemin complet du programme qui interprète le script ou du programme qui sait où se trouve l'interpréteur Python. Dans l'exemple précédent, c'est le programme `/usr/bin/env` qui indique où se trouve l'interpréteur Python.

close-box-def

## Passage d'arguments avec `*args` et `**kwargs`

Avant de lire cette rubrique, nous vous conseillons de bien relire et maîtriser la rubrique *Arguments positionnels et arguments par mot-clé* du chapitre 10 *Fonctions*.

Dans le chapitre 10, nous avons vu qu'il était nécessaire de passer à une fonction tous les arguments positionnels définis dans celle-ci. Il existe toutefois une astuce permettant de passer un nombre arbitraire d'arguments positionnels :

```python
>>> def fct(*args):
...     print(args)
...
>>> fct()
()
>>> fct(1)
(1,)
>>> fct(1, 2, 5, "Python")
(1, 2, 5, 'Python')
>>> fct(z=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: fct() got an unexpected keyword argument 'z'
```

L'utilisation de la syntaxe `*args` permet d'empaqueter tous les arguments positionnels dans un *tuple* unique `args` récupéré au sein de la fonction. L'avantage est que nous pouvons passer autant d'arguments positionnels que l'on veut. Toutefois, on s'aperçoit en ligne 10 que cette syntaxe ne fonctionne pas avec les arguments par mot-clé.

Il existe un équivalent avec les arguments par mot-clé :

```python
>>> def fct(**kwargs):
...     print(kwargs)
...
>>> fct()
{}
>>> fct(z=1, gogo="toto")
{'gogo': 'toto', 'z': 1}
>>> fct(z=1, gogo="toto", y=-67)
{'y': -67, 'gogo': 'toto', 'z': 1}
>>> fct(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: fct() takes 0 positional arguments but 2 were given
```

La syntaxe `**kwargs` permet d'empaqueter l'ensemble des arguments par mot-clé, quel que soit leur nombre, dans un dictionnaire unique `kwargs` récupéré dans la fonction. Les clés et valeurs de celui-ci sont les noms des arguments et les valeurs passées à la fonction. Toutefois, on s'aperçoit en ligne 9 que cette syntaxe ne fonctionne pas avec les arguments positionnels.

Si on attend un mélange d'arguments positionnels et par mot-clé, on peut utiliser `*args` et  `**kwargs` en même temps :

```python
>>> def fct(*args, **kwargs):
...     print(args)
...     print(kwargs)
...
>>> fct()
()
{}
>>> fct(1, 2)
(1, 2)
{}
>>> fct(z=1, y=2)
()
{'y': 2, 'z': 1}
>>> fct(1, 2, 3, z=1, y=2)
(1, 2, 3)
{'y': 2, 'z': 1}
```

Deux contraintes sont toutefois à respecter. Il faut toujours :

- mettre `*args` avant `**kwargs` dans la définition de la fonction ;
- passer les arguments positionnels avant ceux par mot-clé lors de l'appel de la fonction.

Il est possible de combiner des arguments positionnels avec `*args` et des arguments par mot-clé avec `**kwargs`, par exemple :

`def fct(a, b, *args, **kwargs):`

Dans un tel cas, il faudra obligatoirement passer les deux arguments `a` et `b` à la fonction, ensuite on pourra mettre un nombre arbitraire d'arguments positionnels (récupérés dans le tuple `args`), puis un nombre arbitraire d'arguments par mot-clé (récupérés dans le dictionnaire `kwargs`).

open-box-adv

Les noms `*args` et `**kwargs` sont des conventions en Python, ils rappellent les mots *arguments* et *keyword arguments*. Bien qu'on puisse mettre ce que l'on veut, nous vous conseillons de respecter ces conventions pour faciliter la lecture de votre code par d'autres personnes.

close-box-adv

L'utilisation de la syntaxe `*args` et `**kwargs` est très classique dans le module *Fenêtres graphiques et Tkinter* présenté dans le chapitre 25 (en ligne).

Il est possible d'utiliser ce mécanisme d'empaquetage / désempaquetage (*packing* / *unpacking*) dans l'autre sens :

```python
>>> def fct(a, b, c):
...    print(a,b,c)
...
>>> t = (-5,6,7)
>>>
>>> fct(*t)
-5 6 7
```

Avec la syntaxe `*t` on désempaquette le tuple à la volée lors de l'appel à la fonction. Cela est aussi possible avec un dictionnaire : 

```python
>>> def fct(x, y, z):
...    print(x, y, z)
...
>>> dico = {'x': -1, 'y': -2, 'z': -3}
>>> fct(**dico)
-1 -2 -3
```

Attention toutefois à bien respecter deux choses :

- la concordance entre le nom des clés du dictionnaire et le nom des arguments dans la fonction (sinon cela renvoie une erreur) ;
- l'utilisation d'une double étoile pour désempaqueter les valeurs du dictionnaire (si vous utilisez une seule étoile, Python désempaquettera les clés !).

Ce mécanisme de désempaquetage est aussi utilisable avec les objets *zip*, on parle de *zip unpacking*. Souvenons-nous, un objet *zip* permettait d'assembler plusieurs listes, éléments par éléments (voir Chapitre 12 *Plus sur les listes*) :

```python
>>> animaux = ["poulain", "renard", "python"]
>>> couleurs = ["alezan", "roux", "vert"]
>>> zip(range(3), animaux, couleurs)
<zip object at 0x7f333febc880>
>>> triplets = list(zip(range(3), animaux, couleurs))
>>> triplets
[(0, 'poulain', 'alezan'), (1, 'renard', 'roux'), (2, 'python', 'vert')]
```

**Lignes 1 à 4**. On crée un objet *zip* avec trois objets de trois éléments.

**Lignes 5 à 7**. Cet objet *zip* en conjonction avec la fonction `list()` nous permet d'associer les éléments par ordre d'apparition (tous les éléments à la position 1 se retrouve ensemble, idem pour les positions 2 et 3). Au final, l'objet `triplets` est une liste de *tuples* de trois éléments.

L'opérateur `*` en combinaison avec la fonction *zip* va nous permettre de désempaqueter `triplets` pour récupérer les listes initiales (`range(3)`, `animaux` et `couleurs`) :

```python
>>> zip(*triplets)
<zip object at 0x7f333fd44980>
>>> list(zip(*triplets))
[(0, 1, 2), ('poulain', 'renard', 'python'), ('alezan', 'roux', 'vert')]
```

Bien sûr, on peut l'utiliser l'affectation multiple :

```python
>>> numéros2, animaux2, couleurs2 = zip(*triplets)
>>> numéros2
(0, 1, 2)
>>> animaux2
('poulain', 'renard', 'python')
>>> couleurs2
('alezan', 'roux', 'vert')
```

Au final, on récupère des *tuples* au lieu des listes initiales. Mais à ce stade, vous devriez être capable de les retransformer en liste ;-).

## Décorateurs

Dans le chapitre 24, nous avons rencontré la notion de décorateur pour déclarer des objets de type *property*. Cela permettait de rendre des méthodes accessibles comme des attributs (décorateur `@property`), et plus généralement de contrôler l'accès, la modification et la destruction d'attributs (décorateurs `@nom_attribut.setter` et `@nom_attribut.deleter`). Il existe d'autres décorateurs prédéfinis en Python (e.g. `@staticmethod`, `@classmethod`, etc.). Nous allons voir dans cette section comment on crée ses propres décorateurs et les mécanismes sous-jacents. Nous vous conseillons de bien relire commment fonctionne les fonctions de rappel, ou fonctions *callback* (chapitre 25 *Tkinter*).

open-box-def

Un décorateur est une fonction qui modifie le comportement d'une autre fonction.

close-box-def

Ceci étant dit, comme cela fonctionne-t-il ? Commençons par une fonction simple qui affiche de la nourriture :

```python
def imprime_victuaille():
    print("tomate / mozza")
```

On souhaite améliorer cette fonction et transformer cette victuaille en sandwich, en affichant une tranche de pain avant et après. La stratégie va être de créer une fonction spéciale, qu'on appelle **décorateur**, modifiant `imprime_victuaille()`.

```python
def transforme_en_sandwich(fonction_a_decorer):
    def emballage():
        print("Pain")
        fonction_a_decorer()
        print("Pain")
    return emballage
```

La fonction `transforme_en_sandwich()` est notre décorateur, elle prend en argument la fonction que l'on souhaite décorer sous forme de *callback* (donc sans les parenthèses). On voit qu'à l'intérieur, on définit une sous-fonction `emballage()` qui va littéralement « emballer » (*wrap*) notre fonction à décorer, c'est-à-dire, effectuer une action avant et après l'appel de la fonction à décorer. Enfin, le décorateur renvoie cette sous-fonction `emballage` sous forme de *callback*.  Pour que le décorateur soit actif, il faudra « transformer » la fonction à décorer avec notre fonction décoratrice :

```python
imprime_victuaille = transforme_en_sandwich(imprime_victuaille)
```

Voici le code complet implémentant la fonction `imprime_victuaille()` décorée :

```python
def transforme_en_sandwich(fonction_a_decorer):
    def emballage():
        print("Pain")
        fonction_a_decorer()
        print("Pain")
    return emballage

def imprime_victuaille():
    print("tomate/ mozza")

if __name__ == "__main__":
    print("Fonction non décorée:")
    imprime_victuaille()
    print()
    print("Fonction décorée:")
    imprime_victuaille = transforme_en_sandwich(imprime_victuaille)
    imprime_victuaille()
```

Au final l'idée est d'appeler la fonction décoratrice plutôt que la fonction `imprime_victuaille()` elle-même. Regardons ce que donne l'exécution de la fonction avant et après décoration :

```text
Fonction non décorée:
tomate/ mozza

Fonction décorée:
Pain
tomate/ mozza
Pain
```

Le premier appel en ligne 13 exécute la fonction simple, alors que le second en ligne 17 exécute la fonction décorée. Cette construction peut sembler ardue et difficile à comprendre. Heureusement, Python a une notation en  « *sucre syntaxique* » (*syntactic sugar*) qui en facilite la lecture. Celle-ci utilise le symbole `@` :

```python
def transforme_en_sandwich(fonction_a_decorer):
    def emballage():
        print("Pain")
        fonction_a_decorer()
        print("Pain")
    return emballage

@transforme_en_sandwich
def imprime_victuaille():
    print("tomate / mozza")

if __name__ == "__main__":
    imprime_victuaille()
```

La ligne 8 transforme irrémédiablement la fonction `imprime_victuaille()` en fonction décorée. Cela parait déjà un peu plus lisible. L'exécution donnera bien sûr :

```text
Pain
tomate / mozza
Pain
```

Au final, la notation :

```python
@decorator
def fct():
    [...]
```

est équivalente à :

```python
fct = decorator(fct)
```

Cela fonctionne avec n'importe quelle fonction prenant en argument une autre fonction.

open-box-adv

Nous vous conseillons bien sûr d'utiliser systématiquement la notation `@decorator` qui est plus lisible et intuitive.

close-box-adv


Si tout cela vous semble ardu (on vous comprend...), vous devez vous dire « pourquoi utiliser une construction aussi complexe ? ». Et bien, c'est tout simplement parce qu'un décorateur est ré-utilisable dans n'importe quelle fonction. Si on reprend la même fonction décoratrice que ci-dessus :

```python
@transforme_en_sandwich
def imprime_victuaille1():
    print("tomate / mozza")

@transforme_en_sandwich
def imprime_victuaille2():
    print("jambon / fromage")

if __name__ == "__main__":
    imprime_victuaille1()
    print()
    imprime_victuaille2()
```

On a donc un décorateur permettant de transformer en sandwich n'importe quelle fonction imprimant une victuaille ! Ceci renverra :

```text
Pain
tomate / mozza
Pain

Pain
jambon / fromage
Pain
```

Un exemple plus concret de décorateur pourrait être la mesure du temps d'exécution d'une fonction :

```text
import time

def mesure_temps(fonction_a_decorer):
    def emballage():
        temps1 = time.time()
        fonction_a_decorer()
        temps2 = time.time()
		print(f"Le temps d'éxécution de {fonction_a_decorer.__name__} est "
              f"{temps2 - temps1} s")
    return emballage
```

En ligne 8, l'attribut `.__name__` renvoie le nom de la fonction sous forme de chaîne de caractères. Dans cet exemple, le décorateur `@mesure_temps` mis devant n'importe quelle fonction affichera systématiquement le temps d'exécution de celle-ci.

Pour finir, si on revient sur le décorateur `@property` vu dans le chapitre 24 *Avoir plus la classe avec les objets*, nous avions vu également qu'il existait une fonction `property()`. Donc pour les décorateurs pré-existants que nous avons abordés dans le chapitre 24, il existe des fonctions équivalentes. Comme dans notre exemple, la notation `@decorateur` va finalement appeler la fonction décoratrice. Donc derrière une notation `@quelquechose`, il existe toujours une fonction `quelquechose()` remplissant ce rôle de décorateur.

open-box-more

Pour aller plus loin, vous pouvez consulter ce très [bon article](https://realpython.com/primer-on-python-decorators/) sur le site *RealPython*. Il y est expliqué en outre comment on peut gérer le passage d'arguments quand on utilise des décorateurs, ainsi que l'utilisation de décorateurs multiples.

close-box-more

## Un peu de transformée de Fourier avec *NumPy*

La transformée de Fourier est très utilisée pour l'analyse de signaux, notamment lorsqu'on souhaite extraire des périodicités au sein d'un signal bruité. Le module *NumPy* possède la fonction `fft()` (dans le sous-module *fft*) permettant de calculer des transformées de Fourier.

Voici un petit exemple sur la fonction cosinus de laquelle on souhaite extraire la période à l'aide de la fonction `fft()` :

```python
import numpy as np

debut = -2 * np.pi
fin = 2 * np.pi
pas = 0.1
x = np.arange(debut,fin,pas)
y = np.cos(x)

TF = np.fft.fft(y)
ABSTF = np.abs(TF)
pas_xABSTF = 1/(fin-debut)
x_ABSTF = np.arange(0,pas_xABSTF * len(ABSTF),pas_xABSTF)
```

Plusieurs commentaires sur cet exemple :

Ligne 1. On charge le module *NumPy* avec le nom raccourci `np`.

Lignes 3 à 6. On définit l'intervalle (de $-2\pi$ à $2\pi$ radians) pour les valeurs en abscisse ainsi que le pas (0,1 radians).

Lignes 7. On calcule directement les valeurs en ordonnées avec la fonction cosinus du module *NumPy*. On constate ici que *NumPy* redéfinit certaines fonctions ou constantes mathématiques de base, comme `pi`, `cos()` ou `abs()` (valeur absolue, ou module d'un nombre complexe). Ces fonctions sont directement utilisables avec un objet *array*.

Ligne 9. On calcule la transformée de Fourier avec la fonction `fft()` qui renvoie un vecteur (objet *array* à une dimension) de nombres complexes. Eh oui, le module *NumPy* gère aussi les nombres complexes !

Ligne 10. On extrait le module du résultat précédent avec la fonction `abs()`.

Ligne 11. La variable `x_ABSTFL` représente l'abscisse du spectre (en radian$^{-1}$).

Ligne 12. La variable `ABSTF` contient le spectre lui même. L'analyse de ce dernier nous donne un pic à 0,15 radian$^{-1}$, ce qui correspond bien à $2\pi$ (c'est plutôt bon signe de retrouver ce résultat).


## Sauvegardez votre historique de commandes

Vous pouvez sauvegarder l'historique des commandes utilisées dans l'interpréteur Python avec le module `readline`.

```python
>>> print("hello")
hello
>>> a = 22
>>> a = a + 11
>>> print(a)
33
>>> import readline
>>> readline.write_history_file()
```

Quittez Python. L'historique de toutes vos commandes est dans votre répertoire personnel, dans le fichier `.history`.

Relancez l'interpréteur Python.

```python
>>> import readline
>>> readline.read_history_file()
```

Vous pouvez accéder aux commandes de la session précédente avec la flèche du haut de votre clavier. D'abord les commandes `readline.read_history_file()` et `import readline` de la session actuelle, puis `print(a)`, `a = a + 11`, `a = 22`...
