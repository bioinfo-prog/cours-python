# Création de modules

## Pourquoi créer ses propres modules ?

Dans le chapitre 8, nous avons vu comment utiliser les modules existant dans python (comme *random*, *math*, etc). Nous avons vu par ailleurs les fonctions dans les chapitres 9 et 12 qui permettent de ré-utiliser une fraction de code plusieurs fois au sein d'un même programme sans avoir à dupliquer du code. On peut imaginer qu'une fonction bien écrite pourrait être judicieusement ré-utilisée dans un autre programme Python. C'est justement l'objet de la création de module, il s'agit d'y mettre un ensemble de fonctions que vous pourrez être amené à ré-utiliser souvent. En général les modules sont regroupés autour d'un thème précis, par exemple, on pourrait concevoir un module de gestion de séquences biologiques ou encore de gestion de fichiers PDB.

## Comment créer son propre module

En Python, la création de modules est très simple. Il vous suffit d'écrire un ensemble de fonctions (et/ou de constantes) dans un fichier, puis d'enregistrer ce dernier avec une extension `.py` (comme n'importe quel script Python). À titre d'exemple, nous allons créer un module simple que nous enregistrerons sous le nom `message.py`.

```
"""Module inutile qui affiche des messages :-)."""

DATE = 16092008


def bonjour(nom):
    """Dit Bonjour."""
    return "Bonjour " + nom


def ciao(nom):
    """Dit Ciao."""
    return "Ciao " + nom


def hello(nom):
    """Dit Hello."""
    return "Hello " + nom
```

Les chaînes de caractères entre triple guillemets en tête de module et dans chaque fonction sont facultatives mais elles jouent néanmoins un rôle essentiel dans la documentation du code.


## Utilisation de son propre module

Pour appeler une fonction ou une variable de ce module, il faut que le fichier `message.py` soit dans le répertoire courant (dans lequel on travaille) ou bien dans un répertoire listé par la variable d'environnement `PYTHONPATH`. Ensuite, il suffit d'importer le module et toutes ses fonctions (et variables) vous sont alors accessibles.

open-box-rem

Avec Mac OS X et Linux, il faut taper la commande suivante depuis un *shell* pour modifier la variable d'environnement `PYTHONPATH` :

`export PYTHONPATH=$PYTHONPATH:/chemin/vers/mes/super/modules/python`

Avec Windows, toujours depuis un *shell*, il faut taper la commande suivante :

`set PYTHONPATH=%PYTHONPATH%;C:\chemin\vers\mes\super\modules\python`

close-box-rem

L'importation du module se fait avec la commande `import message`. Notez que le fichier est bien enregistré avec une extension `.py` et pourtant on ne la précise pas lorsqu'on importe le module. Ensuite on peut utiliser les fonctions comme avec un module classique.
```
>>> import message
>>> message.hello("Joe")
'Hello Joe'
>>> message.ciao("Bill")
'Ciao Bill'
>>> message.bonjour("Monsieur")
'Bonjour Monsieur'
>>> message.DATE
16092008
```

open-box-rem

La première fois qu'un module est importé, Python crée un répertoire nommé `__pycache__` contenant un fichier avec une extension `.pyc` qui contient le [bytecode](https://docs.python.org/fr/3/glossary.html), c'est-à-dire le code précompilé du module.

close-box-rem


## Les *docstrings*

Lorsqu'on écrit un module, il est important de créer de la documentation pour expliquer ce que fait le module et comment utiliser chaque fonction. Les chaînes de caractères (entre triple guillemets) situés en début de module et sous chaque fonction sont là pour cela, on les appelle *docstrings*. Ces *docstrings* permettent notamment de fournir de l'aide lorsqu'on invoque la commande `help()` :
```
>>> help(message)

Help on module message:

NAME
    message - Module inutile qui affiche des messages :-).

FUNCTIONS
    bonjour(nom)
        Dit Bonjour.

    ciao(nom)
        Dit Ciao.

    hello(nom)
        Dit Hello.

DATA
    DATE = 16092008

FILE
    /home/pierre/message.py
```

open-box-rem

Pour quitter l'aide, pressez la touche `Q`.

close-box-rem

Vous remarquez que Python a généré automatiquement cette page d'aide, tout comme il est capable de le faire pour les modules internes à Python (*random*, *math*, etc) et ce grâce aux *docstrings*. Notez que l'on peut aussi appeler l'aide pour une seule fonction :
```
>>> help(message.ciao)

Help on function ciao in module message:

ciao(nom)
    Dit Ciao.
```

En résumé, les *docstrings* sont destinés aux utilisateurs du module. Leur but est donc différent des commentaires qui eux sont destinés à celui qui lit le code (pour en comprendre les subtilités). Une bonne *docstring* de fonction doit contenir tout ce dont un utilisateur a besoin pour utiliser cette fonction. Une liste minimale et non exhaustive serait :

- ce que fait la fonction,
- ce qu'elle prend en argument,
- ce qu'elle renvoie.

Pour en savoir plus sur les *docstrings* et comment les écrire, nous vous recommandons de lire le chapitre 15 *Bonnes pratiques en programmation Python*.


## Modules et fonctions

La visibilité des fonctions au sein des modules suit des règles simples :

- Les fonctions dans un module peuvent s'appeler les unes les autres.

- Les fonctions dans un module peuvent appeler des fonctions situées dans un autre module s'il a été préalablement importé avec la commande `import`.


## Module ou script ?

Vous avez remarqué que notre module `message` ne contient que des fonctions et une constante. Si on l'exécutait comme un script classique, cela ne renverrait rien :
```
$ python message.py
$
```
Cela s'explique par l'absence de programme principal, c'est-à-dire, de lignes de code que l'interpréteur exécute lorsqu'on lance le script.

À l'inverse, que se passe-t-il alors si on importe un script en tant que module alors qu'il contient un programme principal avec des lignes de code ? Prenons par exemple le code suivant enregistré dans un fichier `message2.py` :
```
"""Script de test."""


def bonjour(nom):
    """Dit Bonjour."""
    return "Bonjour " + nom


# programme principal
print(bonjour("Joe"))
```

Si on l'importe dans l'interpréteur, on obtient :
```
>>> import message2
Bonjour Joe
```

Ceci n'est pas le comportement voulu pour un module car on n'attend pas d'affichage particulier (par exemple la commande `import math` n'affiche rien dans l'interpréteur). Plus généralement, on s'attend à avoir des fonctions accessibles mais pas spécialement à des lignes de code exécutées.

Afin de pouvoir utiliser un code Python en tant que module ou en tant que script, il faut utiliser la structure suivante :
```
"""Script de test."""


def bonjour(nom):
    """Dit Bonjour."""
    return "Bonjour " + nom


if __name__ == '__main__':
    print(bonjour("Joe"))
```

La ligne 9 `if __name__ == '__main__':` indique à Python :

- Si le programme `message2.py` est exécuté en tant que script, le résultat du test `if` sera alors `True` et le bloc d'instructions correspondant (ligne 10) sera exécuté :
    ```
    $ python message2.py
    Bonjour Joe
    ```

- Si le programme `message2.py` est importé en tant que module, le résultat du test `if` sera alors `False` (et le bloc d'instructions correspondant ne sera pas exécuté) :
    ```
    >>> import message2
    >>>
    ```

Ce comportement est possible grâce à la gestion des espaces de noms par Python (voir le chapitre 19 *Avoir la classe avec les objets*).

Au delà de la commodité de pouvoir utiliser votre script en tant que programme ou en tant que module, cela présente l'avantage de bien voir où se situe le programme principal quand on lit le code. Ainsi, plus besoin d'ajouter un commentaire `# programme principal` comme nous vous l'avions suggéré dans les chapitres 9 *Fonctions* et 12 *Plus sur les fonctions*. L'utilisation de la ligne `if __name__ == '__main__':` est une bonne pratique que nous vous recommandons !


## Exercices

*Conseil* : pour cet exercice, écrivez un script dans un fichier, puis exécutez-le dans un *shell*.


### Module ADN

Dans le script `adn.py`, construisez un module qui va contenir les fonctions et variables suivantes.

- Fonction `seq_alea()` : prend en argument une taille de séquence sous forme d'un entier et renvoie une séquence d'ADN de la taille correspondante sous forme d'une chaîne de caractères.
- Fonction `prop_gc()` : prend en argument une séquence d'ADN sous forme d'une chaîne de caractères et renvoie la proportion en GC de la séquence sous forme d'un *float*. Nous vous rappelons que la proportion de GC s'obtient comme la somme des bases Guanine (G) et Cytosine (C) divisée par le nombre total de bases (A, T, C, G).
- Fonction `comp_inv()` : prend en argument une séquence d'ADN sous forme d'une chaîne de caractères et renvoie la séquence complémentaire inverse (aussi sous forme d'une chaîne de caractères).
- Fonction `lit_fasta()` : prend en argument un nom de fichier sous forme d'une chaîne de caractères et renvoie la séquence d'ADN lue dans le fichier sous forme d'une chaîne de caractère.
- La variable `BASE_COMP` : dictionnaire qui contient la complémentarité des bases d'ADN (`A`$\rightarrow$`T`, `T`$\rightarrow$`C`, `G`$\rightarrow$`C`...). Ce dictionnaire sera utilisé par la fonction `comp_inv()`.

Pour les fonctions `seq_alea()` et `comp_inv()`, n'hésitez pas à jeter un œil aux exercices correspondants dans le chapitre 11 *Plus sur les listes.*
