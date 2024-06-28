# Expressions régulières et *parsing*

Le module *re* permet d'utiliser des expressions régulières avec Python. Les expressions régulières sont aussi appelées en anglais *regular expressions*, ou en plus court *regex*. Dans la suite de ce chapitre, nous utiliserons souvent le mot *regex* pour désigner une expression régulière. Les expressions régulières sont puissantes et incontournables en bioinformatique, surtout lorsque vous souhaitez récupérer des informations dans de gros fichiers.

Cette action de recherche de données dans un fichier est appelée généralement *parsing* (qui signifie littéralement « analyse syntaxique »). Le *parsing* fait partie du travail quotidien du bioinformaticien, il est sans arrêt en train de « fouiller » dans des fichiers pour en extraire des informations d'intérêt, par exemple récupérer les coordonnées 3D des atomes d'une protéine dans un fichier PDB, ou encore extraire les gènes d'un fichier GenBank.

Dans ce chapitre, nous ne ferons que quelques rappels sur les expressions régulières. Pour une documentation plus complète, référez-vous à la [page d'aide des expressions régulières](https://docs.python.org/fr/3/library/re.html) sur le site officiel de Python.

\index{re@re (module)}

## Définition et syntaxe

\index{motif@motif (regex)}
\index{pattern@pattern (regex)}
\index{metacaracteres@métacaractères (regex)}

Une expression régulière est une suite de caractères qui a pour but de décrire un fragment de texte. Cette suite de caractères est encore appelée **motif** (en anglais, *pattern*), qui est constitué de deux types de caractères :

- les caractères dits *normaux* ;
- les *métacaractères* ayant une signification particulière, par exemple le caractère `^` signifie début de ligne, et non pas le caractère « chapeau » littéral.

Avant de présenter les *regex* en Python, nous allons faire un petit détour par Unix. En effet, certains programmes, comme `egrep`, `sed` ou encore `awk`, savent interpréter les expressions régulières. Tous ces programmes fonctionnent généralement selon le schéma suivant :

- le programme lit un fichier ligne par ligne ;
- pour chaque ligne lue, si l'expression régulière passée en argument est retrouvée dans la ligne, alors le programme effectue une action.

Par exemple, pour le programme `egrep` :

```text
$ egrep "^DEF" herp_virus.gbk
DEFINITION  Human herpesvirus 2, complete genome.
```

\index{egrep@egrep (regex)}

Ici, `egrep` affiche toutes les lignes du fichier du virus de l'herpès (`herp_virus.gbk`) dans lesquelles la *regex* `^DEF` (c'est-à-dire le mot `DEF` en début de ligne) est retrouvée.

open-box-rem

Il est intéressant de faire un point sur le vocabulaire utilisé en anglais et en français. En général, on utilise le verbe *to match* pour indiquer qu'une *regex* « a fonctionné ». Bien qu'il n'y ait pas de traduction littérale en français, on peut utiliser les verbes « retrouver » ou « correspondre ». Par exemple, on pourra traduire l'expression « *The regex matches the line* » par « La *regex* est retrouvée dans la ligne » ou encore « La *regex* correspond dans la ligne ».

close-box-rem

Après avoir introduit le vocabulaire des *regex*, voici quelques éléments de syntaxe des métacaractères :


`^`

:   Début de chaîne de caractères ou de ligne.

    Exemple : la *regex* `^ATG` est retrouvée dans la chaîne de caractères `ATGCGT` mais pas dans la chaîne `CCATGTT`.

`$`

:   Fin de chaîne de caractères ou de ligne.

    Exemple : la *regex* `ATG$` est retrouvée dans la chaîne de caractères `TGCATG` mais pas dans la chaîne `CCATGTT`.

`.`

:   N'importe quel caractère (mais un caractère quand même).

    Exemple : la *regex* `A.G` est retrouvée dans `ATG`, `AtG`, `A4G`, mais aussi dans `A-G` ou dans `A G`.


`[ABC]`

:   Le caractère A ou B ou C (un seul caractère).

    Exemple : la *regex* `T[ABC]G` est retrouvée dans `TAG`, `TBG` ou `TCG`, mais pas dans `TG`.

`[A-Z]`

:   N'importe quelle lettre majuscule.

    Exemple : la *regex* `C[A-Z]T` est retrouvée dans `CAT`, `CBT`, `CCT`...

`[a-z]`

:   N'importe quelle lettre minuscule.

`[0-9]`

:   N'importe quel chiffre.

`[A-Za-z0-9]`

:   N'importe quel caractère alphanumérique.

`[^AB]`

:   N'importe quel caractère sauf A et B.

    Exemple : la *regex* `CG[^AB]T` est retrouvée dans `CG9T`, `CGCT`... mais pas dans `CGAT` ni dans `CGBT`.

`\`

:   Caractère d'échappement (pour protéger certains caractères).

    Exemple : la *regex* `\+` désigne le caractère `+` littéral. La *regex* `A\.G` est retrouvée dans `A.G` et non pas dans `A` suivi de n'importe quel caractère, suivi de `G`.

`*`

:   0 à *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(CG)*T` est retrouvée dans `AT`, `ACGT`, `ACGCGT`...

`+`

:   1 à *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(CG)+T` est retrouvée dans `ACGT`, `ACGCGT`... mais pas dans `AT`.

`?`

:   0 à 1 fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(CG)?T` est retrouvée dans `AT` ou `ACGT`.

`{n}`

:   *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(CG){2}T` est retrouvée dans `ACGCGT` mais pas dans `ACGT`, `ACGCGCGT` ou `ACGCG`.

`{n,m}`

:   *n* à *m* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(C){2,4}T` est retrouvée dans `ACCT`, `ACCCT` et `ACCCCT` mais pas dans `ACT`, `ACCCCCT` ou `ACCC`.

`{n,}`

:   Au moins *n* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(C){2,}T` est retrouvée dans `ACCT`, `ACCCT` et `ACCCCT` mais pas à `ACT` ou `ACCC`.

`{,m}`

:   Au plus *m* fois le caractère précédent ou l'expression entre parenthèses précédente.

    Exemple : la *regex* `A(C){,2}T` est retrouvée dans `AT`, `ACT` et `ACCT` mais pas dans `ACCCT` ou `ACC`.

`(CG|TT)`

:   Les chaînes de caractères `CG` ou `TT`.

    Exemple : la *regex* `A(CG|TT)C` est retrouvée dans `ACGC` ou `ATTC`.

Enfin, il existe des caractères spéciaux qui sont bien commodes et qui peuvent être utilisés en tant que métacaractères :

`\d`

: remplace n'importe quel chiffre (*d* signifie *digit*), équivalent à `[0-9]`.

`\w`

: remplace n'importe quel caractère alphanumérique et le caractère souligné (*underscore*) (*w* signifie *word character*), équivalent à `[0-9A-Za-z_]`.

`\s`

: remplace n'importe quel « espace blanc » (*whitespace*) (*s* signifie *space*), équivalent à `[ \t\n\r\f]`. La notion d'espace blanc a été abordée dans le chapitre 11 *Plus sur les chaînes de caractères*. Les espaces blancs les plus classiques sont l'espace ` `, la tabulation `\t`, le retour à la ligne `\n`, mais il en existe d'autres comme `\r` et `\f` que nous ne développerons pas ici. `\s` est très pratique pour détecter une combinaison d'espace(s) et/ou de tabulation(s).
\index{whitespace}
\index{espace blanc}

Comme vous le constatez, les métacaractères sont nombreux et leur signification est parfois difficile à maîtriser. Faites particulièrement attention aux métacaractères `.`, `+` et `*` qui, combinés ensemble, peuvent donner des résultats ambigus.

open-box-warn

Il est important de savoir par ailleurs que les *regex* sont « avides » (*greedy* en anglais) lorsqu'on utilise les métacaractères `+` et `*`. Cela signifie que la *regex* cherchera à « s'étendre » au maximum. Par exemple, si on utilise la *regex* `A+` pour faire une recherche dans la chaîne `TTTAAAAAAAAGC`, tous les A de cette chaîne (huit en tout) seront concernés, bien que `AA`, `AAA`, etc. « fonctionnent » également avec cette *regex*.

\index{greedy@greedy (regex)}

close-box-warn


## Quelques ressources en ligne

Nous vous conseillons de tester systématiquement vos expressions régulières sur des exemples simples. Pour vous aider, nous vous recommandons plusieurs sites internet :

- [RegexOne](https://regexone.com/) : tutoriel en ligne très bien fait.
- [RegExr](https://regexr.com/) et [ExtendsClass](https://extendsclass.com/regex-tester.html#python) : visualisent tous les endroits où une *regex* est retrouvée dans un texte.
- [pythex.org](https://pythex.org/) : interface simple et efficace, dédiée à Python.
- [Regular-Expressions.info](https://www.regular-expressions.info) : documentation exhaustive sur les *regex* (il y a même une section sur Python).

N'hésitez pas à explorer ces sites avant de vous lancer dans les exercices ou dans l'écriture de vos propres *regex* !


## Le module *re*

### La fonction `search()`

\index{search@search()}

Dans le module *re*, la fonction `search()` est incontournable. Elle permet de rechercher un motif, c'est-à-dire une *regex*, au sein d'une chaîne de caractères avec une syntaxe de la forme `search(motif, chaine)`. Si `motif` est retrouvé dans `chaine`, Python renvoie un objet du type `SRE_Match`.

Sans entrer dans les détails propres au langage orienté objet, si on utilise un objet du type `SRE_Match` dans un test, il sera considéré comme vrai. Par exemple, si on recherche le motif `tigre` dans la chaîne de caractères `"girafe tigre singe"` :

```python
>>> import re
>>> animaux = "girafe tigre singe"
>>> re.search("tigre", animaux)
<_sre.SRE_Match object at 0x7fefdaefe2a0>
>>> if re.search("tigre", animaux):
...     print("OK")
...
OK
```

open-box-warn

Le motif que vous utilisez comme premier argument de la fonction `search()` sera interprété en tant que *regex*. Ainsi, `^DEF` correspondra au mot `DEF` en début de chaîne et pas au caractère littéral `^`suivi du mot `DEF`.

close-box-warn


### Les fonctions `match()` et `fullmatch()`

\index{match@match()}

Il existe aussi la fonction `match()` dans le module `re` qui fonctionne sur le modèle de `search()`. La différence est qu'elle renvoie un objet du type `SRE_Match` seulement lorsque la *regex* correspond au début de la chaîne de caractères (à partir du premier caractère) :

```python
>>> animaux = "girafe tigre singe"
>>> re.search("tigre", animaux)
<_sre.SRE_Match object at 0x7fefdaefe718>
>>> re.match("tigre", animaux)
>>>
>>> animaux = "tigre singe"
>>> re.match("tigre", animaux)
<_sre.SRE_Match object; span=(0, 5), match='tigre'>
>>>
```

\index{fullmatch@fullmatch()}

Il existe également la fonction `fullmatch()`, qui renvoie un objet du type `SRE_Match` si et seulement si l'expression régulière correspond **exactement** à la chaîne de caractères.

```python
>>> animaux = "tigre "
>>> re.fullmatch("tigre", animaux)
>>> animaux = "tigre"
>>> re.fullmatch("tigre", animaux)
<_sre.SRE_Match object; span=(0, 5), match='tigre'>
```

De manière générale, nous vous recommandons l'usage de la fonction `search()`. Si vous souhaitez avoir une correspondance avec le début de la chaîne de caractères comme dans la fonction `match()`, vous pouvez toujours utiliser l'accroche de début de ligne `^`. Si vous voulez une correspondance exacte, comme dans la fonction `fullmatch()`, vous pouvez utiliser les métacaractères `^` et `$`, par exemple `^tigre$`.


### Compilation d'expressions régulières

\index{compile@compile()}

Lorsqu'on a besoin de tester la même expression régulière sur plusieurs milliers de chaînes de caractères, il est pratique de compiler préalablement la *regex* à l'aide de la fonction `compile()`, qui renvoie un objet de type `SRE_Pattern` :

```python
>>> regex = re.compile("^tigre")
>>> regex
<_sre.SRE_Pattern object at 0x7fefdafd0df0>
```

On peut alors utiliser directement cet objet avec la méthode `.search()` :

```python
>>> animaux = "girafe tigre singe"
>>> regex.search(animaux)
>>> animaux = "tigre singe"
>>> regex.search(animaux)
<_sre.SRE_Match object at 0x7fefdaefe718>
>>> animaux = "singe tigre"
>>> regex.search(animaux)
```


### Groupes

L'intérêt de l'objet de type `SRE_Match` renvoyé par Python lorsqu'une *regex* trouve une correspondance dans une chaîne de caractères est de pouvoir ensuite récupérer certaines zones précises :

```python
>>> regex = re.compile("([0-9]+)\.([0-9]+)")
```

\index{groupe@.group()}

Dans cet exemple, on recherche un nombre décimal, c'est-à-dire une chaîne de caractères :

- qui débute par un ou plusieurs chiffres `[0-9]+`,
- suivi d'un point `\.` (le point a d'habitude une signification de métacaractère, donc il faut l'échapper avec `\` pour qu'il retrouve sa signification de point),
- et qui se termine encore par un ou plusieurs chiffres `[0-9]+`.

Les parenthèses dans la *regex* créent des groupes (`[0-9]+` deux fois) qui seront récupérés ultérieurement par la méthode `.group()`.

```python
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

Les méthodes `.start()` et `.end()` donnent respectivement la position de début et de fin de la zone qui correspond à la *regex*. Notez que la méthode `.search()` ne renvoie que la première zone qui correspond à l'expression régulière, même s'il en existe plusieurs :

```python
>>> resultat = regex.search("pi vaut 3.14 et e vaut 2.72")
>>> resultat.group(0)
'3.14'
```


### La méthode `.findall()`

\index{findall@.findall()}

Pour récupérer chaque zone dans la *regex*, s'il y en a plusieurs, vous pouvez utiliser la méthode `.findall()` qui renvoie une liste des éléments en correspondance :

```python
>>> regex = re.compile("[0-9]+\.[0-9]+")
>>> resultat = regex.findall("pi vaut 3.14 et e vaut 2.72")
>>> resultat
['3.14', '2.72']
```

L'utilisation des groupes entre parenthèses est également possible, ceux-ci sont alors renvoyés sous la forme de tuples :

```python
>>> regex = re.compile("([0-9]+)\.([0-9]+)")
>>> resultat = regex.findall("pi vaut 3.14 et e vaut 2.72")
>>> resultat
[('3', '14'), ('2', '72')]
```


### La méthode `.sub()`

\index{sub@.sub()}

Enfin, la méthode `.sub()` permet d'effectuer des remplacements assez puissants. Par défaut, la méthode `.sub(chaine1, chaine2)` remplace toutes les occurrences trouvées par l'expression régulière dans `chaine2` par `chaine1`. Si vous souhaitez ne remplacer que les *n* premières occurrences, utilisez l'argument `count=n` :

```python
>>> regex = re.compile("[0-9]+\.[0-9]+")
>>> regex.sub("quelque chose", "pi vaut 3.14 et e vaut 2.72")
'pi vaut quelque chose et e vaut quelque chose'
>>> regex.sub("quelque chose", "pi vaut 3.14 et e vaut 2.72", count=1)
'pi vaut quelque chose et e vaut 2.72'
```

Encore plus puissant, il est possible d'utiliser dans le remplacement des groupes qui ont été « capturés » avec des parenthèses :

```python
>>> regex = re.compile("([0-9]+)\.([0-9]+)")
>>> phrase = "pi vaut 3.14 et e vaut 2.72"
>>> regex.sub("approximativement \\1", phrase)
'pi vaut approximativement 3 et e vaut vaut approximativement 2'
>>> regex.sub("approximativement \\1 (puis .\\2)",phrase)
'pi vaut approximativement 3 (puis .14) et e vaut approximativement 2 (puis .72)'
```

Si vous avez capturé des groupes, il suffit d'utiliser `\\1`, `\\2` (etc.) pour utiliser les groupes correspondants dans la chaîne de caractères substituée. On notera que la syntaxe générale pour récupérer des groupes dans les outils qui gèrent les *regex* est `\1`, `\2`, etc. Toutefois, Python nous oblige à mettre un deuxième *backslash* car il y a ici deux niveaux : un premier niveau Python où on veut mettre un *backslash* littéral (donc `\\`), puis un second niveau *regex* dans lequel on veut retrouver `\1`. Si cela est confus, retenez seulement qu'il faut mettre un `\\` devant le numéro de groupe.

Enfin, sachez que la réutilisation d'un groupe précédemment capturé est aussi utilisable lors d'une utilisation classique de *regex*. Par exemple :

```python
>>> re.search("(pan)\\1", "bambi et panpan")
<_sre.SRE_Match object; span=(9, 15), match='panpan'>
>>> re.search("(pan)\\1", "le pistolet a fait pan !")
>>>
```

Dans la *regex* `(pan)\\1`, on capture d'abord le groupe `(pan)` grâce aux parenthèses (il s'agit du groupe 1, puisque c'est le premier jeu de parenthèses), immédiatement suivi du même groupe grâce au `\\1`. Dans cet exemple, on capture donc le mot `panpan` (lignes 1 et 2). Si, par contre, on a une seule occurrence du mot `pan`, cette *regex* ne fonctionne pas, ce qui est le cas ligne 3.

Bien sûr, si on avait eu un deuxième groupe, on aurait pu le réutiliser avec `\\2`, un troisième groupe avec `\\3`, etc.


Nous espérons vous avoir convaincu de la puissance du module *re* et des expressions régulières. Alors, plus de temps à perdre, à vos *regex* !


## Exercices

open-box-adv

Pour ces exercices, créez des scripts puis exécutez-les dans un *shell*.

close-box-adv


### *Regex* de base

\index{GenBank@GenBank}

Dans cet exercice, nous allons manipuler le fichier GenBank [`NC_001133.gbk`](https://python.sdv.u-paris.fr/data-files/NC_001133.gbk) correspondant au chromosome I de la levure *Saccharomyces cerevisiae*.

Créez un script `regex_genbank.py` :

- qui recherche le mot `DEFINITION` en début de ligne dans le fichier GenBank, puis affiche la ligne correspondante ;
- qui recherche tous les journaux (mot-clé `JOURNAL`) dans lesquels ont été publiés les travaux sur cette séquence, puis affiche les lignes correspondantes.

open-box-adv

- Utilisez des *regex* pour trouver les lignes demandées.
- Des explications sur le format GenBank et des exemples de code sont fournies dans l'annexe A *Quelques formats de données en biologie*.

close-box-adv


### Enzyme de restriction

Une enzyme de restriction est une protéine capable de couper une molécule d'ADN. Cette coupure se fait sur le site de restriction de l'ADN qui correspond à une séquence particulière de nucléotides (bases).

Pour chacune des enzymes ci-dessous, déterminez les expressions régulières qui décrivent leurs sites de restriction. Le symbole N correspond aux bases A, T, C ou G. W correspond à A ou T. Y correspond à C ou T. R correspond à A ou G.

| Enzyme  | Site de restriction |
|---------|--------------|
| HinFI   | GANTC        |
| EcoRII  | CCWGG        |
| BbvBI   | GGYRCC       |
| BcoI    | CYCGRG       |
| Psp5II  | RGGWCCY      |
| BbvAI   | GAANNNNTTC   |


### Nettoyeur d'espaces

Le fichier [`cigale_fourmi.txt`](https://python.sdv.u-paris.fr/data-files/cigale_fourmi.txt) contient la célèbre fable de Jean de la Fontaine. Malheureusement, la personne qui l'a recopié a parfois mis plusieurs espaces au lieu d'un seul entre les mots.

Créez un script `cigale_fourmi.py` qui, grâce à une *regex* et à la fonction `sub()`, remplace plusieurs espaces par un seul dans le texte ci-dessus. Le nouveau texte, ainsi nettoyé, sera enregistré dans un fichier `cigale_fourmi_propre.txt`.


### Liste des protéines humaines

\index{FASTA}

Téléchargez le fichier [`human-proteome.fasta`](https://python.sdv.u-paris.fr/data-files/human-proteome.fasta) qui contient le protéome humain, c'est-à-dire les séquences de l'ensemble des protéines chez l'Homme. Ce fichier est au format FASTA.

On souhaite lister toutes ces protéines et les indexer avec un numéro croissant.

Créez un script `liste_proteome.py` qui :

- lit le fichier `human-proteome.fasta` ;
- extrait, avec une *regex*, le numéro d'accession de la protéine de toutes les lignes de commentaires des séquences ;
- affiche le mot `protein`, suivi d'un numéro qui s'incrémente, suivi du numéro d'accession.

Voici un exemple de sortie attendue :

```text
protein 00001 O95139
protein 00002 O75438
protein 00003 Q8N4C6
[...]
protein 20371 Q8IZJ1
protein 20372 Q9UKP6
protein 20373 Q96HZ7
```

open-box-adv

- Des explications sur le format FASTA et des exemples de code sont fournis dans l'annexe A *Quelques formats de données en biologie*.
- La ligne de commentaire d'une séquence au format FASTA est de la forme  
    `>sp|O95139|NDUB6_HUMAN NADH dehydrogenase [...]`  
    Elle débute toujours pas le caractère `>`.
    Le numéro d'accession `O95139` se situe entre le premier et le second symbole `|` (symbole *pipe*). Attention, il faudra « échapper » ce symbole car il a une signification particulière dans une *regex*.
- Le numéro qui s'incrémente débutera à 1 et sera affiché sur 5 caractères, avec des 0 à sa gauche si nécessaires (formatage `{:05d}`).

close-box-adv


### Le défi du dé-HTMLiseur (exercice +++)

Le format HTML permet d'afficher des pages web dans un navigateur. Il s'agit d'un langage à balise qui fonctionne avec des balises ouvrantes `<balise>` et des balises fermantes `</balise>`.

Créez un script `dehtmliseur.py` qui lit le fichier [`fichier_a_dehtmliser.html`](https://python.sdv.u-paris.fr/data-files/fichier_a_dehtmliser.html) au format HTML et qui renvoie à l'écran tout le texte de ce fichier sans les balises HTML.

Nous vous conseillons tout d'abord d'ouvrir le fichier HTML dans un éditeur de texte et de bien l'observer. N'hésitez pas à vous aider des sites mentionnés dans les ressources en ligne.


### Nettoyeur de doublons (exercice +++)

Téléchargez le fichier [`breves_doublons.txt`](https://python.sdv.u-paris.fr/data-files/breves_doublons.txt) qui contient des mots répétés deux fois. Par exemple :

```text
Le cinéma est devenu parlant, la radio radio finira en images.
La sardine, c'est un petit petit poisson sans tête qui vit dans l'huile.
[...]
```

Écrivez un script `ote_doublons.py` qui lit le fichier `breves_doublons.txt` et qui supprime tous les doublons à l'aide d'une *regex*. Le script affichera le nouveau texte à l'écran.

open-box-adv

Utilisez la méthode `.sub()`.

close-box-adv
