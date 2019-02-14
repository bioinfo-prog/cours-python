# Plus sur les chaînes de caractères

## Préambule

Nous avons déjà abordé les chaînes de caractères dans le chapitre *variables* et *affichage*. Ici nous allons un peu plus loin notamment avec les [méthodes associées aux chaînes de caractères](https://docs.python.org/fr/3.6/library/string.html).


## Chaînes de caractères et listes

Les chaînes de caractères peuvent être considérées comme des listes (un peu particulières).
```
>>> animaux = "girafe tigre"
>>> animaux
'girafe tigre'
>>> len(animaux)
12
>>> animaux[3]
'a'
```
Nous pouvons donc utiliser certaines propriétés des listes comme les tranches :
```
>>> animaux = "girafe tigre"
>>> animaux[0:4]
'gira'
>>> animaux[9:]
'gre'
>>> animaux[:-2]
'girafe tig'
```

Mais *a contrario* des listes, les chaînes de caractères présentent toutefois une différence notable, ce sont **des listes non modifiables**. Une fois définie, vous ne pouvez plus modifier un de ses éléments. Le cas échéant, Python renvoie un message d'erreur :
```
>>> animaux = "girafe tigre"
>>> animaux[4]
'f'
>>> animaux[4] = "F"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
Par conséquent, si vous voulez modifier une chaîne, vous êtes obligés d'en construire une nouvelle. Pour cela, n'oubliez pas que les opérateurs de concaténation (`+`) et de duplication (`*`) (voir le chapitre *variables*) peuvent vous aider. Vous pouvez également générer une liste, qui elle est modifiable, puis revenir à une chaîne de caractères.


## Caractères spéciaux

Il existe certains caractères spéciaux comme `\n` que nous avons déjà vu (pour le retour à la ligne). Le caractère `\t` vous permet d'écrire une tabulation. Si vous voulez écrire un guillemet simple ou double (et que celui-ci ne soit pas confondu avec les guillemets de déclaration de la chaîne de caractères), vous pouvez utiliser `\'` ou `\"` ou utiliser respectivement des guillements doubles ou simple pour déclarer votre chaîne de caractères.
```
>>> print("Un retour à la ligne\npuis une tabulation\t, puis un guillemet\"")
Un retour à la ligne
puis une tabulation     , puis un guillemet"
>>> print('J\'affiche un guillemet simple')
J'affiche un guillemet simple
>>> print("Un brin d'ADN")
Un brin d'ADN
>>> print('Python est un "super" langage de programmation')
Python est un "super" langage de programmation
```
Quand on souhaite écrire un texte sur plusieurs lignes, il est très commode d'utiliser les guillemets triples permettant de conserver le formatage (notamment les retours à la ligne):
```
>>> x = '''souris
... chat
... abeille'''
>>> x
'souris\nchat\nabeille'
>>> print(x)
souris
chat
abeille
```

## Méthodes associées aux chaînes de caractères

Voici quelques [méthodes](https://docs.python.org/fr/3/library/string.html) spécifiques aux objets de type `string` :
```
>>> x = "girafe"
>>> x.upper()
'GIRAFE'
>>> x
'girafe'
>>> 'TIGRE'.lower()
'tigre'
```
Les méthodes `.lower()` et `.upper()` renvoient un texte en minuscule et en majuscule respectivement. On remarque que l'utilisation de ces fonctions n'altèrent pas la chaîne de départ mais renvoie la chaîne transformée.

Pour mettre en majuscule la première lettre seulement, vous pouvez faire :
```
>>> x[0].upper() + x[1:]
'Girafe'
```
ou encore plus simple avec la méthode adéquate :
```
>>> x.capitalize()
'Girafe'
```

Il existe une méthode associée aux chaînes de caractères qui est particulièrement pratique, la méthode `.split()` :
```
>>> animaux = "girafe tigre singe souris"
>>> animaux.split()
['girafe', 'tigre', 'singe', 'souris']
>>> for animal in animaux.split():
...     print(animal)
...
girafe
tigre
singe
souris
```

La méthode `.split()` découpe une chaîne de caractères en plusieurs éléments appelés *champs*, en utilisant comme séparateur les espaces et les tabulations. Il est possible de modifier le séparateur de champs, par exemple :
```
>>> animaux = "girafe:tigre:singe:souris"
>>> animaux.split(":")
['girafe', 'tigre', 'singe', 'souris']
```

Il est également intéressant d'indiquer à `.split()` le nombre de fois qu'on souhaite découper la chaîne de caractères avec l'argument `maxsplit()` :
```
>>> animaux = "girafe tigre singe souris"
>>> animaux.split(maxsplit=1)
['girafe', 'tigre singe souris']
>>> animaux.split(maxsplit=2)
['girafe', 'tigre', 'singe souris']
```

La méthode `.find()`, quand à elle, recherche une chaîne de caractères passée en argument :
```
>>> animal = "girafe"
>>> animal.find("i")
1
>>> animal.find("afe")
3
>>> animal.find("z")
-1
>>> animal.find("tig")
-1
```
Si l'élément recherché est trouvé, alors l'indice du début de l'élément dans la chaîne de caractères est renvoyé. Si l'élément n'est pas trouvé, alors la valeur `-1` est renvoyée.

Si l'élément recherché est trouvé plusieurs fois, seul l'indice de la première occurrence est retourné :
```
>>> animaux = "girafe tigre"
>>> animaux.find("i")
1
```

On trouve aussi la méthode `.replace()` qui substitue une chaîne de caractères par une autre :
```
>>> animaux = "girafe tigre"
>>> animaux.replace("tigre", "singe")
'girafe singe'
>>> animaux.replace("i", "o")
'gorafe togre'
```

Enfin, la méthode `.count()` compte le nombre d’occurrences d'une chaîne de caractères passée en argument :
```
>>> animaux = "girafe tigre"
>>> animaux.count("i")
2
>>> animaux.count("z")
0
>>> animaux.count("tigre")
1
```


## Extraction de valeurs numériques d'une chaîne de caractères

Une tâche courante en Python est de lire une chaîne de caractères (provenant par exemple d'un fichier), d'extraire des valeurs de cette chaîne de caractères puis ensuite les manipuler.

On considère par exemple la chaîne de caractères `val` :
```
>>> val = "3.4 17.2 atom"
```

On souhaite extraire les valeurs `3.4` et `17.2` pour ensuite les additionner.

Dans un premier temps, on découpe la chaîne de caractères avec l'instruction `.split()` :
```
>>> val2 = val.split()
>>> val2
['3.4', '17.2', 'atom']
```

On obtient une liste de chaînes de caractères. On transforme ensuite les deux premiers éléments de cette liste en *floats* (avec la fonction `float()`) pour pouvoir les additionner :
```
>>> float(val2[0]) + float(val2[1])
20.599999999999998
```


## Conversion d'une liste de chaînes de caractères en une chaîne de caractères

On a vu dans le chapitre 2 la conversion des types simples (entier, *float* et chaînes de caractères) en un autre avec les fonctions `int()`, `float()` et `str()`. La conversion d'une liste de chaînes de caractères en une chaîne de caractères est un peu particulière puisqu'elle fait appelle à la méthode `.join()`.
```
>>> seq = ["A", "T", "G", "A", "T"]
>>> seq
['A', 'T', 'G', 'A', 'T']
>>> "-".join(seq)
'A-T-G-A-T'
>>> " ".join(seq)
'A T G A T'
>>> "".join(seq)
'ATGAT'
```

Les éléments de la liste initiale sont concaténés les uns à la suite des autres et intercalés par un séparateur qui peut être n'importe quelle chaîne de caractères. Ici, on a utilisé un tiret, un espace et rien.

Attention, la méthode `.join()` ne s'applique qu'à une liste de chaînes de caractères.
```
>>> maliste = ["A", 5, "G"]
>>> " ".join(maliste)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected string, int found
```

On espére qu'après ce petit tour d'horizon vous serez convaincu de la richesse des méthodes associées aux chaînes de caractères. Pour avoir une liste exhaustive de l'ensemble des méthodes associées à une variable particulière, vous pouvez utiliser la fonction `dir()`.
```
>>> animaux = "girafe tigre"
>>> dir(animaux)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '_
_getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '_
_init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__'
, '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'for
mat_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'i
sidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'is
title', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
Pour l'instant vous pouvez ignorer les méthodes qui commencent et qui se terminent par deux tirets bas (*underscores*) `__`.

Vous pouvez ensuite accéder à l'aide et à la documentation d'une méthode particulière avec `help()`, par exemple pour `.split()` :
```
>>> help(animaux.split)
Help on built-in function split:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings

    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator.
(END)
```
Attention de ne pas mettre les parenthèses à la suite du nom de la méthode : `help(animaux.split)` et pas `help(animaux.split())`.


## Exercices

Conseil : pour ces exercices, écrivez des scripts dans des fichiers, puis exécutez-les dans un *shell*.


### Parcours d'une liste de chaînes de caractères

Soit la liste `['girafe', 'tigre', 'singe', 'souris']`. Avec une boucle, affichez chaque élément ainsi que sa taille (nombre de caractères).


### Lecture de fichier et saut de ligne

Le fichier `zoo.txt` contient les lignes suivantes :
```
girafe
tigre
singe
souris
```

Récréez-le puis créez un script qui affiche le contenu de chaque ligne de cette façon, et sans saut de ligne superflu :
```
girafe
tigre
singe
souris
```


### Fréquence des bases dans une séquence nucléique

Soit la séquence nucléique `ATATACGGATCGGCTGTTGCCTGCGTAGTAGCGT`. On souhaite calculer la fréquence de chaque base A, T, C et G dans cette séquence et afficher le résultat à l'écran. Créez pour cela une fonction `calc_composition()` à laquelle vous passez votre séquence nucléique sous forme de chaîne de caractères et qui renvoie une liste de 4 *floats* indiquant respectivement la fréquence en bases `A`, `T`, `G` et `C`.


### Conversion des acides aminés du code à trois lettres au code à une lettre

Soit la séquence protéique `ALA GLY GLU ARG TRP TYR SER GLY ALA TRP`. Transformez cette séquence en une chaîne de caractères en utilisant le code à une lettre pour les acides aminés.

Rappel de la nomenclature des acides aminés :

|  Acide aminé  | Code 3-lettres | Code 1-lettre |
|---------------|:--------------:|:-------------:|
|    Alanine    |       Ala      |       A       |
|    Arginine   |       Arg      |       R       |
|   Asparagine  |       Asn      |       N       |
|   Aspartate   |       Asp      |       D       |
|    Cystéine   |       Cys      |       C       |
|   Glutamate   |       Glu      |       E       |
|   Glutamine   |       Gln      |       Q       |
|    Glycine    |       Gly      |       G       |
|   Histidine   |       His      |       H       |
|   Isoleucine  |       Ile      |       I       |
|    Leucine    |       Leu      |       L       |
|     Lysine    |       Lys      |       K       |
|   Méthionine  |       Met      |       M       |
| Phénylalanine |       Phe      |       F       |
|    Proline    |       Pro      |       P       |
|     Sérine    |       Ser      |       S       |
|   Thréonine   |       Thr      |       T       |
|  Tryptophane  |       Trp      |       W       |
|    Tyrosine   |       Tyr      |       Y       |
|     Valine    |       Val      |       V       |


### Distance de Hamming

La [distance de Hamming](http://en.wikipedia.org/wiki/Hamming_distance) mesure la différence entre deux séquences de même taille en sommant le nombre de positions qui, pour chaque séquence, ne correspondent pas au même acide aminé.

Écrivez la fonction `hamming()`  qui prend en argument deux chaînes de caractères et qui renvoie la distance de Hamming entre ces deux chaînes de caractères.

Calculez la distance de Hamming entre les séquences `AGWPSGGASAGLAIL` et `IGWPSAGASAGLWIL`, puis entre les séquences `ATTCATACGTTACGATT` et `ATACTTACGTAACCATT`.


### Palindrome

Un palindrome est un mot ou une phrase dont l'ordre des lettres reste le même si on le lit de gauche à droite ou de droite à gauche. Par exemple, *ressasser* et *Engage le jeu que je le gagne* sont des palindromes.

Écrivez la fonction `palindrome()` qui prend en argument une chaîne de caractères et qui affiche `xxx est un palindrome` si la chaîne de caractères est un palindrome et `xxx n'est pas un palindrome` sinon (bien sur, `xxx` est ici le palindrome en question). Pensez à vous débarrasser au préalable des majuscules et des espaces.

Testez ensuite si les expressions suivantes sont des palindromes :

- Radar
- Never odd or even
- Karine alla en Iran
- Un roc si biscornu


### Mot composable

Un mot est composable à partir d'une séquence de lettres si la séquence contient toutes les lettres du mot. Comme au Scrabble, chaque lettre de la séquence ne peut être utilisée qu'une seule fois. Par exemple, `coucou` est composable
à partir de *uocuoceokzefhu*.

Écrivez la fonction `composable()` qui prend en argument un mot (chaîne de caractères) et une séquence de lettre (chaîne de caractères) et qui affiche `Le mot xxx est composable à partir de yyy` si le mot (`xxx`) est composable à partir de la séquence de lettres (`yyy`) et `Le mot xxx n'est pas composable à partir de yyy` sinon.

Testez la fonction avec différents mots et séquences.


### Alphabet et pangramme

Les codes ASCII des lettres minuscules de l'alphabet vont de 97 (lettre 'a') à 122 (lettre 'z'). La fonction `chr()` prend en argument un code ASCII sous forme d'une entier et renvoie le caractère correspondant. Ainsi `chr(97)` renvoie `'a'`, `chr(98)` renvoie `'b'` et ainsi de suite.

Écrivez la fonction `get_alphabet()` qui utilise une boucle et la fonction `chr()` et qui renvoie une chaîne de caractères contenant toutes les lettres de l'alphabet.

Un [pangramme](http://fr.wikipedia.org/wiki/Pangramme) est une phrase comportant au moins une fois chaque lettre de l'alphabet. Par exemple, "Portez ce vieux whisky au juge blond qui fume" est un pangramme.

Écrivez la fonction `pangramme()` qui utilise la fonction `get_alphabet()` précédente, qui prend en argument une chaîne de caractère (`xxx`) et qui renvoie `xxx est un pangramme` si cette chaîne de caractères est un pangramme et `xxx n'est pas un pangramme` sinon. Pensez à vous débarasser des majuscules le cas échéant.

Testez ensuite si les expressions suivantes sont des pangrammes :

- Portez ce vieux whisky au juge blond qui fume
- Monsieur Jack vous dactylographiez bien mieux que votre ami Wolf
- Buvez de ce whisky que le patron juge fameux


### Affichage des carbones alpha d'une structure de protéine

Téléchargez le fichier `1bta.pdb` qui correspond à la [structure tridimensionnelle de la protéine barstar](http://www.rcsb.org/pdb/explore.do?structureId=1BTA) sur le site de la ([PDB](https://files.rcsb.org/download/1BTA.pdb)).

Écrivez la fonction `trouve_calpha()` qui prend en argument le nom d'un fichier PDB (sous forme de chaîne de caractères), qui sélectionne uniquement les lignes contenant des carbones alpha, qui stocke ces lignes et les renvoie sous forme de liste.

En utilisant la fonction `trouve_calpha()`, affichez à l'écran les carbones alpha des deux premiers résidus.

*Conseil :* vous trouverez des explications sur le format PDB et des exemples de code pour lire ce type de fichier en Python dans l'annexe A *Quelques formats de données rencontrés en biologie*


### Calcul des distances entre les carbones alpha consécutifs d'une structure de protéine

En utilisant la fonction `trouve_calpha()` précédente, calculez la distance inter-atomique entre les carbones alpha des deux premiers résidus (avec deux chiffres après la virgule).

Écrivez ensuite la fonction `calcule_distance()` qui prend en argument la liste renvoyée par la fonction `trouve_calpha()` précédente, qui calcule les distance inter-atomiques entre carbones alpha consécutifs et affiche ces distances sous la forme :

`numero_calpha_1 numero_calpha_2 distance`

La distance sera affichée avec deux chiffres après la virgule. Voici un exemple avec les premiers carbones alpha :
```
1 2 3.80
2 3 3.80
3 4 3.83
4 5 3.82
```

On rappelle que la distance *d* entre deux points A et B de coordonnées respectives $(x_A, y_A, z_A)$ et $(x_B, y_B, z_B)$ se calcule comme :

$$
d = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}
$$

Modifiez maintenant la fonction `calcule_distance()` pour qu'elle affiche à la fin la moyenne des distances.

La distance inter carbones alpha dans les protéines est très stable et de l'ordre de 3,8 angströms. Observez avec attention les valeurs que vous avez calculées pour la protéine 1BTA. Expliquez la valeur surprenante que vous devriez avoir obtenue.

*Conseil :* vous trouverez des explications sur le format PDB et des exemples de code pour lire ce type de fichier en Python dans l'annexe *Quelques formats de données rencontrés en biologie*
