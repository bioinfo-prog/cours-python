# Affichage

## La fonction `print()`

Dans le chapitre 1, nous avons rencontré la fonction `print()` qui affiche une chaîne de caractères (le fameux `"Hello world!"`). Elle peut également afficher le contenu d'une ou plusieurs variables :
```
>>> x = 32
>>> nom = "John"
>>> print(nom , "a" , x , "ans")
John a 32 ans
```
Python a donc écrit une phrase complète en remplaçant les variables `x` et `nom` par leur contenu. Vous remarquerez que pour afficher plusieurs éléments de texte sur une seule ligne, nous avons utilisé le séparateur `,` entre les différents éléments. Python a également ajouté un espace à chaque fois que l'on utilisait le séparateur `,`. On peut modifier ce comportement en passant à la fonction `print()` l'argument par « mot clé » `sep` (la notion d'argument par « mot clé » sera détaillée dans le chapitre 9 *Fonctions*) :
```
>>> x = 32
>>> nom = "John"
>>> print(nom , "a" , x , "ans", sep="")
Johna32ans
>>> print(nom , "a" , x , "ans", sep="-")
John-a-32-ans
```

Pour imprimer deux chaînes de caractères l'une à côté de l'autre sans espace, vous devrez les concaténer :
```
>>> ani1 = "chat"
>>> ani2 = "souris"
>>> print(ani1, ani2)
chat souris
>>> print(ani1 + ani2)
chatsouris
```


## Écriture formatée

La méthode `.format()` permet une meilleure organisation de l'affichage des variables (nous expliquerons à la fin de ce chapitre ce que signifie le terme *méthode* en Python).

Si on reprend l'exemple précédent :
```
>>> x = 32
>>> nom = "John"
>>> print("{} a {} ans".format(nom, x))
John  a  32  ans
```
- Dans la chaîne de caractères, les accolades vides `{}` précisent l'endroit où le contenu de la variable doit être inséré.
- Juste après la chaîne de caractères, l'instruction `.format(nom, x)` fournie la liste des variables à insérer, d'abord la variable `nom` puis la variable `x`. La méthode `.format()` agit sur la chaîne de caractères à laquelle elle est attachée par le point.

open-box-rem

Il est possible d'indiquer entre les accolades `{}` dans quel ordre afficher les variables, avec 0 pour la variable à afficher en premier, 1 pour la variable à afficher en second, etc. (attention, Python commence à compter à 0). Cela permet de modifier l'ordre dans lequel sont affichées les variables.

```
>>> x = 32
>>> nom = "John"
>>> print("{0} a {1} ans".format(nom, x))
John a 32  ans
>>> print("{1} a {0} ans".format(nom, x))
32 a John ans
```
close-box-rem

Imaginez maintenant que vous vouliez calculer, puis afficher, la proportion de GC d'un génome. La proportion de GC s'obtient comme la somme des bases Guanine (G) et Cytosine (C) divisée par le nombre total de bases (A, T, C, G) du génome considéré. Si on a, par exemple, 4500 bases G et 2575 bases C, pour un total de 14800 bases, vous pourriez procéder comme suit (notez bien l'utilisation des parenthèses pour gérer les priorités des opérateurs) :
```
>>> prop_GC = (4500 + 2575) / 14800
>>> print("La proportion de GC est", prop_GC)
La proportion de GC est 0.4780405405405405
```
Le résultat obtenu présente trop de décimales (seize dans le cas présent). Pour écrire le résultat plus lisiblement, vous pouvez spécifier dans les accolades `{}` le format qui vous intéresse. Dans le cas présent, vous voulez formater un *float* pour l'afficher avec deux puis trois décimales :

```
>>> print("La proportion de GC est {:.2f}".format(prop_GC))
Le proportion de GC est 0.48
>>> print("La proportion de GC est {:.3f}".format(prop_GC))
La proportion de GC est 0.478
```

Détaillons le contenu des accolades de la première ligne (`{:.2f}`) :

- Les deux points `:` indiquent qu'on veut préciser le format.
- La lettre `f` indique qu'on souhaite afficher la variable sous forme d'un *float*.
- Les caractères `.2` indiquent la précision voulue, soit ici deux chiffres après la virgule.

Notez enfin que le formatage avec `.xf` (`x` étant un entier positif) renvoie un résultat arrondi.

Il est par ailleurs possible de combiner le formatage (à droite des 2 points) ainsi que l'emplacement des variables à substituer (à gauche des 2 points), par exemple :
```
>>> print("prop GC(2 déci.) = {0:.2f}, prop GC(3 déci.) = {0:.3f}".format(prop_GC))
prop GC(2 déci.) = 0.48, prop GC(3 déci.) = 0.478
```
Vous remarquerez qu'on utilise ici la même variable (`prop_GC`) à deux endroits différents.

Vous pouvez aussi formater des entiers avec la lettre `d`,
```
>>> nb_G = 4500
>>> print("Ce génome contient {:d} guanines".format(nb_G))
Ce génome contient 4500 guanines
```
ou mettre plusieurs nombres dans une même chaîne de caractères.
```
>>> nb_G = 4500
>>> nb_C = 2575
>>> print("Ce génome contient {:d} G et {:d} C, soit une prop de GC de {:.2f}" \
... .format(nb_G,nb_C,prop_GC))
Ce génome contient 4500 G et 2575 C, soit une prop de GC de 0.48
>>> perc_GC = prop_GC * 100
>>> print "Ce génome contient {:d} G et {:d} C, soit un %GC de {:.2f} %" \
... .format(nb_G,nb_C,perc_GC)
Ce génome contient 4500 G et 2575 C, soit un %GC de 47.80 %
```

open-box-rem

Le signe `\` en fin de ligne permet de poursuivre la commande sur la ligne suivante. Cette syntaxe est pratique lorsque vous voulez taper une commande longue.

close-box-rem

Enfin, il est possible de préciser sur combien de caractères vous voulez qu'un résultat soit écrit et comment se fait l'alignement (à gauche, à droite ou centré). Dans la portion de code suivante, le caractère `;` sert de séparateur entre les instructions sur une même ligne :
```
>>> print(10) ; print(1000)
10
1000
>>> print("{:>6d}".format(10)) ; print("{:>6d}".format(1000))
    10
  1000
>>> print("{:<6d}".format(10)) ; print("{:<6d}".format(1000))
10    
1000
>>> print("{:^6d}".format(10)) ; print("{:^6d}".format(1000))
  10  
 1000
>>> print("{:*^6d}".format(10)) ; print("{:*^6d}".format(1000))
**10**
*1000*
>>> print("{:0>6d}".format(10)) ; print("{:0>6d}".format(1000))
000010
001000
```

Notez que `>` spécifie un alignement à droite, `<` spécifie un alignement à gauche et `^` spécifie un alignement centré. Il est également possible d'indiquer le caractère qui servira de remplissage lors des alignements (l'espace est le caractère par défaut).

Ce formatage est également possible sur des chaînes de caractères, notées `s` (comme *string*) :
```
>>> print("atom HN") ; print("atom HDE1")
atom HN
atom HDE1
>>> print("atom {:>4s}".format("HN")) ; print("atom {:>4s}".format("HDE1"))
atom   HN
atom HDE1
```

Vous voyez tout de suite l'énorme avantage de l'écriture formatée. Elle vous permet d'écrire en colonnes parfaitement alignées. Nous verrons que ceci est très pratique si l'on veut écrire les coordonnées des atomes d'une molécule au format PDB (pour en savoir plus sur ce format, reportez-vous à l'annexe A *Quelques formats de données rencontrés en biologie*).

Pour les *floats*, il est possible de combiner le nombre de caractères à afficher avec le nombre de décimales :
```
>>> print("{:7.3f}".format(perc_GC))
 47.804
>>> print("{:10.3f}".format(perc_GC))
    47.804
```

L'instruction `7.3f` signifie que l'on souhaite écrire le *float* avec 3 décimales et formaté sur 7 caractères (par défaut justifiés à droite). L'instruction `10.3f` fait la même chose sur 10 caractères. Remarquez que le séparateur décimal `.` compte pour un caractère.

Enfin, si on veut afficher des accolades littérales et utiliser la méthode `.format()` en même temps, il faut doubler les accolades pour échapper au formatage :
```
>>> print("Accolades littérales {{}} et pour le formatage {}".format(10))
Accolades littérales {} et pour le formatage 10
```

La méthode `.format()` agit sur la chaîne de caractères à laquelle elle est *attachée* par un `.` et n'a rien à voir avec la fonction `print()`. Si on donne une chaîne de caractères suivie d'un `.format()` à la fonction `print()`, Python évalue d'abord le formatage et c'est la chaîne de caractères qui en résulte qui est affichée à l'écran. Tout comme dans l'instruction `print(5*5)`, c'est d'abord la multiplication (`5*5`) qui est évaluée, puis son résultat qui est affiché à l'écran. On peut s'en rendre compte de la manière suivante dans l'interpréteur :
```
>>> "{:10.3f}".format(perc_GC)
'    47.804'
>>> type("{:10.3f}".format(perc_GC))
<class 'str'>
```
Python affiche le résultat de l'instruction `"{:10.3f}".format(perc_GC)` comme une chaîne de caractères et la fonction `type()` nous le confirme.


## Ancienne méthode de formatage des chaînes de caractères

*Conseil* : Pour les débutants, vous pouvez passer cette section.

Dans d'anciens livres ou programmes Python, il se peut que vous rencontriez l'écriture formatée avec le style suivant :
```
>>> x = 32
>>> nom = "John"
>>> print("%s a %d ans" % (nom, x))
John a 32 ans
>>> nb_G = 4500
>>> nb_C = 2575
>>> prop_GC = (nb_G + nb_C)/14800
>>> print("On a %d G et %d C -> prop GC = %.2f" % (nb_G, nb_C, prop_GC))
On a 4500 G et 2575 C -> prop GC = 0.48
```
La syntaxe est légèrement différente. Le symbole `%` est d'abord appelé dans la chaîne de caractères (dans l'exemple ci-dessus `%d`, `%d` et `%.2f`) pour :

- Désigner l'endroit où sera placée la variable dans la chaîne de caractères.
- Préciser le type de variable à formater, `d` pour un entier (`i` fonctionne également) ou `f` pour un *float*.
- Éventuellement pour indiquer le format voulu. Ici `.2` signifie une précision de deux décimales.

Le signe `%` est rappelé une seconde fois (`% (nb_G, nb_C, prop_GC)`) pour indiquer les variables à formater.

Cette ancienne façon de formater vous est présentée à titre d'information. Ne l'utilisez pas dans vos programmes.


## Note sur le vocabulaire et la syntaxe

Revenons quelques instants sur la notion de **méthode** abordée dans ce chapitre avec `.format()`. En Python, on peut considérer chaque variable comme un objet sur lequel on peut appliquer des méthodes. Une méthode est simplement une fonction qui utilise et/ou agit sur l'objet lui-même, les deux étant connectés par un point. La syntaxe générale est du type `objet.méthode()`.

Dans l'exemple suivant :
```
>>> "Joe a {} ans".format(20)
'Joe a 20 ans'
```
la méthode `.format()` est liée à `"Joe a {} ans"` qui est un objet de type chaîne de caractères. La méthode renvoie une nouvelle chaîne de caractères avec le bon formatage (ici, `'Joe a 20 ans'`).

Nous aurons de nombreuses occasions de revoir cette notation `objet.méthode()`.


## Exercices

*Conseil* : utilisez l'interpréteur Python pour les exercices 2 à 5.


### Affichage dans l'interpréteur et dans un programme

Ouvrez l'interpréteur Python et tapez l'instruction `1+1`. Que se passe-t-il ?

Écrivez la même chose dans un script `test.py` que vous allez créer avec un éditeur de texte. Exécutez ce script en tapant `python3 test.py` dans un *shell*. Que se passe-t-il ? Pourquoi ? Faites en sorte d'afficher le résultat de l'addition `1+1` en exécutant le script dans un *shell*.


### Poly-A

Générez une chaîne de caractères représentant un brin d'ADN poly-A (c'est-à-dire qui ne contient que des bases A) de 20 bases de longueur, sans taper littéralement toutes les bases.


### Poly-A et poly-GC

Suivant le modèle de l'exercice précédent, générez en une ligne de code un brin d'ADN poly-A (AAAA...) de 20 bases suivi d'un poly-GC régulier (GCGCGC...) de 40 bases.


### Écriture formatée

En utilisant l'écriture formatée, affichez en une seule ligne les variables `a`, `b` et `c` dont les valeurs sont respectivement la chaîne de caractères `"salut"`, le nombre entier `102` et le *float* `10.318`. La variable `c` sera affichée avec 2 décimales.


### Écriture formatée 2

Dans un script `percGC.py`, calculez un pourcentage de GC avec l'instruction suivante :

`perc_GC = ((4500 + 2575)/14800)*100`

Ensuite, affichez le contenu de la variable `perc_GC` à l'écran avec 0, 1, 2 puis 3 décimales sous forme arrondie en utilisant `.format()`. On souhaite que le programme affiche la sortie suivante :
```
Le pourcentage de GC est 48     %
Le pourcentage de GC est 47.8   %
Le pourcentage de GC est 47.80  %
Le pourcentage de GC est 47.804 %
```
