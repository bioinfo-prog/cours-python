# Variables

## Définition d'une variable

Une **variable** est une zone de la mémoire dans laquelle une **valeur** est stockée. Aux yeux du programmeur, cette variable est définie par un **nom**, alors que pour l'ordinateur, il s'agit en fait d'une adresse (*i.e.* une zone particulière de la mémoire).

En Python, la **déclaration** d'une variable et son **initialisation** (c'est-à-dire la première valeur que l'on va stocker dedans) se font en même temps. Pour vous en convaincre, testez les instructions suivantes après avoir lancé l'interpréteur :

    >>> x = 2
    >>> x
    2

Dans cet exemple, nous avons déclaré, puis initialisé la variable `x` avec la valeur 2. Notez bien qu'en réalité, il s'est passé plusieurs choses :

- Python a *deviné* que la variable était un entier. On dit que Python est un langage au *typage dynamique*.
- Python a alloué (*i.e.* réservé) l'espace en mémoire pour y accueillir un entier (chaque type de variable prend plus ou moins d'espace en mémoire), et a fait en sorte qu'on puisse retrouver la variable sous le nom `x`
- Python a assigné la valeur 2 à la variable `x`.

Dans certains autres langages, il faut coder ces différentes étapes une par une (en C par exemple). Python étant un langage dit de *haut niveau*, la simple instruction `x = 2` a suffi à réaliser les 3 étapes en une fois !

Ensuite, l'interpréteur nous a permis de connaître le contenu de la variable juste en tapant son nom. Retenez ceci car c'est une **spécificité de l'interpréteur Python**, très pratique pour chasser les erreurs (*debugging*) dans un programme. Par contre, la ligne d'un script Python qui contient seulement le nom d'une variable (sans aucune autre indication) n'affichera pas la valeur de la variable à l'écran (pour autant ceci reste valide et ne génèrera pas d'erreur).

Dernière chose, l'opérateur d'affectation `=` s'utilise dans un certain sens : par exemple `x = 2` signifie qu'on attribue la valeur située à droite de l'opérateur `=` (`2`) à la variable située à gauche (`x`). Certains autres langages comme **R** utilise les symboles `<-` pour rendre les choses plus explicites, par exemple `x <- 2`. 

Si on a `x = y - 3`, l'opération `y - 3` est d'abord évaluée et ensuite le résultat de cette opération est affecté à la variable `x`.

## Les types de variables

Le **type** d'une variable correspond à la nature de celle-ci. Les trois types principaux dont nous aurons besoin dans un premier temps sont les entiers (*integer* ou *int*), les réels (*float*) et les chaînes de caractères (*string* ou *str*). Bien sûr, il existe de nombreux autres types (par exemple, les nombres complexes), c'est d'ailleurs un des gros avantages de Python (si vous n'êtes pas effrayés, vous pouvez vous en rendre compte [ici](https://docs.python.org/3.6/library/stdtypes.html?highlight=type#)). 

Dans l'exemple précédent, nous avons stocké un nombre entier (*int*) dans la variable `x`, mais il est tout a fait possible de stocker des nombres réels (*float*), des chaînes de caractères (*string* ou *str*) ou plein d'autres types de variables que nous verrons par la suite :

    >>> y = 3.14
    >>> y
    3.14
    >>> a = "bonjour"
    >>> a
    'bonjour'
    >>> b = 'salut'
    >>> b
    'salut'
    >>> c = '''girafe'''
    >>> c
    'girafe'

Vous remarquez que Python reconnaît certains types de variable automatiquement (entier, réel). Par contre, pour une chaîne de caractères, il faut l'entourer de guillemets (simples, doubles voire trois guillemets successifs simples ou doubles) afin d'indiquer à Python le début et la fin de la chaîne.


## Nommage des variables

Le nom des variable en Python peut-être constitué de lettres minuscules (`a` à `z`), de lettres majuscules (`A` à `Z`), de nombres (`0` à `9`) ou du caractère souligné (`_`).

Néanmoins, un nom de variable ne doit pas débuter ni par un chiffre, ni par `_` et ne peut pas contenir de caractère accentué. Il faut absolument éviter d'utiliser un mot "réservé" par Python comme nom de variable (par exemple : `print`, `range`, `for`, `from`, etc.).

Python est sensible à la casse, ce qui signifie que les variables `TesT`, `test` ou `TEST` sont différentes. Enfin, vous ne pouvez pas utilisez d'espace dans un nom de variable.


## Opérations

### Opérations sur les types numériques

Les quatre opérations de base se font de manière simple sur les types numériques (nombres entiers et réels) :

    >>> x = 45
    >>> x + 2
    47
    >>> y = 2.5
    >>> x + y
    47.5
    >>> (x * 10) / y
    180.0

Remarquez toutefois que si vous mélangez les types entiers et réels, le résultat est renvoyé comme un réel (car ce type est plus général). Par ailleurs, l'utilisation de parenthèses permet de gérer les priorités.

open-box-warn

En Python 3, la division de deux entiers renvoie systématiquement un *float* :

```
>>> 3 / 4
0.75
```

close-box-warn

L'opérateur puissance utilise le symbole `**`. Pour obtenir le quotient et le reste d'une division entière (voir [ici](https://fr.wikipedia.org/wiki/Division_euclidienne) pour un petit rappel sur la division entière), on utilise respectivement les symboles `//` et  modulo `%` :

```
>>> 2**3
8
>>> 5 // 4
1
>>> 5 % 4
1
>>> 8 // 4
2
>>> 8 % 4
0
```

Les symboles `+`, `-`, `*`, `/`, `**`, `//` et `%` sont appelés **opérateurs**, car ils permettent de faire des opérations sur les variables.

### Opérations sur les chaînes de caractères

Pour les chaînes de caractères, deux opérations sont possibles, l'addition et la multiplication :

    >>> chaine = "Salut"
    >>> chaine
    'Salut'
    >>> chaine + " Python"
    'Salut Python'
    >>> chaine * 3
    'SalutSalutSalut'


L'opérateur d'addition `+` permet de concaténer (assembler) deux chaînes de caractères et l'opérateur de multiplication `*` permet de dupliquer plusieurs fois une chaîne.

**Attention** : Vous voyez que les opérateurs `+` et `*` se comportent différemment selon s'il s'agit d'entiers ou de chaînes de caractères : `2 + 2` est un addition, `'2' + '2'` est une concaténation. On appelle ce comportement **redéfinition des opérateurs**. Nous serons amenés à revoir cette notion dans le chapitre 18 sur les classes.

### Opérations illicites

Attention à ne pas faire d'opération illicite car vous obtiendriez un message d'erreur :

    >>> 'toto' + 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TypeError: cannot concatenate 'str' and 'int' objects

Notez que Python vous donne le maximum d'information dans son message d'erreur. Dans l'exemple précédent, il vous indique que vous ne pouvez pas mélanger des objets de type `str` (*string*, donc des chaînes de caractères) avec des objets de type `int` (donc des entiers), ce qui est assez logique.


## La fonction type()

Si vous ne vous souvenez plus du type d'une variable, utilisez la fonction `type()` qui vous le rappellera.

    >>> x = 2
    >>> type(x)
    <class 'int'>
    >>> y = 2.0
    >>> type(y)
    <class 'float'>
    >>> z = '2'
    >>> type(z)
    <class 'str'>

Faites bien attention, car pour Python, la valeur `2` (nombre entier) est différente de `2.0` (nombre réel), de même que `2` (nombre entier) est différent de `'2'` (chaîne de caractères). Nous verrons plus tard ce que signifie le mot *class*.

## Conversion de types

Dans tout langage de programmation, on est souvent amené à convertir les types, c'est-à-dire passer d'un type numérique à une chaîne de caractères ou vice-versa. En Python, rien de plus simple avec les fonctions `int()`, `float()` et `str()`. Pour vous en convaincre, regardez ces exemples :

    >>> i = 3
    >>> str(i)
    '3'
    >>> i = '456'
    >>> int(i)
    456
    >>> float(i)
    456.0
    >>> i = '3.1416'
    >>> float(i)
    3.1416

On verra au chapitre 7 sur les fichiers que ces conversions sont essentielles. En effet, lorsqu'on lit ou écrit des nombres dans un fichier, ils sont considérés comme du texte. 

Toute conversion d'une variable d'un type en un autre est appelé *casting* en anglais, il se peut que vous croisiez ce terme si vous allez consulter d'autres ressources.

## Note sur la division

Notez bien qu'en Python 3, la division de nombres entiers renvoie par défaut un nombre réel (*float*) :

    >>> x = 3 / 4
    >>> x
    0.75
    >>> type(x)
    <class 'float'>

Attention, ceci n'était pas le cas en Python 2. Pour en savoir plus sur ce point, vous pouvez consulter la section *Pour aller plus loin*


## Note sur le vocabulaire et la syntaxe

Nous avons vu dans ce chapitre la notion de **variable** qui est commune à tous les langages de programmation. Toutefois, Python est un langage dit **orienté objet**, il se peut que dans la suite du cours nous employions ce mot *objet* pour désigner une variable. Par exemple *variable de type entier* sera équivalent à un *objet de type entier*. Nous verrons ce que le mot *objet* signifie réellement plus tard (tout comme le mot *class*).

Par ailleurs, nous avons rencontré plusieurs fois des **fonctions** dans ce chapitre, avec `type(x)`, `int(x)`, `float(x)` et `str(x)`. Dans le chapitre 1 nous avons également vu la fonction `print()`. On reconnait qu'il s'agit d'une fonction au nom  - par exemple `type` - suivi de parenthèses `()`. En Python la syntaxe générale est `fonction()`. La variable `x` entre les parenthèses est appelé **argument** que l'on passe à la fonction. Dans `type(2)` c'est l'entier `2` qui est l'argument passé à la fonction. Pour l'instant on retiendra qu'une fonction est une sorte de *boite* à qui on passe un *argument* et qui renvoie un *résultat* ou plus généralement un objet. Par exemple, la fonction `type()` renvoie le type de la variable qu'on lui a passé en argument.

Si ces notions vous font peur, ne vous inquiétez pas, au fur et à mesure que vous avancerez dans le cours tout deviendra limpide.

