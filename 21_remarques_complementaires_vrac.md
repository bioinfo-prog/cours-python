
## Shebang et /usr/bin/env python3

Lorsque l'on programme sur un système Unix (Mac OS X ou Linux par exemple), on peut exécuter directement un script Python, sans appeler explicitement la commande `python`.

Pour cela, deux opérations sont nécessaires :

1. Préciser la localisation de l'interpréteur Python en indiquant dans la première ligne du script :
    ```
    #! /usr/bin/env python
    ```
    Par exemple, si le script *test.py* contenait :
    ```
    print('Hello World !')
    ```
    il va alors contenir :
    ```
    #!/usr/bin/env python

    print('Hello World !')
    ```

2. Rendre le script Python exécutable en lançant l'instruction :
    ```
    $ chmod +x test.py
    ```

open-box-rem

La ligne `#! /usr/bin/env python` n'est pas considérée comme un commentaire
par Python, ni par une instruction Python d'ailleurs . Cette ligne a une signification
particulière pour le système d'exploitation Unix.

close-box-rem

Pour exécuter le script, il suffit alors de taper son nom précédé des deux caractères **./** (afin de préciser au *shell* où se trouve le script) :
```
$ ./test.py
Hello World !
```

open-box-def

Le [**shebang**](http://fr.wikipedia.org/wiki/Shebang) correspond aux caractères `#!` qui se trouvent au début de la première ligne du script `test`.

Le *shebang* est suivi du chemin complet du programme qui interprète le script ou du programme qui sait où se trouve l'interpréteur Python. Dans l'exemple précédent, c'est le programme `/usr/bin/env` qui indique où se trouve l'interpréteur Python.

close-box-def


## Passage d'arguments avec `*args` et `**kwargs`

Avant de lire cette rubrique, nous vous conseillons de bien relire et maîtriser la rubrique *Arguments positionnels et arguments par mot-clé* du chapitre 9 *Fonctions*.

Dans le chapitre 9, nous avons vu qu'il était nécessaire de passer à une fonction tous les arguments positionnels définis dans celle-ci. Il existe toutefois une astuce permettant de passer un nombre arbitraire d'arguments positionnels :

```
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

```
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

```
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

Enfin, il est possible de combiner des arguments positionnels avec `*args` et `**kwargs`, par exemple :

`def fct(a, b, *args, **kwargs):`

Dans un tel cas, il faudra obligatoirement passer les deux arguments `a` et `b` à la fonction, ensuite on pourra mettre un nombre arbitraire d'arguments positionnels (récupérés dans le tuple `args`), puis un nombre arbitraire d'arguments par mot-clé (récupérés dans le dictionnaire `kwargs`).

open-box-adv

Les noms `*args` et `**kwargs` sont des conventions en Python. Nous vous conseillons de respecter ces conventions pour faciliter la lecture de votre code par d'autres personnes.

close-box-adv

L'utilisation de la syntaxe `*args` et `**kwargs` est très classique dans le module *Tkinter* présenté dans le chapitre 20.

Enfin, il est possible d'utiliser ce mécanisme d'empaquetage / désempaquetage (*packing* / *unpacking*) dans l'autre sens :

```
>>> def fct(a, b, c):
...    print(a,b,c)
...
>>> t = (-5,6,7)
>>>
>>> fct(*t)
-5 6 7
```

Avec la syntaxe `*t` on désempaquette le tuple à la volée lors de l'appel à la fonction. Cela est aussi possible avec un dictionnaire : 

```
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


## Un peu de transformée de Fourier avec *NumPy*

La transformée de Fourier est très utilisée pour l'analyse de signaux, notamment lorsqu'on souhaite extraire des périodicités au sein d'un signal bruité. Le module *NumPy* possède la fonction `fft()` (dans le sous-module *fft*) permettant de calculer des transformées de Fourier.

Voici un petit exemple sur la fonction cosinus de laquelle on souhaite extraire la période à l'aide de la fonction `fft()` :
```
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
```
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
```
>>> import readline
>>> readline.read_history_file()
```
Vous pouvez accéder aux commandes de la session précédente avec la flèche du haut de votre clavier. D'abord les commandes `readline.read_history_file()` et `import readline` de la session actuelle, puis `print(a)`, `a = a + 11`, `a = 22`...
