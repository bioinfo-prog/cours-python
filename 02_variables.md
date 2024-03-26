# Variables

## Définition et création

open-box-def 

Une **variable**\index{variable} est une zone de la mémoire de l'ordinateur dans laquelle une **valeur** est stockée. Aux yeux du programmeur, cette variable est définie par un **nom**, alors que pour l'ordinateur, il s'agit en fait d'une adresse, c'est-à-dire d'une zone particulière de la mémoire.

close-box-def

En Python, la **déclaration**\index{declaration@déclaration (de variable)} d'une variable et son **initialisation**\index{initialisation@initialisation (de variable)} (c'est-à-dire la première valeur que l'on va stocker dedans) se font en même temps. Pour vous en convaincre, testez les instructions suivantes après avoir lancé l'interpréteur :

```python
>>> x = 2
>>> x
2
```

**Ligne 1**. Dans cet exemple, nous avons déclaré, puis initialisé la variable `x` avec la valeur 2. Notez bien qu'en réalité, il s'est passé plusieurs choses :

- Python a « deviné » que la variable était un entier. On dit que Python est un langage au **typage dynamique** \index{typage dynamique@typage dynamique}.
- Python a alloué (réservé) l'espace en mémoire pour y accueillir un entier. Chaque type de variable prend plus ou moins d'espace en mémoire. Python a aussi fait en sorte qu'on puisse retrouver la variable sous le nom `x`.
- Enfin, Python a assigné la valeur 2 à la variable `x`.

Dans d'autres langages (en C par exemple), il faut coder ces différentes étapes une par une. Python étant un langage dit de *haut niveau*, la simple instruction `x = 2` a suffi à réaliser les trois étapes en une fois !

**Lignes 2 et 3**. L'interpréteur nous a permis de connaître le contenu de la variable juste en tapant son nom. Retenez ceci car c'est une **spécificité de l'interpréteur Python**, très pratique pour chasser (*debugger*) les erreurs dans un programme. En revanche, la ligne d'un script Python qui contient seulement le nom d'une variable (sans aucune autre indication) n'affichera pas la valeur de la variable à l'écran lors de l'exécution (pour autant, cette instruction reste valide et ne générera pas d'erreur).

Depuis la version 3.10, l'interpréteur Python a amélioré ses messages d'erreur. Il est ainsi capable de suggérer des noms de variables existants lorsqu'on fait une faute de frappe :

```python
>>> voyelles = "aeiouy"
>>> voyelle
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'voyelle' is not defined. Did you mean: 'voyelles'?
```

Si le mot qu'on tape n'est pas très éloigné, cela fonctionne également lorsqu'on se trompe à différents endroits du mot !

```python
pharmacie = "vente de médicaments"
>>> farmacia
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'farmacia' is not defined. Did you mean: 'pharmacie'?
```

Revenons sur le signe `=` ci-dessus.

open-box-def

Le symbole `=` est appelé **opérateur d'affectation**. Il permet d'assigner une valeur à une variable en Python. Cet opérateur s'utilise toujours de la droite vers la gauche. Par exemple, dans l'instruction  `x = 2` ci-dessus, Python attribue la valeur située à droite (ici, `2`) à la variable située à gauche (ici, `x`). D'autres langages de programmation comme *R* utilisent les symboles `<-` pour rendre l'affectation d'une variable plus explicite, par exemple `x <- 2`. 

close-box-def

Voici d'autres cas de figures que vous rencontrerez avec l'opérateur `=` :

```python
>>> x = 2
>>> y = x
>>> y
2
>>> x = 5 - 2
>>> x
3
```

**Ligne 2**. Ici on a un nom de variable à gauche et à droite de l'opérateur `=`. Dans ce cas, on garde la règle d'aller toujous de la droite vers la gauche. C'est donc le contenu de la variable `y` qui est affecté à la variable `x`.

**Ligne 5**. Comme on le verra plus bas, si on a à droite de l'opérateur `=` une expression, ici la soustraction `x = 4 - 2`, celle-ci est d'abord évaluée et c'est le résultat de cette opération qui sera affecté à la variable `x`. On pourra noter également que la valeur de `x` précédente (2) a été écrasée.

open-box-warn

L'opérateur d'affectation `=` \index{operateur affectation@opérateur d'affectation} écrase systématiquement la valeur de la variable située à sa gauche si celle-ci existe déjà.

close-box-warn

## Les types de variables

\index{type@type (de variable)}

open-box-def

Le **type** d'une variable correspond à la nature de celle-ci. Les trois principaux types dont nous aurons besoin dans un premier temps sont les entiers\index{entier} (*integer*\index{integer@integer (type de variable)} ou *int*\index{int@int (type de variable)), les nombres décimaux que nous appellerons *floats*\index{float@float (type de variable)} et les chaînes de caractères\index{chaine de caracteres@chaîne de caractères} (*string*\index{string@string (type de variable)} ou *str*\index{str@str (type de variable)}). 

close-box-def

Bien sûr, il existe de nombreux autres types (par exemple, les booléens, les nombres complexes, etc.). Si vous n'êtes pas effrayés, vous pouvez vous en rendre compte [ici](https://docs.python.org/fr/3.12/library/stdtypes.html).

Dans l'exemple précédent, nous avons stocké un nombre entier (*int*) dans la variable `x`, mais il est tout à fait possible de stocker des *floats*, des chaînes de caractères (*string* ou *str*) ou de nombreux autres types de variables que nous verrons par la suite :

```python
>>> y = 3.14
>>> y
3.14
>>> a = "bonjour"
>>> a
'bonjour'
>>> b = 'salut'
>>> b
'salut'
>>> c = """girafe"""
>>> c
'girafe'
>>> d = '''lion'''
>>> d
'lion'
```

open-box-rem

Python reconnaît certains types de variables automatiquement (entier, *float*). Par contre, pour une chaîne de caractères, il faut l'entourer de guillemets\index{guillemets@guillemets (chaîne de caractères)} (doubles, simples, voire trois guillemets successifs doubles ou simples) afin d'indiquer à Python le début et la fin de la chaîne de caractères.

Dans l'interpréteur, l'affichage direct du contenu d'une chaîne de caractères se fait avec des guillemets simples, quel que soit le type de guillemets utilisé pour définir la chaîne de caractères.

En Python, comme dans la plupart des langages de programmation, c'est le point qui est utilisé comme séparateur décimal. Ainsi, `3.14` est un nombre reconnu comme un *float* en Python alors que ce n'est pas le cas de `3,14`.

close-box-rem

\index{booleen@booléen}

Il existe également des variables de type booléen. Un [booléen](https://fr.wikipedia.org/wiki/Bool%C3%A9en) est une variable qui ne prend que deux valeurs : Vrai ou Faux. En python, on utilise pour cela les deux mots réservés `True` \index{True} et `False` \index{False} :

```python
>>> var = True
>>> var2 = False
>>> var
True
>>> var2
False
```

Nous verrons l'utilité des booléens dans les chapitres 5 *Boucles* et 6 *Tests*.

## Nommage

\index{nommage@nommage (de variable)}

Le nom des variables en Python peut être constitué de lettres minuscules (`a` à `z`), de lettres majuscules (`A` à `Z`), de nombres (`0` à `9`) ou du caractère souligné (`_`). Vous ne pouvez pas utiliser d'espace dans un nom de variable.

Par ailleurs, un nom de variable ne doit pas débuter par un chiffre et il n'est pas recommandé de le faire débuter par le caractère `_` (sauf cas très particuliers).

De plus, il faut absolument éviter d'utiliser un mot « réservé » par Python\index{mot reserve@mot réservé} comme nom de variable (par exemple : `print`, `range`, `for`, `from`, etc.).

Dans la mesure du possible, il est conseillé de mettre des noms de variables explicites. Sauf dans de rares cas que nous expliquerons plus tard dans le cours, évitez les noms de variables à une lettre.

Enfin, Python est sensible à la casse\index{casse@casse (nom de variable)}, ce qui signifie que les variables `TesT`, `test` et `TEST` sont différentes.


## Écriture scientifique

\index{ecriture scientifique@écriture scientifique}

On peut écrire des nombres très grands ou très petits avec des puissances de 10 en utilisant le symbole `e` :

```python
>>> 1e6
1000000.0
>>> 3.12e-3
0.00312
```

On appelle cela écriture ou notation scientifique. On pourra noter deux choses importantes :

- `1e6` ou `3.12e-3` n'implique pas l'utilisation du nombre exponentiel *e* mais signifie $1 \times 10^{6}$ ou $3.12 \times 10^{-3}$ respectivement ;
- même si on ne met que des entiers à gauche et à droite du symbole `e` (comme dans `1e6`), Python génère systématiquement un *float*.

Enfin, vous avez sans doute constaté qu'il est parfois pénible d'écrire des nombres composés de beaucoup de chiffres, par exemple le nombre d'Avogradro $6.02214076 \times 10^{23}$ ou le [nombre d'humains sur Terre](https://thepopulationproject.org/) $8094752749$ au 5 mars 2024 à 19h34. Pour s'y retrouver, Python autorise l'utilisation du caractère « souligné » (ou *underscore*) `_` pour séparer des groupes de chiffres. Par exemple :

```python
>>> avogadro_number = 6.022_140_76e23
>>> print(avogadro_number)
6.02214076e+23
>>> humans_on_earth = 8_094_752_749
>>> print(humans_on_earth)
8094752749
```

\index{\_}

Dans ces exemples, le caractère `_` est utilisé pour séparer des groupes de trois chiffres, mais on peut faire ce qu'on veut :

```python
>>> print(80_94_7527_49)
8094752749
```


## Opérations

### Opérations sur les types numériques

Les quatre opérations arithmétiques de base se font de manière simple sur les types numériques (nombres entiers et *floats*) :

```python
>>> x = 45
>>> x + 2
47
>>> x - 2
43
>>> x * 3
135
>>> y = 2.5
>>> x - y
42.5
>>> (x * 10) + y
452.5
```

Remarquez toutefois que si vous mélangez les types entiers et *floats*, le résultat est renvoyé comme un *float* (car ce type est plus général). Par ailleurs, l'utilisation de parenthèses permet de gérer les priorités.

L'opérateur\index{operateur@opérateur} `/` effectue une division. Contrairement aux opérateurs `+`, `-` et `*`, celui-ci renvoie systématiquement un *float* :

```python
>>> 3 / 4
0.75
>>> 2.5 / 2
1.25
```

L'opérateur puissance utilise les symboles `**` :

```python
>>> 2**3
8
>>> 2**4
16
```

Pour obtenir le quotient et le reste d'une division entière\index{division entiere@division entière} (voir [ici](https://fr.wikipedia.org/wiki/Division_euclidienne) pour un petit rappel sur la division entière), on utilise respectivement les symboles `//` et  modulo\index{modulo@modulo (opérateur)} `%` :

```python
>>> 5 // 4
1
>>> 5 % 4
1
>>> 8 // 4
2
>>> 8 % 4
0
```

Les symboles `+`, `-`, `*`, `/`, `**`, `//` et `%` sont appelés **opérateurs**, car ils réalisent des opérations sur les variables.

Enfin, il existe des opérateurs « combinés » qui effectue une opération et une affectation en une seule étape :

```python
>>> i = 0
>>> i = i + 1
>>> i
1
>>> i += 1
>>> i
2
>>> i += 2
>>> i
4
```

L'opérateur `+=` effectue une addition puis affecte le résultat à la même variable. Cette opération s'appelle une « incrémentation ».

Les opérateurs `-=`, `*=` et `/=` se comportent de manière similaire pour la soustraction, la multiplication et la division.

### Opérations sur les chaînes de caractères

Pour les chaînes de caractères, deux opérations sont possibles, l'addition et la multiplication :

```python
>>> chaine = "Salut"
>>> chaine
'Salut'
>>> chaine + " Python"
'Salut Python'
>>> chaine * 3
'SalutSalutSalut'
```

L'opérateur d'addition `+` concatène (assemble) deux chaînes de caractères. On parle de concaténation\index{concatenation@concaténation}.

L'opérateur de multiplication `*` entre un nombre entier et une chaîne de caractères duplique (répète) plusieurs fois une chaîne de caractères. On parle de duplication\index{duplication}.

open-box-warn

Vous observez que les opérateurs `+` et `*` se comportent différemment s'il s'agit d'entiers ou de chaînes de caractères. Ainsi, l'opération `2 + 2` est une addition alors que l'opération `"2" + "2"` est une concaténation. On appelle ce comportement **redéfinition des opérateurs** \index{redefinition operateur@redéfinition des opérateurs}. Nous serons amenés à revoir cette notion dans le chapitre 24 *Avoir plus la classe avec les objets* (en ligne).

close-box-warn


### Opérations illicites

Attention à ne pas faire d'opération illicite car vous obtiendriez un message d'erreur :

```python
>>> "toto" * 1.3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> "toto" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Notez que Python vous donne des informations dans son message d'erreur. Dans le second exemple, il indique que vous devez utiliser une variable de type *str* c'est-à-dire une chaîne de caractères et pas un *int*, c'est-à-dire un entier.


## La fonction `type()`

Si vous ne vous souvenez plus du type d'une variable, utilisez la fonction `type()`\index{type@type()} qui vous le rappellera.

```python
>>> x = 2
>>> type(x)
<class 'int'>
>>> y = 2.0
>>> type(y)
<class 'float'>
>>> z = '2'
>>> type(z)
<class 'str'>
>>> type(True)
<class 'bool'>
```

Nous verrons plus tard ce que signifie le mot *class*.

open-box-warn

Pour Python, la valeur `2` (nombre entier) est différente de `2.0` (*float*) et est aussi différente de `'2'` (chaîne de caractères).

close-box-warn


## Conversion de types

\index{conversion type@conversion (de types)}

En programmation, on est souvent amené à convertir les types, c'est-à-dire passer d'un type numérique à une chaîne de caractères ou vice-versa. En Python, rien de plus simple avec les fonctions `int()`\index{int@int()}, `float()` \index{float@float()} et `str()`\index{str@str()}. Pour vous en convaincre, regardez ces exemples :

```python
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
```

On verra au chapitre 7 *Fichiers* que ces conversions sont essentielles. En effet, lorsqu'on lit ou écrit des nombres dans un fichier, ils sont considérés comme du texte, donc des chaînes de caractères.

Toute conversion d'une variable d'un type en un autre est appelé *casting*\index{casting} en anglais, il se peut que vous croisiez ce terme si vous consultez d'autres ressources.


## Note sur le vocabulaire et la syntaxe

Nous avons vu dans ce chapitre la notion de **variable** qui est commune à tous les langages de programmation. Toutefois, Python est un langage dit « orienté objet », il se peut que dans la suite du cours nous employions le mot **objet**\index{objet} pour désigner une variable. Par exemple, « une variable de type entier » sera pour nous équivalent à « un objet de type entier ». Nous verrons dans le chapitre 23 *Avoir la classe avec les objets* (en ligne) ce que le mot « objet » signifie réellement (tout comme le mot « classe\index{classe} »).

Par ailleurs, nous avons rencontré plusieurs fois des **fonctions**\index{fonction} dans ce chapitre, notamment avec `type()`, `int()`, `float()` et `str()`. Dans le chapitre 1 *Introduction*, nous avons également vu la fonction `print()`. On reconnaît qu'il s'agit d'une fonction car son nom est suivi de parenthèses (par exemple, `type()`). En Python, la syntaxe générale est `fonction()`.

Ce qui se trouve entre les parenthèses d'une fonction est appelé **argument**\index{argument@argument (passé à une fonction)} et c'est ce que l'on « passe » à la fonction. Dans l'instruction `type(2)`, c'est l'entier `2` qui est l'argument passé à la fonction `type()`. Pour l'instant, on retiendra qu'une fonction est une sorte de boîte à qui on passe un (ou plusieurs) argument(s), qui effectue une action et qui peut renvoyer un résultat ou plus généralement un objet. Par exemple, la fonction `type()` renvoie le type de la variable qu'on lui a passé en argument.

Si ces notions vous semblent obscures, ne vous inquiétez pas, au fur et à mesure que vous avancerez dans le cours, tout deviendra limpide.


## Minimum et maximum

Python propose les fonctions `min()`\index{min@min()} et `max()`\index{max@max()} qui renvoient respectivement le minimum et le maximum de plusieurs entiers ou *floats* :

```python
>>> min(1, -2, 4)
-2
>>> pi = 3.14
>>> e = 2.71
>>> max(e, pi)
3.14
>>> max(1, 2.4, -6)
2.4
```

Par rapport à la discussion de la rubrique précédente, `min()` et `max()` sont des exemples de fonctions prenant plusieurs arguments. En Python, quand une fonction prend plusieurs arguments, on doit les séparer par une virgule. `min()` et `max()` prennent en argument autant d'entiers et de *floats* que l'on veut, mais il en faut au moins deux.


## Exercices

open-box-adv

Pour ces exercices, utilisez l'interpréteur Python.

close-box-adv

### Nombres de Friedman

Les [nombres de Friedman](https://fr.wikipedia.org/wiki/Nombre_de_Friedman) sont des nombres qui peuvent s'exprimer avec tous leurs chiffres dans une expression mathématique.

Par exemple, 347 est un nombre de Friedman car il peut s'écrire sous la forme $4+7^3$. De même pour 127 qui peut s'écire sous la forme $2^7 - 1$.

Déterminez si les expressions suivantes correspondent à des nombres de Friedman. Pour cela, vous les écrirez en Python puis exécuterez le code correspondant.

- $7 + 3^6$
- $(3 + 4)^3$
- $3^6 - 5$
- $(1 + 2^8) \times 5$
- $(2 + 1^8)^7$


### Prédire le résultat : opérations

Essayez de prédire le résultat de chacune des instructions suivantes, puis vérifiez-le dans l'interpréteur Python :

- `(1+2)**3`
- `"Da" * 4`
- `"Da" + 3`
- `("Pa"+"La") * 2`
- `("Da"*4) / 2`
- `5 / 2`
- `5 // 2`
- `5 % 2`


### Prédire le résultat : opérations et conversions de types

Essayez de prédire le résultat de chacune des instructions suivantes, puis vérifiez-le dans l'interpréteur Python :

- `str(4) * int("3")`
- `int("3") + float("3.2")`
- `str(3) * float("3.2")`
- `str(3/4) * 2`
