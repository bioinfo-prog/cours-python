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

Tout ce que nous avons vu avec les *f-strings* sur la manière de formater l'affichage d'une variable (après les `:` au sein des accolades) est identique avec la méthode `.format()`. Par exemple `{:.2f}`, `{:0>6d}`, `{:.6e}`, etc., fonctionneront de la même manière. La différence notable est qu'on ne met pas directement le nom de la variable au sein des accolades. Comme pour l'opérateur `%`, c'est l'emplacement dans les arguments passés à la méthode `.format()` qui dicte quelle variable doit être remplacée. Par exemple, dans `"{} {} {}".format(bidule, machin, truc)`, les premières accolades remplaceront la variable `bidule`, les deuxièmes la variable `machin`, les troisièmes la variable `truc`.

Le formatage avec la méthode `.format()` se rapproche de la syntaxe des *f-strings* (accolades, deux-points), mais présente l'inconvénient -- comme avec l'opérateur `%` -- de devoir mettre la liste des variables tout à la fin, alourdissant ainsi la syntaxe. En effet, dans l'exemple avec la proportion de GC, la ligne équivalente avec une *f-string* apparait tout de même plus simple à lire :

```python
>>> print(f"On a {nb_G} G et {nb_C} C -> prop GC = {prop_GC:.2f}")
On a 4500 G et 2575 C -> prop GC = 0.48
```

open-box-adv

Pour conclure, ces deux anciennes façons de formater une chaîne de caractères avec l'opérateur `%` ou la méthode `.format()` vous sont présentées à titre d'information. La première avec l'opérateur `%` est clairement déconseillée. La deuxième avec la méthode `.format()` est encore tout à fait valable. Si vous débutez Python, nous vous conseillons fortement d'apprendre et d'utiliser les *f-strings*. C'est ce que vous rencontrerez dans la suite de ce cours. Si vous connaissez déjà Python et que vous utilisez la méthode `.format()`, nous vous conseillons de passer aux *f-strings*. Depuis que nous les avons découvertes, aucun retour n'est envisageable pour nous tant elles sont puissantes et plus claires à utiliser ! 

Enfin, si vous souhaitez aller plus loin, voici deux articles (en anglais) très bien faits sur le site *RealPython*: sur l'[écriture formatée](https://realpython.com/python-string-formatting) et sur les [*f-strings*](https://realpython.com/python-f-strings/)

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
- Pa ailleurs, ne mettez pas trop de lignes dans le bloc du `try`. Dans un tel cas, il peut être très pénible de trouver la ligne qui a conduit à l'exécution du `except`. Pire encore, il se peut que des lignes que vous aviez prévues ne soient pas exécutées ! Donc gardez des choses simples dans un premier temps, comme par exemple tester les conversions de type ou vérifier qu'un fichier existe bien et que vous pouvez l'ouvrir.

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

Il est possible de combiner des arguments positionnels avec `*args` et `**kwargs`, par exemple :

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
