# Expressions régulières et parsing

Le [module re](https://docs.python.org/3/library/re.html) vous permet d'utiliser des expressions régulières au sein de Python. Les expressions régulières sont aussi appelées en anglais *regular expressions* ou en plus court *regex* (dans la suite de ce chapitre, nous utiliserons souvent le mot *regex* pour désigner une expression régulière). Elles sont puissantes et donc incontournables en bioinformatique, spécialement lorsque vous souhaitez récupérer des informations dans des gros fichiers.

Cette action de recherche de données dans un fichier est appelée plus généralement *parsing* (qui signifie littéralement "analyse syntaxique"). Le *parsing* fait partie du travail quotidien du bioinformaticien, il est sans arrêt en train de "fouiller" dans des fichiers pour en extraire des informations d'intérêt comme par exemple récupérer les coordonnées 3D des atomes d'une protéines dans un fichier PDB ou alors extraire les gènes d'un fichier GenBank.

Dans ce chapitre, nous ne ferons que quelques rappels sur les expressions régulières. Pour une documentation plus complète, référez-vous à la [page d'aide des expressions régulières](https://docs.python.org/3/library/re.html) sur le site officiel de Python.

## Définition et syntaxe

Une expression régulière est une suite de caractères qui a pour but de décrire un fragment de texte. Cette suite de caractères est encore appelée *motif* (en anglais *pattern*), motif qui est constitué de deux types de caractères:

- Les caractères dits *normaux*.
- Les *métacaractères* ayant une signification particulière, par exemple le caractère `^` signifie début de ligne et non pas le caractère "chapeau" littéral.

Certains programmes Unix comme `egrep`, `sed` ou encore `awk` savent interpréter les expressions régulières. Tous ces programmes fonctionnent généralement selon le schéma suivant:

- Le programme lit un fichier ligne par ligne.
- Pour chaque ligne lue, si l'expression régulière passée en argument est retrouvée dans la ligne alors le programme effectue une action.

Par exemple, pour le programme `egrep` :

```
$ egrep "^DEF" herp_virus.gbk
DEFINITION  Human herpesvirus 2, complete genome.
$
```

Ici, `egrep` affiche toutes les lignes du fichier GenBank du virus de l'herpès (`herp_virus.gbk`) dans lesquelles la regex `^DEF` (c'est-à-dire le mot `DEF` en début de ligne) est retrouvée.

Il est intéressant ici de faire une petite digression sur le vocabulaire utilisé en anglais : en général, on utilise le verbe *to match* pour indiquer qu'une regex "a fonctionné". Bien qu'il n'y ait pas de traduction littérale en français, on peut utiliser les verbes "retrouver" ou "correspondre". Par exemple, pour traduire la phrase *The regex matches the line*" on pourra utiliser "la regex est retrouvée dans la ligne" ou encore "la regex correspond dans la ligne".

Avant de voir comment Python gère les expressions régulières, voici quelques éléments de syntaxe des métacaractères :


`^`

:   Début de chaîne de caractères ou de ligne.

    Exemple : la regex `^ATG` est retrouvée dans la chaîne de caractères `ATGCGT` mais pas dans la chaîne `CCATGTT`.

`$`

:   Fin de chaîne de caractères ou de ligne.

    Exemple : la regex `ATG$` est retrouvée correspond dans la chaîne de caractères `TGCATG` mais pas dans la chaîne `CCATGTT`.

`.`

:   N'importe quel caractère (mais un caractère quand même).

    Exemple : la regex `A.G` est retrouvée dans `ATG`, `AtG`, `A4G`, mais aussi dans `A-G` ou dans `A G`.


`[ABC]`

:   Le caractère A ou B ou C (un seul caractère).

    Exemple : la regex `T[ABC]G` est retrouvée dans `TAG`, `TBG` ou `TCG`, mais pas à `TG`.

`[A-Z]`

:   N'importe quelle lettre majuscule.

    Exemple : la regex `C[A-Z]T` est retrouvée dans `CAT`, `CBT`, `CCT`...

`[a-z]`

:   N'importe quelle lettre minuscule.

`[0-9]`

:   N'importe quel chiffre.

`[A-Za-z0-9]`

:   N'importe quel caractère alphanumérique.

`[^AB]`

:   N'importe quel caractère sauf A et B.

    Exemple : la regex `CG[^AB]T` est retrouvée dans `CG9T`, `CGCT`... mais pas dans `CGAT` ni dans `CGBT`.

`\`

:   Caractère d'échappement (pour protéger certains caractères).

    Exemple : la regex `\+` désigne le caractère `+` littéral. La regex `A\.G` est retrouvée dans `A.G` et non pas dans `A` suivi de n'importe quel caractère, suivi de `G`.

`*`

:   0 à n fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(CG)*T` est retrouvée dans `AT`, `ACGT`, `ACGCGT`...

`+`

:   1 à n fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(CG)+T` est retrouvée dans `ACGT`, `ACGCGT`... mais pas dans `AT`.

`?`

:   0 à 1 fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(CG)?T` est retrouvée dans `AT` ou `ACGT`.

`{n}`

:   *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(CG){2}T` est retrouvée dans `ACGCGT` mais pas dans `ACGT`, `ACGCGCGT` ou `ACGCG`.

`{n,m}`

:   *n* à *m* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(C){2,4}T` est retrouvée dans `ACCT`, `ACCCT` et `ACCCCT` mais pas dans `ACT`, `ACCCCCT` ou `ACCC`.

`{n,}`

:   Au moins *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(C){2,}T` est retrouvée dans `ACCT`, `ACCCT` et `ACCCCT` mais pas à `ACT` ou `ACCC`.

`{,m}`

:   Au plus *m* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la regex `A(C){,2}T` est retrouvée dans `AT`, `ACT` et `ACCT` mais pas dans `ACCCT` ou `ACC`.

`(CG|TT)`

:   Les chaînes de caractères `CG` ou `TT`.

    Exemple : la regex `A(CG|TT)C` est retrouvée dans `ACGC` ou `ATTC`.

Enfin, il existe des caractères spéciaux qui sont bien commodes et qui peuvent être utilisés en tant que métacaractères :

`\d`

: remplace n'importe quel chiffre (*d* signifie *digit*), équivalent à `[0-9]`.

`\w`

: remplace n'importe quel caractère alphanumérique et le caractère souligné (*underscore*) (*w* signifie *word character*), équivalent à `[0-9A-Za-z_]`.

`\s`

: remplace n'importe quel "espace blanc" (*whitespace*) (*s* signifie *space*), équivalent à `[ \t\n]` (c'est à dire espace, tabulation, nouvelle ligne), **attention** `\s` remplace également les caractères spéciaux `\r` et `\f` que nous ne développerons pas ici. `\s` est particulièrement pratique pour détecter une combinaison d'espace(s) et/ou de tabulation(s).

Comme vous le constatez, les métacaractères sont nombreux et leur signification est parfois difficile à maîtriser. Faites particulièrement attention aux métacaractères `.`, `+` et `*` qui combinés ensemble peuvent donner des résultats ambigus.

Il est important de savoir par ailleurs que les regex sont *avides* lorsqu'on utilise les métacaractères `+` et `*` lors d'une substitution. C'est à dire que la regex cherchera à "s'étendre" au maximum. Par exemple, si on utilise la regex `A+` pour faire une substitution dans la chaîne `TTTAAAAAAAAGC`, tous les A de cette chaîne (8 en tout) seront concernés, bien que `AA`, `AAA`, etc, "fonctionnent" également avec cette regex.

Nous vous conseillons de tester systématiquement vos expressions régulières sur des exemples simples. Pour vous aider nous vous recommandons des sites internet :

- [https://regexone.com/](https://regexone.com/) qui propose un petit tutorial en ligne très bien fait.
- [https://regexr.com/](https://regexr.com/) qui permet de visualiser tous les endroits où une regex est retrouvée dans un texte.
- [https://www.regular-expressions.info](https://www.regular-expressions.info) vous donnera une documentation exaustive sur les regex (il y a même une section sur Python).

N'hésitez pas à tester ces sites avant de vous lancer dans les exercices ou dans l'écriture de vos propres regex !


## Le Module re

### La fonction search()

Dans le module `re`, la fonction incontournable est la fonction `search()`. Elle permet de rechercher un motif (*pattern* en anglais, c'est à dire une regex) au sein d'une chaîne de caractères avec une syntaxe de la forme `search(motif, chaine)`. Si `motif` est retrouvé dans `chaine`, Python renvoie un objet du type `SRE_Match`.

**Attention**, le motif (ou *pattern*) que vous utilisez comme premier argument de la fonction `search()` sera interprété *en tant que regex*. Ainsi, `^DEF` correspondra au mot `DEF` en début de chaîne, et non pas au caractère littéral `^`suivi du mot `DEF`.

Sans entrer dans les détails propres au langage orienté objet, si on utilise un objet du type `SRE_Match` dans un test, il sera considéré comme vrai. Regardez cet exemple dans lequel on va rechercher le motif `tigre` dans la chaîne de caractères `"girafe tigre singe"` :

```
>>> import re
>>> animaux = "girafe tigre singe"
>>> re.search('tigre', animaux)
<_sre.SRE_Match object at 0x7fefdaefe2a0>
>>> if re.search('tigre', animaux):
...     print("OK")
...
OK
```

### Les fonctions match() et fullmatch()

Il existe aussi la fonction `match()` dans le module `re` qui fonctionne sur le modèle de `search()`. La différence est qu'elle renvoie un object du type `SRE_Match` seulement lorsque l'expression régulière correspond au début de la chaîne de caractères (à partir du premier caractère).

```
>>> animaux = "girafe tigre singe"
>>> re.search('tigre', animaux)
<_sre.SRE_Match object at 0x7fefdaefe718>
>>> re.match('tigre', animaux)
>>>
>>> animaux = "tigre singe"
>>> re.match('tigre', animaux)
<_sre.SRE_Match object; span=(0, 5), match='tigre'>
>>>
```

Il existe également la fonction `fullmatch()` qui renvoie un object du type `SRE_Match` si et seulement si l'expression régulière correspond **exactement** à la chaîne de caractères.

```
>>> animaux = "tigre "
>>> re.fullmatch('tigre', animaux)
>>> animaux = "tigre"
>>> re.fullmatch('tigre', animaux)
<_sre.SRE_Match object; span=(0, 5), match='tigre'>
```

De manière générale, nous vous recommandons plutôt l'usage de la fonction `search()`. Si vous souhaitez avoir une correspondance avec le début de la chaîne comme dans la fonction `match()`, vous pouvez toujours utiliser l'accroche de début de ligne `^`. Si vous voulez une correspondance exacte comme dans la fonction `fullmatch()`, vous pouvez utiliser les métacaractères `^` et `$`, par exemple `^tigre$`.

### Compilation d'expressions régulières

Lorsqu'on a besoin de tester la même expression régulière sur plusieurs milliers de chaînes de caractères, il est pratique de préalablement compiler l'expression régulière à l'aide de la fonction `compile()` qui renvoie un objet de type `SRE_Pattern` :

```
>>> regex = re.compile("^tigre")
>>> regex
<_sre.SRE_Pattern object at 0x7fefdafd0df0>
```

On peut alors utiliser directement cet objet avec la méthode `.search()` :

```
>>> animaux = "girafe tigre singe"
>>> regex.search(animaux)
>>> animaux = "tigre singe"
>>> regex.search(animaux)
<_sre.SRE_Match object at 0x7fefdaefe718>
>>> animaux = "singe tigre"
>>> regex.search(animaux)
```


### Groupes

L'intérêt de l'objet de type `SRE_Match` renvoyé par Python lorsqu'une expression régulière trouve une correspondance dans une chaîne de caractères est de pouvoir ensuite récupérer certaines zones précises :

```
>>> regex = re.compile('([0-9]+)\.([0-9]+)')
```

Dans cet exemple, on recherche un nombre :

- qui débute par un ou plusieurs chiffres `[0-9]+`,
- suivi d'un point `\.` (le point a d'habitude une signification de métacaractère, donc il faut l'échapper avec `\` pour qu'il retrouve sa signification de point),
- et qui se termine encore par un ou plusieurs chiffres `[0-9]+`.

Les parenthèses dans l'expression régulière permettent de créer des groupes (`[0-9]+` deux fois) qui seront récupérés ultérieurement par la méthode `.group()`.

```
>>> resultat = regex.search("pi vaut 3.14")
>>> resultat.group(0)
'3.14'
>>> resultat.group(1)
'3'
>>> resultat.group(2)
'14'
>>> resultat.start()
8
>>> resultat.end()
12
```

La totalité de la correspondance est donnée par `.group(0)`, le premier élément entre parenthèses est donné par `.group(1)` et le second par `.group(2)`.

Les méthodes `.start()` et `.end()` donnent respectivement la position de début et de fin de la zone qui correspond à l'expression régulière. Notez que la méthode `.search()` ne renvoie que la première zone qui correspond à l'expression régulière, même s'il en existe plusieurs :

```
>>> resultat = regex.search("pi vaut 3.14 et e vaut 2.72")
>>> resultat.group(0)
'3.14'
```


### La méthode .findall()

Pour récupérer chaque zone, vous pouvez utiliser la méthode `.findall()` qui renvoie une liste des éléments en correspondance.

```
>>> regex = re.compile('[0-9]+\.[0-9]+')
>>> resultat = regex.findall("pi vaut 3.14 et e vaut 2.72")
>>> resultat
['3.14', '2.72']
```

L'utilisation des groupes entre parenthèses est également possible et ceux-ci sont automatiquement renvoyés sous la forme de tuples.

```
>>> regex = re.compile('([0-9]+)\.([0-9]+)')
>>> resultat = regex.findall("pi vaut 3.14 et e vaut 2.72")
>>> resultat
[('3', '14'), ('2', '72')]
```

### La méthode .sub()

Enfin, la méthode `.sub()` permet d'effectuer des remplacements assez puissants. Par défaut la méthode `.sub(chaine1,chaine2)` remplace toutes les occurrences trouvées par l'expression régulière dans `chaine2` par `chaine1`. Si vous souhaitez ne remplacer que les *n* premières occurrences, utilisez l'argument `count=n` :

```
>>> regex = re.compile('[0-9]+\.[0-9]+')
>>> regex.sub('quelque chose',"pi vaut 3.14 et e vaut 2.72")
'pi vaut quelque chose et e vaut quelque chose'
>>> regex.sub('quelque chose',"pi vaut 3.14 et e vaut 2.72", count=1)
'pi vaut quelque chose et e vaut 2.72'
```

Encore plus puissant, il est possible d'utiliser dans le remplacement des groupes qui ont été *capturés* avec des parenthèses.

```
>>> regex = re.compile('([0-9]+)\.([0-9]+)')
>>> phrase = "pi vaut 3.14 et e vaut 2.72"
>>> regex.sub("approximativement \\1",phrase)
'pi vaut approximativement 3 et e vaut vaut approximativement 2'
>>>
>>> regex.sub("approximativement \\1 (puis .\\2)",phrase)
'pi vaut approximativement 3 (puis .14) et e vaut approximativement 2 (puis .72)'
```

Si vous avez capturé des groupes, il suffit d'utiliser `\\1`, `\\2` (etc) pour utiliser les groupes correspondants dans la chaîne substituée. On pourra noter que la syntaxe générale pour récupérer des groupes dans les outils qui gèrent les regex est `\1`, `\2` (etc). Toutefois Python nous oblige à mettre un deuxième backslash car il y a ici deux niveaux: i) un premier niveau Python où on veut mettre un backslash littéral (donc `\\`), puis ii) un deuxième niveau regex dans lequel on veut retrouver `\1`. Si cela est confus, retenez seulement qu'il faut mettre un `\\` devant le numéro de groupe.

Enfin, sachez que la réutilisation d'un groupe précédemment capturé est aussi utilisable lors d'une utilisation classique de regex. Par exemple :

```
>>> re.search("(pan)\\1","bambi et panpan")
<_sre.SRE_Match object; span=(9, 15), match='panpan'>
>>> re.search("(pan)\\1","le pistolet a fait pan !")
>>>
```

Dans cette regex `(pan)\\1` on capture d'abord le groupe `(pan)` grâce aux parenthèses (il s'agit du groupe 1 puisque c'est le premier jeu de parenthèses), immédiatement suivi du même groupe grâce au `\\1`. Dans cet exemple, on capture donc le mot `panpan`. Ainsi, si on a une seule occurrence du mot `pan`, cette regex ne fonctionne pas.

Bien sûr, si on avait eu un deuxième groupe, on aurait pu le réutiliser avec `\\2`, un troisième groupe avec `\\3`, etc.


Nous espérons vous avoir convaincu de la puissance du module `re` et des expressions régulières, alors plus de temps à perdre, à vos regex !


## Exercices


### Regex de base

Dans ces exercices, nous allons utiliser le fichier GenBank [NC_001133.gbk](data-files/NC_001133.gbk) correspondant au chromosome I de la levure Saccharomyces Cerevisiae (souche S288C).

- Créer un script `def.py` qui recherche le mot `DEFINITION` dans le fichier gbk, et ce en début de ligne. Le script affichera cette ligne (équivalent de `egrep`)
- Ecrire un script `journal.py` qui affiche tous les journaux (mot-clé `JOURNAL`) dans lesquels ont été publiés les travaux sur ce génome (bien sûr utiliser une regex !).


### Nettoyeur d'espaces

Le fichier [cigale_fourmi.txt](data-files/cigale_fourmi.txt) contient le célèbre poème de Jean de la Fontaine. Malheureusement celui qui l'a recopié a parfois mis plusieurs espaces au lieu d'un seul entre les différents mots. Créer un script `cigale_fourmi.py` qui grâce aux regex et à la fonction `sub()` remplace les combinaisons de 2, 3, 4 (etc) espaces par un seul espace. Le nouveau texte "propre" sera enregistré dans un fichier `cigale_fourmi_propre.txt`.


### Compteur de gènes

- Téléchargez un petit fichier gbk sur la GenBank (vous pouvez réutiliser NC_001133.gbk).
- Écrivez un script `genes.py` qui affiche tous les mots `gene` dans le fichier gbk. Lancez ce script de la manière suivante afin de voir ce que celui-ci renvoie page par page :
```
$ python3 genes.py | less
```
Si on compte ces lignes est-ce une bonne méthode pour compter les gènes ? Comment selon vous peut-on récupérer une ligne unique par gène (bien observer le fichier GenBank) ?
- Sur la base du script précédent, écrivez un script `compte_genes.py` qui compte le nombre de gènes total et qui l'affiche à l'écran.
- Améliorez le script afin qu'il affiche en plus le nombre de gènes directs et le nombre de gènes complémentaires.


### Recherche de séquence dans un fichier gbk

On veut créer un script `get_seq.py` qui extrait une séquence d'un fichier GenBank.

- Téléchargez un petit fichier gbk sur la GenBank (vous pouvez réutiliser NC_001133.gbk).
- Affichez toutes les lignes qui commencent par au moins un espace suivi d'un chiffre. Cela correspond-il aux lignes contenant la séquence d'ADN?
- Affinez la regex pour ne récupérer que les lignes contenant la séquence. Testez votre nouvelle regex sur d'autres fichiers GenBank récupérés sur internet.
- Avec la regex trouvée précédemment, écrivez un script qui récupère la séquence (dans une chaîne de caractères) en récupérant les bonnes lignes et en substituant les chiffres, espaces et retours chariot par rien du tout. Le script fonctionnera comme suit :
```
$ python3 get_seq.py file.gbk
Le fichier file.gbk contient un génome de XXX bases.
$
```
où XXX correspond au nombre de paires de bases dans le génome. Comparez avec le nombre de bases indiqué dans le fichier GenBank (ligne LOCUS).


### Nettoyeur de doublons (++)

Écrivez un script `ote_doublons.py` qui lit un fichier [breves_doublons.txt](data-files/breves_doublons.txt) et qui ôte tous les doublons de celui-ci à l'aide d'une regex. Le script affichera le nouveau texte à l'écran.


### Le défi du dé-htmliseur (+++)

Le format html permet d'afficher des pages web sur un navigateur. Il s'agit d'un langage à balise qui fonctionne avec des balises ouvrantes `<balise>` et des balises fermantes `</balise>`. Créez un script `dhtmliseur.py` qui lit le fichier [fichier_a_dhtmliser.html](data-files/fichier_a_dhtmliser.html) et qui renvoie à l'écran tout le texte de ce fichier contenu en dehors des balises html. Nous vous conseillons d'ouvrir le fichier html dans un éditeur de texte et de bien l'observer. N'hésitez pas à vous aider du site [https://regexr.com/](https://regexr.com/).


### Remplacements puissants (+++)

À partir du fichier contenant le [protéome humain](data-files/human-proteome.fasta), on souhaite faire une liste de toutes les protéines et les indexer avec un numéro arbitraire. Nous allons pour cela utiliser les regex et la substitution. Écrivez un script `liste_proteome.py` qui procède comme suit :

- Lisez le fichier de protéome, et affichez uniquement les lignes de commentaires du fichier multi-fasta à l'aide d'une regex (lignes commençant par `>`).
- Développez votre regex afin de récupérer le numéro d'accession dans un groupe (par exemple dans la ligne `>sp|O95139|NDUB6_HUMAN NADH dehydrogenase [...]` le numéro d'accession est `O95139`, il se situe entre le premier et le deuxième symbole `|` (symbole *pipe*)).
- Au lieu d'afficher les lignes complète, affichez seulement le numéro d'accession, à l'aide de la fonction `sub()`.
- Au final, on souhaite la sortie suivante (pensez à l'opérateur de formatage qui ajoute des 0 à la place d'espaces, par exemple `{:03d}`) :

```
protein 00001 O95139
protein 00002 O75438
[...]
protein 20372 Q9UKP6
protein 20373 Q96HZ7
```
