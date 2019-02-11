# Introduction


## Avant de commencer

Pour apprendre la programmation Python, il va falloir que vous pratiquiez et pour cela il est préférable que Python soit installé sur votre ordinateur. La bonne nouvelle est que vous pouvez installer gratuitement Python sur votre machine, que ce soit sous Windows, Mac OS X ou Linux. Si Python n'est pas déjà installé sur votre machine, consultez l'annexe B *Installation de Python* qui explique la marche à suivre.

L'apprentissage d'un langage informatique comme Python va nécessiter d'écrire des lignes de codes à l'aide d'un éditeur de texte. Si vous êtes débutants, on vous conseille d'utiliser *notepad++* sous Windows, *TextWrangler* ou *BBedit* sous Mac OS X et *gedit* sous Linux. La configuration de ces éditeurs de texte est détaillée dans l'annexe B *Installation de Python*. Bien sur, si vous préférez d'autres éditeurs comme *Atom*, *Visual Studio Code*, *Sublime Text*, *emacs*, *vim*, *geany*... utilisez-les. À toute fin utile, on rappelle néanmoins que les logiciels *Microsoft Word*, *WordPad* et *LibreOffice Writer* ne sont pas des éditeurs de texte, ce sont des traitements de texte qui ne peuvent pas et ne doivent pas être utilisés pour écrire du code informatique.


## C'est quoi Python ?

Le langage de programmation Python a été créé en 1989 par Guido van Rossum, aux Pays-Bas. Le nom *Python* vient d'un hommage à la série télévisée *Monty Python's Flying Circus* dont G. van Rossum est fan. La première version publique de ce langage a été publiée en 1991.

La dernière version de Python est la version 3. Plus précisément, la version 3.7 a été publiée en juin 2018. Ce cours est basé sur Python 3. La version 2 de Python est désormais obsolète, dans la mesure du possible évitez de l'utiliser.

La *Python Software Foundation* est l'association qui organise le développement de Python et anime la communauté de développeurs et d'utilisateurs.

Ce langage de programmation présente de nombreuses caractéristiques intéressantes :

- Il est multiplateforme. C'est-à-dire qu'il fonctionne sur de nombreux systèmes d'exploitation : Windows, Mac OS, Linux, Android, iOS, depuis les mini-ordinateurs Raspberry Pi jusqu'aux supercalculateurs.
- Il est gratuit. Vous pouvez l'installer sur autant d'ordinateurs que vous voulez.
- C'est un langage de haut niveau. Il demande relativement peu de connaissance sur le fonctionnement d'un ordinateur pour être utilisé.
- C'est un langage interprété. Chaque script Python n'a pas besoin d'être compilé pour pouvoir l'utiliser, contrairement à des langages comme le C ou le C++.
- Il est orienté objet. C'est-à-dire qu'il est possible de créer en Python des entités qui ont un sens dans le monde réel (une cellule, une protéine, un atome) avec un certain nombre de fonctionnements et d'interactions.
- Il est relativement *simple* à prendre en main[^footnote].
- Enfin, il est très utilisé en bioinformatique et plus généralement en analyse de données.

[^footnote]: Nous sommes d'accord, cette notion est très relative.

Toutes ces caractéristiques font que Python est désormais enseigné dans de nombreuses formations, depuis l'enseignement secondaire jusqu'à l'enseignement supérieur.


## Notations utilisées

Dans cet ouvrage, les commandes, les instructions Python, les résultats et les contenus de fichiers
sont indiqués avec `cette police` pour les éléments ponctuels ou
```
sous cette forme,
sur plusieurs lignes,
pour les éléments les plus longs.
```

Pour ces derniers, le numéro à gauche indique le numéro de la ligne et sera utilisé
pour faire référence à une instruction particulière. Ce numéro n'est bien sûr là qu'à titre indicatif.

Par ailleurs, dans le cas de programmes, de contenus de fichiers ou de résultats trop longs pour être inclus dans leur intégralité, la notation `[...]` indique une coupure arbitraire de plusieurs caractères ou lignes.


## Premier contact avec Python

Python est un langage interprété, c'est-à-dire que chaque ligne de code est lue puis interprétée afin d'être exécutée par l'ordinateur. Pour vous en rendre compte, ouvrez un *shell*, puis lancez la commande :

`python`


open-box-rem

Si vous ne savez pas ou avez oublié ce qu'est un *shell*, consultez la rubrique *Qu'appelle-t-on le shell ?* de l'annexe C *Installation de Python*.

close-box-rem


La commande précédente va lancer l'**interpréteur Python**. Vous devriez obtenir quelque chose de ce style pour Windows :
```
(base) C:\Users\pierre>python
Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] [...]
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

pour Mac OS X :
```
iMac-de-LBM-516b:Downloads lbm_516b$ python
Python 3.7.0 (default, Jun 28 2018, 07:39:16)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

ou pour Linux :
```
(base) pierre@jeera:~$ python
Python 3.7.0 (default, Jun 28 2018, 13:15:42)
[GCC 7.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Les blocs

- `(base) C:\Users\pierre>` pour Windows,
- `iMac-de-LBM-516b:Downloads lbm_516b$` pour Mac OS X
- et `(base) pierre@jeera:~$` pour Linux

représentent l'invite de commande de votre *shell*. Par la suite, cette invite de commande sera représentée simplement par le caractère `$`, que vous soyez sous Windows, Mac OS X ou Linux.

Le triple chevron `>>>` est l'invite de commande de Python (*prompt* en anglais), ce qui signifie que Python attend une commande.
Tapez par exemple l'instruction

`print("Hello world!")`

puis validez votre commande en appuyant sur la touche `Entrée`.

Python a exécuté la commande directement et a affiché le texte `Hello world!`. Il attend ensuite votre prochaine instruction en affichant l'invite de l'interpréteur Python (`>>>`). En résumé, voici ce qui a dû apparaître sur votre écran :
```
>>> print("Hello world!")
Hello world!
>>>
```
Vous pouvez refaire un nouvel essai en vous servant cette fois de l'interpréteur comme d'une calculatrice.
```
>>> 1+1
2
>>> 6*3
18
```
À ce stade, vous pouvez entrer une autre commande ou bien quitter l'interpréteur Python, soit en tapant la commande `exit()` puis en validant en appuyant sur la touche `Entrée`, soit en pressant simultanément les touches `Ctrl` et `D`.

L'interpréteur Python est donc un système interactif dans lequel vous pouvez entrer des commandes, que Python exécutera sous vos yeux (au moment où vous validerez la commande en appuyant sur la touche `Entrée`).

Il existe de nombreux autres langages interprétés tels que [Perl](http://www.perl.org) ou [R](http://www.r-project.org). Le gros avantage de ce type de langage est qu'on peut immédiatement tester une commande à l'aide de l'interpréteur, ce qui est très utile pour débugger (c'est-à-dire corriger les éventuelles erreurs d'un programme). Gardez bien en mémoire cette propriété de Python qui pourra parfois vous faire gagner un temps précieux !


## Premier programme en Python

Bien sûr, l'interpréteur présente vite des limites dès lors que l'on veut exécuter une suite d'instructions plus complexe. Comme tout langage informatique, on peut enregistrer ces instructions dans un fichier, que l'on appelle communément un script Python.

Pour reprendre l'exemple précédent, ouvrez un éditeur de texte (pour choisir et configurer un éditeur de texte, reportez-vous si nécessaire à l'annexe B *Installation de Python*) et entrez le code suivant :  
`print("Hello world!")`

Ensuite, enregistrez votre fichier sous le nom `test.py`, puis quittez l'éditeur de texte.

open-box-rem

L'extension de fichier standard des scripts Python est `.py`.

close-box-rem

Pour exécuter votre script, ouvrez un *shell*  et entrez la commande :  
`python test.py`

Vous devriez obtenir un résultat similaire à ceci :
```
$ python test.py
Hello world!
```

Si c'est bien le cas, bravo ! Vous avez exécuté votre premier programme Python.


## Commentaires

Dans un script, tout ce qui suit le caractère `#` est ignoré par Python
jusqu'à la fin de la ligne et est considéré comme un commentaire.

Les commentaires doivent expliquer votre code dans un langage humain.
L'utilisation des commentaires est rediscutée dans le chapitre 15 *Bonnes pratiques en programmation Python*.

Voici un exemple :

```
# votre premier commentaire en  Python
print('Hello world!')

# d'autres commandes plus utiles pourraient suivre
```

open-box-rem

On appelle souvent à tord le caractère `#` « dièse ». On devrait plutôt parler de « [croisillon](https://fr.wikipedia.org/wiki/Croisillon_(signe)) ».

close-box-rem


## Notion de bloc d'instructions et d'indentation

Pour terminer ce chapitre, nous allons aborder les notions de **bloc d'instructions** et d'**indentation**.

En programmation, il est courant de répéter un certain nombre de choses (avec les boucles, voir le chapitre 5 *Boucles et comparaisons*) ou de faire des choix (avec les tests, voir le chapitre 6 *Tests*).

Par exemple, on souhaite répéter 10 fois 3 instructions différentes, les unes à la suite des autres. Voici ce que cela donnerait avec du pseudo-code (c'est-à-dire avec des instructions qui n'existent pas en Python) :
```
instruction_qui_répète_10_fois_ce_qui_suit:
    instruction_1
    instruction_2
    instruction_3
instruction_suivante
```

Ligne 1. Cette instruction va indiquer à Python de répéter 10 fois d'autres instructions (il s'agit d'une boucle, on verra la commande exacte plus tard). Cette instruction se termine par le symbole **:** qui indique à Python qu'il doit attendre un bloc d'instructions.

Lignes 2 à 4. Les 3 instructions à répéter sont `instruction_1`, `instruction_2` et `instruction_3` . Ces instructions constituent un bloc d'instructions car elles sont indentées. L'**indentation est le décalage vers la droite d'un bloc d'instructions**. L'indentation peut être réalisée par des espaces ou des tabulations. Pratiquement, l'indentation en Python doit être homogène (soit des espaces, soit des tabulations, mais pas un mélange des deux). Une indentation avec 4 espaces est le style d'indentation recommandé (voir le chapitre 15 *Bonnes pratiques en programmation Python*).

Ligne 5. Enfin, la ligne `instruction_suivante` est exécutée une fois que le bloc d'instructions est terminé.

Si tout cela semble un peu complexe, ne vous inquiétez pas. Vous allez comprendre tous ces détails chapitre après chapitre.


## Python 2 ou Python 3 ?

Ce cours est basé sur la version 3 de Python, qui est maintenant devenu un standard. Par ailleurs, Python 2 cessera d'être maintenu après le 1er janvier 2020. Python 3 est donc la version à utiliser.

Si, néanmoins, vous devez un jour travailler sur un ancien programme écrit en Python 2, sachez qu'il existe quelques différences importantes entre Python 2 et Python 3. Le chapitre 21 *Remarques complémentaires* vous apportera plus de précisions.
