# Remarques complémentaires


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


## Différences Python 2 et Python 3

Python 3 est la version de Python qu'il faut utilisé.

Néanmoins, Python 2 a été employé pendant de nombreuses années par la communauté scientifique et vous serez certainement confrontés à un programme écrit en Python 2. Voici quelques éléments pour vous en sortir :

### La fonction print()

La fonction `print()` en Python 2 s'utilise sans parenthèse. Par exemple :
```
>>> print 12
12
>>> print "girafe"
girafe
```
Par contre en Python 3, si vous n'utilisez pas de parenthèse, Python vous renverra une erreur :
```
>>> print 12
  File "<stdin>", line 1
    print 12
           ^
SyntaxError: Missing parentheses in call to 'print'
```

### Division d'entiers

En Python 3, la division de deux entiers, se fait *naturellement*, c'est-à-dire que l'opérateur `/` renvoie systématiquement un *float*. Par exemple :
```
>>> 3 / 4
0.75
```
Il est également possible de réaliser une division entière avec l'opérateur `//` :
```
>>> 3 // 4
0
```
La division entière renvoie finalement la partie entière du nombre `0.75`, c'est à dire `0`.

Attention ! En Python 2, la division de deux entiers avec l'opérateur `/` correspond à la division entière, c'est-à-dire le résultat arrondi à l'entier inférieur. Par exemple :
```
>>> 3 / 5
0
>>> 4 / 3
1
```
Faites très attention à cet aspect si vous programmez encore en Python 2, c'est une source d'erreur récurrente.


### La fonction range()

En Python 3, la fonction `range()` est un générateur, c'est-à-dire que cette fonction va itérer sur le nombre entier donner en argument. On ne peut pas l'utiliser seule :
```
>>> range(3)
range(0, 3)
```

Lorsqu'on l'utilise dans une boucle `for`, `range(3)` va produire successivement les nombres `0`, puis `1` puis `2`. Par exemple :
```
>>> for i in range(3):
...     print(i)
...
0
1
2
```
En Python 2, la fonction `range()` renvoie une liste. Par exemple :
```
>>> range(3)
[0, 1, 2]
>>> range(2, 6)
[2, 3, 4, 5]
```
La création de liste avec `range()` était pratique mais très peu efficace en mémoire lorsque l'argument donné à `range()` était un grand nombre.

D'ailleurs la fonction `xrange()` est disponible en Python 2 pour faire la même chose que la fonction `range()` en Python 3. Attention, ne vous mélangez pas les pinceaux !
```
>>> range(3)
[0, 1, 2]
>>> xrange(3)
xrange(3)
```

open-box-rem

Pour générer une liste d'entiers avec la fonction `range()` en Python 3, vous avez vu dans le chapitre 4 *Listes* qu'il suffit de l'associer avec la fonction `list()`. Par exemple :
```
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

close-box-rem


### Encodage et utf-8

En Python 3, vous pouvez utiliser des caractères accentués dans les commentaires ou dans les chaîne de caractères.

Ce n'est pas le cas en Python 2. Si un caractère accentué est présent dans votre code, cela occasionnera une erreur de ce type lors de l'exécution de votre script :
```
SyntaxError: Non-ASCII character '\xc2' in file xxx on line yyy, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

Pour éviter ce genre de désagrément, ajoutez la ligne suivante en tout début de votre script :
```
# coding: utf-8
```

Si vous utilisez un shebang (voir rubrique précédente), il faudra mettre la ligne `# coding: utf-8` sur la deuxième ligne ([la position est importante](http://www.python.org/dev/peps/pep-0263/)) de votre script :
```
#! /usr/bin/env python
# coding: utf-8
```

open-box-rem

L'encodage utf-8 peut aussi être déclaré de cette manière :
```
# -*- coding: utf-8 -*-
```
mais c'est un peu plus long à écrire.

close-box-rem


## Liste de compréhension

Une manière originale et très puissante de générer des listes est la compréhension de listes. Pour plus de détails, consultez à ce sujet le site de [Python](http://www.python.org/dev/peps/pep-0202/) et celui de [Wikipédia](http://fr.wikipedia.org/wiki/Comprehension_de_liste).

Voici quelques exemples.

### Nombres pairs compris entre 0 et 30
```
>>> print([i for i in range() if i%2 == 0])
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
```

### Jeu sur la casse des mots d'une phrase
```
>>> message = "C'est sympa la BioInfo"
>>> msg_lst = message.split()
>>> print([[m.upper(), len(m)] for m in msg_lst])
[["C'EST", 5], ['SYMPA', 5], ['LA', 2], ['BIOINFO', 7]]
```

### Formatage d'une séquence avec 60 caractères par ligne

Exemple d'une séquence constituée de 150 alanines :
```
# exemple d'une séquence de 150 alanines
>>> seq = "A"*150
>>> width = 60
>>> seq_split = [seq[i:i+width] for i in range(0,len(seq),width)]
>>> print("\n".join(seq_split))
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

### Formatage fasta d'une séquence (avec la ligne de commentaire)

Exemple d'une séquence constituée de 150 alanines :
```
>>> com = "Séquence de 150 alanines"
>>> seq = "A"*150
>>> width = 60
>>> seq_split = [seq[i:i+width] for i in range(0,len(seq),width)]
>>> print(">"+com+"\n"+"\n".join(seq_split))
>séquence de 150 alanines
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

### Sélection des carbones alpha dans un fichier pdb

Exemple avec la structure de la [barstar](http://www.rcsb.org/pdb/explore.do?structureId=1BTA) :
```
>>> with open("1bta.pdb", "r") as f_pdb:
...     CA_lines = [line for line in f_pdb if line.startswith("ATOM")
                                           and line[12:16].strip() == "CA"]
...
>>> print(len(CA_lines))
89
```


## Gestion des erreurs

La gestion des erreurs permet d'éviter que votre programme plante en prévoyant vous même les sources d'erreurs éventuelles.

Voici un exemple dans lequel on demande à l'utilisateur d'entrer un nombre entier, puis on affiche ce nombre.
```
>>> nb = int(input("Entrez un nombre entier : "))
Entrez un nombre entier : 23
>>> print(nb)
23
```

La fonction `input()` demande à l'utilisateur de saisir une chaîne de caractères. Cette chaîne de caractères est ensuite transformée en nombre entier avec la fonction `int()`.

Si l'utilisateur ne rentre pas un nombre, voici  ce qui se passe :
```
>>> nb = int(input("Entrez un nombre entier : "))
Entrez un nombre entier : ATCG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ATCG'
```

L'erreur provient de la fonction `int()` qui n'a pas pu convertir la chaîne de caractères `"ATCG"` en nombre entier, ce qui est parfaitement normal.

Le jeu d'instructions `try` / `except` permet de tester l'exécution d'une commande et d'intervenir en cas d'erreur.
```
>>> try:
...     nb = int(input("Entrez un nombre entier : "))
... except:
...     print("Vous n'avez pas entré un nombre entier !")
...
Entrez un nombre entier : ATCG
Vous n'avez pas entré un nombre entier !
```

Dans cette exemple, l'erreur renvoyée par la fonction `int()` (qui ne peut pas convertir `"ATCG"` en nombre entier) est interceptée et déclenche l'affichage du message d'avertissement.

On peut ainsi redemander sans cesse un nombre entier à l'utilisateur, jusqu'à ce que celui-ci en rentre bien un.
```
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
Entrez un nombre : 55
Le nombre est 55
```
Notez que dans cet exemple, l'instruction `while True` est une boucle infinie car la condition `True` est toujours vérifiée. L'arrêt de cette boucle est alors forcé par la commande `break` lorsque l'utilisateur a effectivement entré un nombre entier.

La gestion des erreurs est très utile dès lors que des données extérieures entrent dans un programme Python, que ce soit directement par l'utilisateur (avec la fonction `input()`) ou par des fichiers.

Vous pouvez par exemple vérifier qu'un fichier a bien été ouvert.
```
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
```
>>> try:
...     nb = int(input("Entrez un nombre entier : "))
... except ValueError:
...     print("Vous n'avez pas entré un nombre entier !")
...
Entrez un nombre entier : ATCG
Vous n'avez pas entré un nombre entier !
```

Ici, on intercepte une erreur de type `ValueError`, ce qui correspond bien à un problème de conversion avec `int()`. Il existe d'autres types d'erreurs comme `RuntimeError`, `TypeError`, `NameError`, `IOError`, etc.

Enfin, on peut aussi être très précis dans le message d'erreur. Observez la fonction `download_page()` qui, avec le module `urllib`, télécharge un fichier sur internet.
```
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
            error = "Server failed {:d}".format(e.code)
    return page, error

data, error = download_page("https://files.rcsb.org/download/1BTA.pdb")

if error:
    print("Erreur rencontrée : {}".format(error))
else:
    with open("proteine.pdb", "w") as prot:
        prot.write(data.decode('utf-8'))
    print("Protéine enregistrée")
```

La variable `e` est une instance (un représentant) de l'erreur de type `IOError`. Certains de ces attributs sont testés avec la fonction `hasattr()` pour ainsi affiner le message renvoyé (ici contenu dans la variable `error`).

Si tout se passe bien, la page est téléchargée et stockée dans la variable `data`, puis ensuite enregistrée sur le disque dur.


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


## Ressources complémentaires

Pour compléter votre apprentissage de Python, nous vous conseillons les ressources suivantes :  

- Le livre *Apprendre à programmer avec Python 3* de Gérard Swinnen. Ce livre s’adresse aux débutants et propose une approche différente de la nôtre. Cet ouvrage est téléchargeable gratuitement sur le site de [Gérard Swinnen](http://www.inforef.be/swi/python.htm). Les éditions Eyrolles proposent également la version papier de cet ouvrage.
- Le livre *Apprendre à programmer en Python avec PyZo et Jupyter Notebook* de Bob Cordeau et Laurent Pointal, publié aux éditions Dunod. Une partie de cet ouvrage est téléchargeable gratuitement sur le site de [Laurent Pointal](https://perso.limsi.fr/pointal/python:courspython3).
- Le site [www.python.org](http://www.python.org). Il contient énormément d'informations et de liens sur Python. La page d'[index des modules](https://docs.python.org/fr/3/py-modindex.html) est particulièrement utile.
