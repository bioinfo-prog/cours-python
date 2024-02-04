# Remarques complémentaires

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

Par contre en Python 3, `print()` est une fonction. Ainsi, si vous n'utilisez pas de parenthèse, Python vous renverra une erreur :

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

La création de liste avec `range()` était pratique mais très peu efficace en mémoire lorsque l'argument donné à `range()` était un grand nombre.

D'ailleurs la fonction `xrange()` est disponible en Python 2 pour faire la même chose que la fonction `range()` en Python 3. Attention, ne vous mélangez pas les pinceaux !

```python
>>> range(3)
[0, 1, 2]
>>> xrange(3)
xrange(3)
```

open-box-rem

Pour générer une liste d'entiers avec la fonction `range()` en Python 3, vous avez vu dans le chapitre 4 *Listes* qu'il suffit de l'associer avec la fonction `list()`. Par exemple :

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

close-box-rem

open-box-rem
En Python 3, la fonction `range()` est ce qu'on appelle un **générateur** dans le sens où elle génère un objet contenant une série de valeurs, utilisables une à la fois, par itération dans une boucle *for*. L'objet de type *range* renvoyé par la fonction est quant à lui appelé **itérateur**. Si vous souhaitez en savoir un peu plus sur la différence entre un générateur et un itérateur, vous pouvez consulter cette [ressource](https://data-flair.training/blogs/python-generator-vs-iterator/).
close-box-rem

### Encodage et utf-8

En Python 3, vous pouvez utiliser des caractères accentués dans les commentaires ou dans les chaîne de caractères.

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

## Ancienne méthode de formatage des chaînes de caractères

Dans les premières versions de Python jusqu'à la 2.6, il fallait utiliser l'opérateur `%`, puis de la version 2.7 jusqu'à la 3.5 il était plutôt conseillé d'utiliser la méthode `.format()` (voir la rubrique suivante pour la définition du mot « méthode »). Même si les *f-strings* sont devenues la manière conseillée pour mettre en place l'écriture formatée, ces deux anciennes manières, sont encore pleinement compatibles avec les versions modernes de Python.

Même si elle fonctionne encore, la première manière avec l'opérateur `%` est maintenant clairement déconseillée pour un certain nombre de [raisons](https://docs.python.org/fr/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting). Néanmoins, nous rappelons ci-dessous son fonctionnement, car il se peut que vous tombiez dessus dans d'anciens livres ou si vous lisez de vieux programmes Python.

La deuxième manière avec la méthode `.format()` est encore largement utilisée et reste tout à fait valide. Elle est clairement plus puissante et évite un certain nombre de désagréments par rapport à l'opérateur `%`. Vous la croiserez sans doute très fréquemment dans des programmes et ouvrages récents. Heureusement elle a un fonctionnement relativement proche des *f-strings*, donc vous ne serez pas totalement perdus !

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

Depuis la version 2.7 de Python, la méthode `.format()` (voir la rubrique suivante pour la définition d'une méthode) a apporté une nette amélioration pour mettre en place l'écriture formatée. Celle-ci fonctionne de la manière suivante :

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

Tout ce que nous avons vu avec les *f-strings* sur la manière de formatter l'affichage d'une variable (après les `:` au sein des accolades) est identique avec la méthode `.format()`. Par exemple `{:.2f}`, `{:0>6d}`, `{:.6e}`, etc., fonctionneront de la même manière. La différence notable est qu'on ne met pas directement le nom de la variable au sein des accolades. Comme pour l'opérateur `%`, c'est l'emplacement dans les arguments passés à la méthode `.format()` qui dicte quelle variable doit être remplacée. Par exemple, dans `"{} {} {}".format(bidule, machin, truc)`, les premières accolades remplaceront la variable `bidule`, les deuxièmes la variable `machin`, les troisièmes la variable `truc`.

Le formattage avec la méthode `.format()` se rapproche de la syntaxe des *f-strings* (accolades, deux-points), mais présente l'inconvénient -- comme avec l'opérateur `%` -- de devoir mettre la liste des variables tout à la fin, alourdissant ainsi la syntaxe. En effet, dans l'exemple avec la proportion de GC, la ligne équivalente avec une *f-string* apparait tout de même plus simple à lire :

```python
>>> print(f"On a {nb_G} G et {nb_C} C -> prop GC = {prop_GC:.2f}")
On a 4500 G et 2575 C -> prop GC = 0.48
```

open-box-adv

Pour conclure, ces deux anciennes façons de formater une chaîne de caractères avec l'opérateur `%` ou la méthode `.format()` vous sont présentées à titre d'information. La première avec l'opérateur `%` est clairement déconseillée. La deuxième avec la méthode `.format()` est encore tout à fait valable. Si vous débutez Python, nous vous conseillons fortement d'apprendre et d'utiliser les *f-strings*. C'est ce que vous rencontrerez dans la suite de ce cours. Si vous connaissez déjà Python et que vous utilisez la méthode `.format()`, nous vous conseillons de passer aux *f-strings*. Depuis que nous les avons découvertes, aucun retour n'est envisageable pour nous tant elles sont puissantes et plus claires à utiliser ! 

Enfin, si vous souhaitez aller plus loin, voici deux articles (en anglais) très bien faits sur le site *RealPython*: sur l'[écriture formatée](https://realpython.com/python-string-formatting) et sur les [*f-strings*](https://realpython.com/python-f-strings/)

close-box-adv


## Gestion des exceptions

Les langages de programmation comme Python contiennent un [système de gestion des **exceptions**](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions). Qu'est-ce qu'une exception ? Sur la [page anglaise de Wikipedia](https://en.wikipedia.org/wiki/Exception_handling), une exception est définie comme une anomalie de l'exécution d'un programme requérant une action spéciale, en général l'arrêt de l'exécution. Le plus souvent, **une exception correspond à une erreur** que Python rencontre lorsqu'il tente d'exécuter les lignes de code qu'on lui soumet. Par exemple, un problème de syntaxe, une variable ou objet qui prend une valeur aberrante (par exemple diviser par 0, parcourir une liste au delà du nombre d'éléments, etc.). 

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

Dans cette exemple, l'exception levée par la fonction `int()` (qui ne peut pas convertir `"ATCG"` en nombre entier) est interceptée et déclenche l'affichage du message d'avertissement.

On peut ainsi redemander sans cesse un nombre entier à l'utilisateur, jusqu'à ce que celui-ci en rentre bien un.

```python
>>> while True:
...     try:
...             nb = int(input("Entrez un nombre entier : "))
...             print("Le nombre est", nb)
...             break
...     except:
...             print("Vous n'avez pas entré un nombre entier !")
...             print("Essayez encore")
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

Ici l'exception levée est de type `NameError` car `variable` n'existe pas. Alors que si vous mettez `except` tout court, cela intercepte n'importe quelle exception.

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
- Pa ailleurs, ne mettez pas trop de lignes dans le bloc du `try`. Dans un tel cas, il peut être très pénible de trouver la ligne qui a conduit à l'exécution du `except`. Pire encore, il se peut que des lignes que vous aviez prévues ne soient pas exécutées ! Donc gardez des choses simples dans un premier temps, comme par exemple tester les conversions de type ou vérifier qu'un fichier existe bien et que vous pouvez l'ouvrir.

close-box-adv

Il existe de nombreux types d'exception comme `RuntimeError`, `TypeError`, `NameError`, `IOError`, etc. Vous pouvez aller voir la [liste complète](https://docs.python.org/fr/3.7/library/exceptions.html#exceptions.TypeError) sur le site de Python. Nous avions déjà croisé des noms d'exception au chapitre 23 (*Avoir la classe avec les objets*) en regardant ce que contient le module `builtins`.

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

Un autre aspect très important que nous avons croisé au chapitre 23 est la possibilité de lever vous-même une exception avec le mot-clé `raise`. Nous avions vu le code suivant :


```
if valeur < 0:
    raise ValueError("Z'avez déjà vu une masse négative ? C'est nawak")
```

La ligne 2 lève une exception `ValueError` lorsque la variable `valeur` est négative. L'instruction `raise` est bien pratique lorsque vous souhaitez stopper l'exécution d'un programme si une variable ne se trouve pas dans le bon intervalle ou ne contient pas la bonne valeur. Vous avez sans doute compris maintenant pourquoi on parlait de « levée » d'exception... Pour les non anglophones, allez voir ce que signifie *raise* en anglais ;-) !

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

Si tout se passe bien, la page est téléchargée est stockée dans la variable `data`, puis ensuite enregistrée sur le disque dur.

Pour aller plus loin sur les exceptions, vous pouvez lire l'[excellente page](https://sametmax2.com/gestion-des-erreurs-en-python/) du blog impertinent et politiquement incorrect de Sam et Max.