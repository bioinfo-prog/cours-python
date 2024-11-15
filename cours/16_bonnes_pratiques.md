# Bonnes pratiques en programmation Python

Comme vous l'avez constaté dans tous les chapitres précédents, la syntaxe de Python est très permissive. Afin d'uniformiser l'écriture de code en Python, la communauté des développeurs Python recommande un certain nombre de règles afin qu'un code soit lisible. Lisible par quelqu'un d'autre, mais également, et surtout, par soi-même. Essayez de relire un code que vous avez écrit « rapidement » il y a un mois, six mois ou un an. Si le code ne fait que quelques lignes, il se peut que vous vous y retrouviez, mais s'il fait plusieurs dizaines, voire centaines de lignes, vous serez perdus.

Dans ce contexte, le créateur de Python, Guido van Rossum, part d'un constat simple : « *code is read much more often than it is written* » (« le code est plus souvent lu qu'écrit »). Avec l'expérience, vous vous rendrez compte que cela est parfaitement vrai. Alors, plus de temps à perdre, voyons en quoi consistent ces bonnes pratiques.

Plusieurs choses sont nécessaires pour écrire un code lisible : la syntaxe, l'organisation du code, le découpage en fonctions (et possiblement en classes, que nous verrons dans le chapitre 23 *Avoir la classe avec les objets*), mais souvent, aussi, le bon sens. Pour cela, les « PEP » peuvent nous aider.

open-box-def

Afin d'améliorer le langage Python, la communauté qui développe Python publie régulièrement des [*Python Enhancement Proposal*](https://www.python.org/dev/peps/) (PEP), suivi d'un numéro. Il s'agit de propositions concrètes pour améliorer le code, ajouter de nouvelles fonctionnalités, mais aussi des recommandations sur la manière d'utiliser Python, bien écrire du code, etc.

close-box-def

On va aborder dans ce chapitre sans doute la plus célèbre des PEP, à savoir la PEP 8, qui est incontournable lorsque l'on veut écrire du code Python correctement.

\index{pythonique}

open-box-def

On parle de code **pythonique** lorsque ce dernier respecte les règles d'écriture définies par la communauté Python, mais aussi les règles d'usage du langage.

close-box-def

\index{pep8@PEP 8}

## De la bonne syntaxe avec la PEP 8

La PEP 8 [*Style Guide for Python Code*](https://www.python.org/dev/peps/pep-0008/) est une des plus anciennes PEP (les numéros sont croissants avec le temps). Elle consiste en un nombre important de recommandations sur la syntaxe de Python. Il est vivement recommandé de lire la PEP 8 en entier au moins une fois pour avoir une bonne vue d'ensemble. On ne présentera ici qu'un rapide résumé de cette PEP 8.


### Indentation

\index{indentation}

On a vu que l'indentation est obligatoire en Python pour séparer les blocs d'instructions. Cela vient d'un constat simple : l'indentation améliore la lisibilité d'un code. La PEP 8 recommande
d'utiliser **quatre espaces** pour chaque niveau d'indentation. Nous vous recommandons de suivre impérativement cette règle.

open-box-warn

Afin de toujours utiliser cette règle des quatre espaces pour l'indentation, il est essentiel de régler correctement votre éditeur de texte. Consultez pour cela l'annexe *Installation de Python* disponible en [ligne](https://python.sdv.u-paris.fr/livre-dunod). Avant d'écrire la moindre ligne de code, faites en sorte que lorsque vous pressez la touche tabulation, cela ajoute quatre espaces (et non pas un caractère tabulation).

close-box-warn


### Importation des modules

Comme on l'a vu dans le chapitre 9 *Modules*, le chargement d'un module est réalisé avec l'instruction `import module` plutôt qu'avec `from module import *`.

Si on souhaite ensuite utiliser une fonction d'un module, la première syntaxe conduit à `module.fonction()`, ce qui rend explicite la provenance de la fonction. Avec la seconde syntaxe, il faudrait écrire `fonction()`, ce qui peut :

- mener à un conflit si une de vos fonctions a le même nom ;
- rendre difficile la recherche de documentation si on ne sait pas d'où vient la fonction, notamment si plusieurs modules sont chargés avec l'instruction  
    `from module import *`

Par ailleurs, la première syntaxe définit un « espace de noms » spécifique au module (voir le chapitre 24 *Avoir plus la classe avec les objets* (en ligne)).

Dans un script Python, on importe un module par ligne. D'abord les modules internes (classés par ordre alphabétique), c'est-à-dire les modules de base de Python, puis les modules externes (ceux que vous avez installés en plus), et enfin, les modules que vous avez créés.

Si le nom du module est trop long, on peut utiliser un alias. L'instruction `from` est tolérée si vous n'importez que quelques fonctions clairement identifiées.

En résumé :

```python
import module_interne_1
import module_interne_2
from module_interne_3 import fonction_spécifique

import module_externe_1
import module_externe_2_qui_a_un_nom_long as mod2

import module_cree_par_vous
```

### Règles de nommage

\index{nommage@nommage (de variable)}

Les noms de variables, de fonctions et de modules doivent être de la forme :

```python
ma_variable
fonction_test_27()
mon_module
```

c'est-à-dire en minuscules avec un caractère « souligné » (« tiret du bas », ou *underscore* en anglais) pour séparer les différents « mots » dans le nom.

\index{underscore@underscore (caractère)}

Les constantes sont écrites en majuscules :

```python
MA_CONSTANTE
VITESSE_LUMIERE
```

Les noms de classes (voir le chapitre 23 *Avoir la classe avec les objets*) et les exceptions (voir le chapitre 26 *Remarques complémentaires* (en ligne)) sont de la forme :

```python
MaClasse
MyException
```

open-box-rem

\index{snakecase@snake\_case}
\index{underscore@underscore (caractère)}


- Le style recommandé pour nommer les variables et les fonctions en Python est
appelé *snake_case*. Il est différent du *CamelCase* utilisé pour les noms des
classes et des exceptions.
- La variable `_` est habituellement employée pour stocker des valeurs qui ne seront pas utilisées par la suite. Par exemple, dans le cas d'une affectation multiple, on peut utiliser `_` pour stocker une valeur qui ne nous intéresse pas (voir chapitre 14 *Conteneurs*).

close-box-rem

Pensez à donner à vos variables des noms qui ont du sens. Évitez autant que possible les `a1`, `a2`, `i`, `truc`, `toto`... Les noms de variables à un caractère sont néanmoins autorisés pour les indices dans les boucles :

```python
>>> ma_liste = [1, 3, 5, 7, 9, 11]
>>> for i in range(len(ma_liste)):
...     print(ma_liste[i])
```

\index{pythonique}

Bien sûr, une écriture plus « pythonique » de l'exemple précédent permet de se débarrasser de l'indice `i` :

```python
>>> ma_liste = [1, 3, 5, 7, 9, 11]
>>> for entier in ma_liste:
...     print(entier)
```

Enfin, des noms de variable à une lettre peuvent être utilisés lorsque cela a un sens mathématique (par exemple, les noms `x`, `y` et `z` évoquent des coordonnées cartésiennes).


### Gestion des espaces

\index{espace}

La PEP 8 recommande d'entourer les opérateurs (`+`, `-`, `/`, `*`, `==`, `!=`, `>=`, `not`, `in`, `and`, `or`...) d'un espace avant et d'un espace après. Par exemple :

```python
# Code recommandé :
ma_variable = 3 + 7
mon_texte = "souris"
mon_texte == ma_variable
# Code non recommandé :
ma_variable=3+7
mon_texte="souris"
mon_texte== ma_variable
```

Il n'y a, par contre, pas d'espace à l'intérieur de crochets, d'accolades et de parenthèses :

```python
# Code recommandé :
ma_liste[1]
mon_dico{"clé"}
ma_fonction(argument)
# Code non recommandé :
ma_liste[ 1 ]
mon_dico{"clé" }
ma_fonction( argument )
```

Ni juste avant la parenthèse ouvrante d'une fonction ou le crochet ouvrant d'une liste ou d'un dictionnaire :

```python
# Code recommandé :
ma_liste[1]
mon_dico{"clé"}
ma_fonction(argument)
# Code non recommandé :
ma_liste [1]
mon_dico {"clé"}
ma_fonction (argument)
```

On met un espace après les caractères `:` et `,` (mais pas avant) :

```python
# Code recommandé :
ma_liste = [1, 2, 3]
mon_dico = {"clé1": "valeur1", "clé2": "valeur2"}
ma_fonction(argument1, argument2)
# Code non recommandé :
ma_liste = [1 , 2 ,3]
mon_dico = {"clé1" : "valeur1", "clé2":"valeur2"}
ma_fonction(argument1 ,argument2)
```

Par contre, pour les tranches de listes, on ne met pas d'espace autour du `:`

```python
ma_liste = [1, 3, 5, 7, 9, 1]
# Code recommandé :
ma_liste[1:3]
ma_liste[1:4:2]
ma_liste[::2]
# Code non recommandé :
ma_liste[1 : 3]
ma_liste[1: 4:2 ]
ma_liste[ : :2]
```

Enfin, on n'ajoute pas plusieurs espaces autour du `=` ou des autres opérateurs pour faire joli :

```python
# Code recommandé :
x1 = 1
x2 = 3
x_old = 5
# Code non recommandé :
x1    = 1
x2    = 3
x_old = 5
```


### Longueur de ligne

Une ligne de code ne doit pas dépasser 79 caractères, pour des raisons tant historiques que de lisibilité.

On a déjà vu dans le chapitre 1 *Introduction* que le caractère `\` permet de couper des lignes trop longues. Par exemple :

```python
>>> ma_variable = 3
>>> if ma_variable > 1 and ma_variable < 10 \
... and ma_variable % 2 == 1 and ma_variable % 3 == 0:
...     print(f"ma variable vaut {ma_variable}")
...
ma variable vaut 3
```

À l'intérieur de parenthèses, on peut revenir à la ligne sans utiliser le caractère `\`. C'est particulièrement utile pour préciser les arguments d'une fonction ou d'une méthode, lors de sa création ou lors de son utilisation :

```python
>>> def ma_fonction(argument_1, argument_2,
...                 argument_3, argument_4):
...     return argument_1 + argument_2
...
>>> ma_fonction("texte très long", "tigre",
...             "singe", "souris")
'texte très longtigre'
```

Les parenthèses sont également très pratiques, pour répartir sur plusieurs lignes une chaîne de caractères qui sera ensuite affichée sur une seule ligne :

```python
>>> print("ATGCGTACAGTATCGATAAC"
...       "ATGACTGCTACGATCGGATA"
...       "CGGGTAACGCCATGTACATT")
ATGCGTACAGTATCGATAACATGACTGCTACGATCGGATACGGGTAACGCCATGTACATT
```

Notez qu'il n'y a pas d'opérateur `+` pour concaténer les trois chaînes de caractères, et que celles-ci ne sont pas séparées par des virgules. À partir du moment où elles sont entre parenthèses, Python les concatène automatiquement.

On peut aussi utiliser les parenthèses pour évaluer un expression trop longue :

```python
>>> ma_variable = 3
>>> if (ma_variable > 1 and ma_variable < 10
... and ma_variable % 2 == 1 and ma_variable % 3 == 0):
...     print(f"ma variable vaut {ma_variable}")
...
ma variable vaut 3
```

open-box-rem

\index{method chaining}

Les parenthèses sont aussi très utiles lorsqu'on a besoin d’enchaîner des méthodes les unes à la suite des autres. Cette technique du *method chaining* a été introduite dans le chapitre 11 *Plus sur les chaînes de caractères* et sera très utilisée dans le chapitre 22 *Module Pandas*.

close-box-rem

Enfin, il est possible de créer des listes ou des dictionnaires sur plusieurs lignes, en sautant une ligne après une virgule :

```python
>>> ma_liste = [1, 2, 3,
...             4, 5, 6,
...             7, 8, 9]
>>> mon_dico = {"clé1": 13,
...             "clé2": 42,
...             "clé3": -10}
```


### Lignes vides

Dans un script, les lignes vides sont utiles pour séparer visuellement les différentes parties du code.

Il est recommandé de laisser deux lignes vides avant la définition d'une fonction ou d'une classe, et de laisser une seule ligne vide avant la définition d'une méthode (dans une classe).

On peut aussi laisser une ligne vide dans le corps d'une fonction pour séparer les sections logiques de la fonction, mais cela est à utiliser avec parcimonie.


### Commentaires

\index{commentaire}

Les commentaires débutent toujours par le symbole `#` suivi d'un espace. Ils fournissent des explications sur l'utilité du code et permettent de comprendre son fonctionnement.

Les commentaires sont sur le même niveau d'indentation que le code qu'ils commentent. Les commentaires sont constitués de phrases complètes, avec une majuscule au début (sauf si le premier mot est une variable qui s'écrit sans majuscule) et un point à la fin.

La PEP 8 recommande d'écrire les commentaires en anglais, sauf si vous êtes absolument certains que votre code ne sera lu que par des francophones. Dans la mesure où vous allez souvent développer des programmes scientifiques, nous vous conseillons d'écrire vos commentaires en anglais.

Soyez également cohérent entre la langue utilisée pour les commentaires et la langue utilisée pour nommer les variables. Pour un programme scientifique, les commentaires et les noms de variables sont en anglais. Ainsi `ma_liste` deviendra `my_list` et `ma_fonction` deviendra `my_function` (par exemple).

Les commentaires qui suivent le code sur la même ligne sont à éviter le plus possible et doivent être séparés du code par au moins deux espaces :

```python
var_x = number / total * 100   # My useful comment.
```

open-box-rem

La PEP 8 [ne fournit pas de recommandation](https://peps.python.org/pep-0008/#string-quotes) quant à l'usage de guillemets simples ou de guillemets doubles pour déclarer une chaîne de caractères.

```python
>>> var_1 = "Ma chaîne de caractères"
>>> var_1
'Ma chaîne de caractères'
>>> var_2 = 'Ma chaîne de caractères'
>>> var_2
'Ma chaîne de caractères'
>>> var_1 == var_2
True
```

Vous constatez dans l'exemple ci-dessus que, pour Python, les guillemets simples et doubles sont équivalents.
Nous vous conseillons cependant d'utiliser les **guillemets doubles** car ceux-ci sont, de notre point de vue, plus lisibles.

close-box-rem


## Les *docstrings* et la PEP 257

\index{PEP 257}
\index{docstrings}

Les *docstrings*, que l'on pourrait traduire par « chaînes de documentation » en français, sont un élément essentiel des programmes Python, comme on l'a vu au chapitre 15 *Création de modules*. À nouveau, les développeurs de Python ont émis des recommandations dans la PEP 8, et plus exhaustivement dans la [PEP 257](https://www.python.org/dev/peps/pep-0257/), sur la manière de rédiger correctement les *docstrings*. En voici un résumé succinct.


### Les principales règles

De manière générale, écrivez des *docstrings* pour les modules, les fonctions, les classes et les méthodes que vous développez.

Lorsque l'explication est courte et compacte, comme dans certaines fonctions ou méthodes simples, utilisez des *docstrings* d'une ligne :

```python
"""Docstring simple d'une ligne se finissant par un point."""
```

Lorsque vous avez besoin de décrire plus en détail un module, une fonction, une classe ou une méthode, utilisez une *docstring* sur plusieurs lignes :

```python
"""Docstring de plusieurs lignes, la première ligne est un résumé.

Après avoir sauté une ligne, on décrit les détails de cette docstring.
On termine la docstring avec les triples guillemets 
sur la ligne suivante.
"""
```

open-box-rem

La PEP 257 recommande d'écrire des *docstrings* avec trois doubles guillemets, c'est-à-dire :

`"""Ceci est une docstring recommandée."""`

mais pas :

`'''Ceci n'est pas une docstring recommandée.'''`

close-box-rem

Comme indiqué dans le chapitre 15 *Création de modules*, n'oubliez pas que les *docstrings* sont destinées aux utilisateurs des modules, fonctions, méthodes et classes que vous avez développés. Les éléments essentiels pour les fonctions et les méthodes sont :

1. ce que fait la fonction ou la méthode,
2. ce qu'elle prend en argument,
3. ce qu'elle renvoie.

Pour les modules et les classes, on ajoute également des informations générales sur leur fonctionnement.

Pour autant, la PEP 257 ne dit pas explicitement comment organiser les *docstrings* pour les fonctions et les méthodes. Pour répondre à ce besoin, deux solutions ont émergées :

- la solution Google avec le [*Google Style Python Docstrings*](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html),
- la solution *NumPy* avec le [*NumPy Style Python Docstrings*](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html). *NumPy* est un module complémentaire à Python, très utilisé en analyse de données et dont on parlera dans le chapitre 20.


### Un exemple concret

On illustre ici la solution de *docstrings* *NumPy* pour des raisons de goût personnel. Sentez-vous libre d'explorer la proposition de Google.

Voici un exemple pour une fonction qui prend en argument deux entiers et qui renvoie leur produit :

```python
def multiplie_nombres(nombre1, nombre2):
    """Multiplication de deux nombres entiers.

    Cette fonction ne sert pas à grand chose.

    Parameters
    ----------
    nombre1 : int
        Le premier nombre entier.
    nombre2 : int
        Le second nombre entier,
        très important pour cette fonction.

    Returns
    -------
    int
        Le produit des deux nombres.
    """
    return nombre1 * nombre2
```

- **Lignes 6 et 7.** La section `Parameters` précise les paramètres de la fonction. Les tirets sur la ligne 7 soulignent le nom de la section pour la rendre visible.
- **Lignes 8 et 9.** On indique le nom et le type du paramètre, séparés par le caractère deux-points. Le type n'est pas obligatoire. En dessous, on indique une description du paramètre en question. La description est indentée.
- **Lignes 10 à 12.** Même chose pour le second paramètre. La description du paramètre peut s'étaler sur plusieurs lignes.
- **Lignes 14 et 15.** La section `Returns` indique ce qui est renvoyé par la fonction (le cas échéant).
- **Lignes 16 et 17.** La mention du type renvoyé est obligatoire. En dessous, on indique une description de ce qui est renvoyé par la fonction. Cette description est aussi indentée.

open-box-warn

L'être humain a une fâcheuse tendance à la procrastination (le fameux « Bah je le ferai demain...») et écrire de la documentation peut être un sérieux motif de procrastination. Soyez vigilant sur ce point, et rédigez vos *docstrings* au moment où vous écrivez vos modules, fonctions, classes ou méthodes. Passer une journée (voire plusieurs) à écrire les *docstrings* d'un gros projet est particulièrement pénible. Croyez-nous !

close-box-warn


## Outils de contrôle qualité du code

Pour évaluer la qualité d'un code Python, c'est-à-dire sa conformité avec les recommandations de la PEP 8 et de la PEP 257, on peut utiliser les outils `pycodestyle`, `pydocstyle` et `pylint`.

\index{pycodestyle}
\index{pydocstyle}
\index{pylint}

Ces outils ne sont fournis dans l'installation de base de Python et doivent être installés sur votre machine. Avec la distribution Miniconda, cette étape d'installation se résume à une ligne de commande :

```bash
$ conda install -c conda-forge pycodestyle pydocstyle pylint
```

open-box-def

Les outils `pycodestyle`, `pydocstyle` et `pylint` sont des **linters**, c'est-à-dire des programmes qui vont chercher les sources potentielles d'erreurs dans un code informatique. Ces erreurs peuvent être des erreurs de style (PEP 8 et 257) ou des erreurs logiques (manipulation d'une variable, chargement de module).

close-box-def

Voici le contenu du script [`script_quality_not_ok.py`](https://python.sdv.u-paris.fr/data-files/script_quality_not_ok.py) que nous allons analyser par la suite :

```python
"""Un script de multiplication.
"""

import os

def Multiplie_nombres(nombre1,nombre2 ):
    """Multiplication de deux nombres entiers
    Cette fonction ne sert pas à grand chose.

    Parameters
    ----------
    nombre1 : int
        Le premier nombre entier.
    nombre2 : int
        Le second nombre entier.
        Très utile.

    Returns
    -------
    int
        Le produit des deux nombres.

    """
    return nombre1 *nombre2


if __name__ == "__main__":
    print(f"2 x 3 = {Multiplie_nombres(2, 3)}")
    print (f"4 x 5 = {Multiplie_nombres(4, 5)}")

```

Ce script est d'ailleurs parfaitement fonctionnel :

```bash
$ python script_quality_not_ok.py
2 x 3 = 6
4 x 5 = 20
```

On va tout d'abord vérifier la conformité avec la PEP 8 grâce à l'outil `pycodestyle` :

```bash
$ pycodestyle script_quality_not_ok.py
script_quality_not_ok.py:6:1: E302 expected 2 blank lines, found 1
script_quality_not_ok.py:6:30: E231 missing whitespace after ','
script_quality_not_ok.py:6:38: E202 whitespace before ')'
script_quality_not_ok.py:26:21: E225 missing whitespace around operator
script_quality_not_ok.py:31:10: E211 whitespace before '('
```

- **Ligne 2.** Le bloc `script_quality_not_ok.py:6:1:` désigne le nom du script (`script_quality_not_ok.py`), le numéro de la ligne (6) et le numéro de la colonne (1) où se trouve la non-conformité avec la PEP 8. Ensuite, `pycodestyle` fournit un code et un message explicatif. Ici, il faut deux lignes vides avant la fonction `Multiplie_nombres()`.
- **Ligne 3.** Il manque un espace après la virgule qui sépare les arguments `nombre1` et `nombre2` dans la définition de la fonction `Multiplie_nombres()` à la ligne 6 (colonne 30) du script.
- **Ligne 4.** Il y un espace de trop après le second argument `nombre2` dans la définition de la fonction `Multiplie_nombres()` à la ligne 6 (colonne 38) du script.
- **Ligne 5.** Il manque un espace après l'opérateur `*` à la ligne 26 (colonne 21) du script.
- **Ligne 6.** Il y a un espace de trop entre `print` et `(` à la ligne 31 (colonne 10) du script.

Assez curieusement, `pycodestyle` n'a pas détecté que le nom de la fonction `Multiplie_nombres()` ne respecte pas la convention de nommage (pas de majuscule).


Ensuite, l'outil `pydocstyle` va vérifier la conformité avec la PEP 257 et s'intéresser particulièrement aux *docstrings* :

```bash
$ pydocstyle script_quality_not_ok.py
script_quality_not_ok.py:1 at module level:
        D200: One-line docstring should fit on one line with quotes (found 2)
script_quality_not_ok.py:7 in public function `Multiplie_nombres`:
        D205: 1 blank line required between summary line and description (found 0)
script_quality_not_ok.py:7 in public function `Multiplie_nombres`:
        D400: First line should end with a period (not 's')
```

- **Lignes 2 et 3.** `pydocstyle` indique que la *docstring* à la ligne 1 du script est sur deux lignes, alors qu'elle devrait être sur une seule ligne.
- **Lignes 4 et 5.** Dans la *docstring* de la fonction `Multiplie_nombres()` (ligne 7 du script), il manque une ligne vide entre la ligne résumé et la description plus complète.
- **Lignes 6 et 7.** Dans la *docstring* de la fonction `Multiplie_nombres()` (ligne 7 du script), il manque un point à la fin de la première ligne.


Les outils `pycodestyle` et `pydocstyle` vont simplement vérifier la conformité aux PEP 8 et 257. L'outil `pylint` va lui aussi vérifier une partie de ces règles mais il va également essayer de comprendre le contexte du code et proposer des éléments d'amélioration. Par exemple :

```bash
$ pylint script_quality_not_ok.py
************* Module script_quality_not_ok
script_quality_not_ok.py:6:0: C0103: Function name "Multiplie_nombres" 
doesn't conform to snake_case naming style (invalid-name)
script_quality_not_ok.py:4:0: W0611: Unused import os (unused-import)

------------------------------------------------------------------
Your code has been rated at 6.67/10
```  

- **Lignes 3 et 4.** `pylint` indique que nom de la fonction `Multiplie_nombres()` ne respecte pas la convention PEP 8 (ligne 6 du script).
- **Ligne 5.** Le module `os` est chargé mais pas utilisé (ligne 4 du script).
- **Ligne 8.** `pylint` produit également une note sur 10. Ne soyez pas surpris si cette note est très basse (voire négative) la première fois que vous analysez votre script avec `pylint`. Cet outil fournit de nombreuses suggestions d'amélioration et la note attribuée à votre script devrait rapidement augmenter. Pour autant, la note de 10 est parfois difficile à obtenir. Ne soyez pas trop exigeant.

Une version améliorée du script précédent est disponible [en ligne](https://python.sdv.u-paris.fr/data-files/script_quality_ok.py).


## Outil de formatage automatique du code

\index{black}

Se souvenir de toutes les règles PEP 8 est fastidieux. Il existe des outils pour formater automatiquement le code Python pour qu'il soit conforme à la PEP 8. L'outil le plus connu est `black`.

Cet outil n'est pas fourni dans l’installation de base de Python et doit être installé
sur votre machine. Avec la distribution Miniconda, cette étape d’installation se résume à
une ligne de commande :

```bash
$ conda install -c conda-forge black
```

Voici un exemple d'utilisation :

```bash
$ black script_quality_not_ok.py
reformatted script_quality_not_ok.py

All done!
1 file reformatted.
```

Le script `script_quality_not_ok.py` a été modifié pour être conforme à la PEP 8, ce qu'on peut vérifier avec `pycodestyle` :

```bash
$ pycodestyle script_quality_not_ok.py
```

qui ne renvoie aucune erreur.

`black` peut modifier votre code de manière significative. Il est donc recommandé de l'utiliser avec l'option `--diff` au préalable pour afficher les modifications apportées. Par exemple, avec le programme `script_quality_not_ok.py` qui n'aurait pas été modifié :

```bash
$ black --diff script_quality_not_ok.py 
--- script_quality_not_ok.py	2024-02-05 12:07:04.851491+00:00
+++ script_quality_not_ok.py	2024-02-05 12:07:10.418009+00:00
@@ -1,11 +1,12 @@
 """Un script de multiplication.
 """
 
 import os
 
-def Multiplie_nombres(nombre1,nombre2 ):
+
+def Multiplie_nombres(nombre1, nombre2):
[...]
```

open-box-adv

`black` est très pratique. N'hésitez pas à l'utiliser pour formater automatiquement votre code.

close-box-adv


open-box-warn

- `black` ne fait qu'une entorse à la PEP 8 : il autorise des longueurs de lignes jusqu'à 88 caractères. Si vous souhaitez respecter strictement la PEP 8, utilisez l'option `--line-length 79`.
- `black` se limite à la PEP 8. Il ne vérifie pas la conformité avec la PEP 257 ni la qualité du code (imports inutiles, etc.). Utilisez toujours `pydocstyle` et `pylint` en complément.

close-box-warn


## Organisation du code

Il est important de toujours structurer son code de la même manière. Ainsi, on sait tout de suite où trouver l'information et un autre programmeur pourra s'y retrouver. Voici un exemple de code avec les différents éléments dans le bon ordre :

```python
"""Docstring d'une ligne décrivant brièvement ce que fait le programme.

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Johny B Good", "Hubert de la Pâte Feuilletée")
__contact__ = ("johny@bgood.us", "hub@pate.feuilletee.fr")
__copyright__ = "MIT"
__date__ = "2030-01-01"
__version__ = "1.2.3"

import module_interne
import module_interne_2 as mod2

import module_externe

import my_module

UNE_CONSTANTE = valeur


def une_fonction_complexe(arg1, arg2, arg3):
    """Résumé de la docstring décrivant la fonction.

    Description détaillée.
    """
    [...]
    return une_chose


def une_fonction_simple(arg1, arg2):
    """Docstring d'une ligne décrivant la fonction."""
    [...]
    return autre_chose


if __name__ == "__main__":
    # Ici débute le programme principal.
    [...]
```

- **Lignes 1 à 9.** Cette *docstring* décrit globalement le script. Cette *docstring* (ainsi que les autres) seront visibles si on importe le script en tant que module, puis en invoquant la commande `help()` (voir chapitre 15 *Création de modules*).
- **Lignes 11 à 15.** On définit ici un certain nombre de variables avec des doubles *underscores* donnant quelques informations sur la version du script, les auteurs, etc. Il s'agit de métadonnées que la commande `help()` pourra afficher. Ces métadonnées sont utiles lorsque le code est distribué à la communauté.
- **Lignes 17 à 22.** Importation des modules. D'abord les modules internes à Python (fournis en standard), puis les modules externes (ceux qu'il faut installer en plus), puis les modules créés localement. Un module par ligne.
- **Ligne 24.** Définition des constantes. Le nom des constantes est en majuscule.
- **Lignes 27 à 39.** Définition des fonctions. Avant chaque fonction, on laisse deux lignes vides.
- **Lignes 42 à 44.** On écrit le programme principal. Le test ligne 42 n'est vrai que si le script est utilisé en tant que programme.

## Conseils sur la conception d'un script

Voici quelques conseils pour vous aider à concevoir un script Python.

- **Réfléchissez** avec un papier, un crayon... et un cerveau (voire même plusieurs) ! Reformulez avec vos propres mots les consignes qui vous ont été données. Dessinez des schémas si cela vous aide.
- **Découpez en fonctions** chaque élément de votre programme. Vous pourrez ainsi tester chaque élément indépendamment du reste. Pensez à écrire les *docstrings* en même temps que vous écrivez vos fonctions.
- **Documentez-vous**. L'algorithme dont vous avez besoin existe-t-il déjà dans un autre module ? De quels outils mathématiques avez-vous besoin dans votre algorithme ?
- Quand l'algorithme est complexe, **commentez votre code** pour expliquer votre raisonnement. Utiliser des fonctions (ou méthodes) encore plus petites peut aussi être une solution.
- Utilisez des **noms de variables explicites**, qui signifient quelque chose. En lisant votre code, on doit comprendre ce que vous faites. Choisir des noms de variables pertinents permet aussi de réduire les commentaires.
- Quand vous construisez une structure de données complexe (par exemple une liste de dictionnaires contenant d'autres objets), **documentez** l'organisation de cette structure de données avec un exemple simple.
- Si vous créez ou manipulez une entité cohérente avec des propriétés propres, essayez de construire une **classe**. Reportez-vous, pour cela, au chapitre 23 *Avoir la classe avec les objets*.
- **Testez** votre code sur un **petit jeu de données**, pour comprendre rapidement ce qui se passe et corriger d'éventuelles erreurs. Par exemple, une séquence d'ADN de 1 000 bases est plus facile à manipuler que le génome humain ($3 \times 10^9 \textrm{ bases}$) !
- Lorsque votre programme « plante », **lisez le message d'erreur**. Python tente de vous expliquer ce qui ne va pas. Le numéro de la ligne qui pose problème est aussi indiqué.
- **Discutez avec des gens**. Faites tester votre programme par d'autres. Les instructions d'utilisation sont-elles claires ?
- Enfin, si vous **distribuez votre code** :
    + Rédigez une **documentation** claire.
    + **Testez** votre programme (jetez un œil aux [tests unitaires](https://fr.wikipedia.org/wiki/Test_unitaire)).
    + Précisez une **licence** d'utilisation (voir le site [*Choose an open source license*](https://choosealicense.com/)).


## Pour terminer : la PEP 20

\index{PEP 20}

La PEP 20 est une sorte de réflexion philosophique avec des phrases simples qui devraient guider tout programmeur. Comme les développeurs de Python ne manque pas d'humour, celle-ci est accessible sous la forme d'un « œuf de Pâques » (*easter egg*, en anglais) ou encore « fonctionnalité cachée d'un programme » en important un module nommé `this` :

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Et si l'aventure et les *easter eggs* vous plaisent, testez également la commande

```python
>>> import antigravity
```

Il vous faudra un navigateur et une connexion internet.

open-box-more

- L'article [*Python Code Quality: Tools & Best Practices*](https://realpython.com/python-code-quality/)
du site *Real Python* est une ressource intéressante pour explorer plus en détail la notion de qualité
pour un code Python. De nombreux *linters* y sont présentés.

- Les articles [*Assimilez les bonnes pratiques de la PEP 8*](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8) du site *OpenClassrooms* et [*Structuring Python Programs*](https://realpython.com/python-program-structure/)
du site *Real Python* rappellent les règles d'écriture et les bonnes pratiques vues dans ce chapitre.

close-box-more
