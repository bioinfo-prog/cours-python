# Affichage

Nous avons déjà vu au chapitre 1 la fonction `print()` qui permet d'afficher une chaîne de caractères. Elle permet en plus d'afficher le contenu d'une ou plusieurs variables :

    >>> x = 32
    >>> nom = 'John'
    >>> print(nom , ' a ' , x , ' ans')
    John  a  32  ans

Python a donc écrit la phrase en remplaçant les variables `x` et `nom` par leur contenu. Vous pouvez noter également que pour écrire plusieurs blocs de texte sur une seule ligne, nous avons utilisé le séparateur `,` avec la fonction `print()`. En regardant de plus près, vous vous aperçevrez que Python a automatiquement ajouté un espace à chaque fois que l'on utilisait le séparateur `,`. Par conséquent, si vous voulez mettre un seul espace entre chaque bloc, vous pouvez retirer ceux de vos chaînes de caractères :

    >>> print(nom , 'a' , x , 'ans')
    John a 32 ans

Pour imprimer deux chaînes de caractères l'une à côté de l'autre sans espace, vous devrez les concaténer :

    >>> ani1 = 'chat'
    >>> ani2 = 'souris'
    >>> print(ani1, ani2)
    chat souris
    >>> print(ani1 + ani2)
    chatsouris

## Écriture formatée

La méthode `.format()` permet une meilleure organisation de l'affichage des variables (nous expliquerons à la fin de ce chapitre ce que signifie le terme *méthode* en Python).

Si on reprend l'exemple précédent :

    >>> x = 32
    >>> nom = 'John'
    >>> print('{} a {} ans'.format(nom, x))
    John  a  32  ans

- Dans la chaîne de caractères, les accolades vides `{}` précisent l'endroit où le contenu de la variable doit être inséré.
- Juste après la chaîne de caractères, l'instruction `.format(nom, x)` indique la liste des variables à insérer, d'abord la variable `nom` puis la variable `x`. Ainsi, la méthode `.format()` agit sur la chaîne de caractères à laquelle elle est attachée par le `.`.

open-box-rem

Il est possible d'indiquer entre les accolades `{}` dans quel ordre afficher les variables, avec 0 pour la variable à afficher en premier, 1 pour la variable à afficher en second, etc. (attention, Python commence à compter à 0). Cela permet de modifier l'ordre dans lequel sont affichées les variables.
```
>>> x = 32
>>> nom = 'John'
>>> print('{0} a {1} ans'.format(nom, x))
John a 32  ans
>>> print('{1} a {0} ans'.format(nom, x))
32 a John ans
```
close-box-rem

Imaginez maintenant que vous vouliez calculer puis afficher la proportion de GC d'un génome. La proportion de GC s'obtient comme la somme des bases Guanine (G) et Cytosine (C) divisée par le nombre total de bases (A, T, C, G) du génome considéré. Si on a, par exemple, 4500 bases G, 2575 bases C pour un total de 14800 bases, vous pourriez faire comme suit (notez bien l'utilisation des parenthèses pour gérer les priorités des opérateurs) :

    >>> propGC = (4500 + 2575) / 14800
    >>> print("La proportion de GC est", propGC)
    La proportion de GC est 0.4780405405405405

Le résultat obtenu présente trop de décimales (seize dans le cas présent)... Pour écrire le résultat plus lisiblement, vous pouvez spécifier dans les accolades `{}` le format qui vous intéresse. Dans votre cas, vous voulez formater un réel (*float*) pour l'afficher avec deux puis trois décimales :

```
>>> print("La proportion de GC est {:.2f}".format(propGC))
Le proportion de GC est 0.48
>>> print("La proportion de GC est {:.3f}".format(propGC))
La proportion de GC est 0.478
```

Détaillons le contenu des accolades de la première ligne (`{:.2f}`) :

- Les deux points `:` indiquent qu'on veut préciser le format.
- La lettre `f` indique qu'on souhaite afficher la variable sous forme d'un réel (*float*).
- Les caractères `.2` indiquent la précision voulue, soit ici deux chiffres après la virgule.

Notez enfin que le formatage avec `.xf` (`x` étant un entier positif) renvoie un résultat arrondi.

Il est par ailleurs possible de combiner le formatage (à droite des 2 points) ainsi que l'emplacement des variables à substituer (à gauche des 2 points), par exemple :

    >>> print("propGC(2 décimales) = {0:.2f}, propGC(3 décimales) = {0:.3f}".format(propGC))
    propGC(2 décimales) = 0.48, propGC(3 décimales) = 0.478

Vous remarquerez qu'on utilise ici la même variable (`propGC`) à deux endroits différents.

Vous pouvez aussi formater des entiers avec `d`,

    >>> nbG = 4500
    >>> print("Le génome de cet exemple contient {:d} guanines".format(nbG))
    Le génome de cet exemple contient 4500 guanines

ou mettre plusieurs nombres dans une même chaîne de caractères.

    >>> nbG = 4500
    >>> nbC = 2575
    >>> print("Ce génome contient {:d} G et {:d} C, soit une prop de GC de {:.2f}" \
    ... .format(nbG,nbC,propGC))
    Ce génome contient 4500 G et 2575 C, soit une prop de GC de 0.48
    >>> percGC = propGC * 100
    >>> print "Ce génome contient {:d} G et {:d} C, soit un %GC de {:.2f} %" \
    ... .format(nbG,nbC,percGC)
    Ce génome contient 4500 G et 2575 C, soit un %GC de 47.80 %

**Remarque** : Le signe `\` en fin de ligne permet de poursuivre la commande sur la ligne suivante. Cette syntaxe est pratique lorsque vous voulez taper une commande longue.

Enfin, il est possible de préciser sur combien de caractères vous voulez qu'un résultat soit écrit et comment se fait l'alignement (à gauche, à droite ou centré). Dans la portion de code suivant, le caractère `;` sert de séparateur entre les instructions sur une même ligne :

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

Notez que `>` spécifie un alignement à droite, `<` spécifie un alignement à gauche et `^` spécifie un alignement centré. Il est également possible d'indiquer le caractère qui servira de remplissage lors des alignements (l'espace par défaut).

Ce formatage est également possible sur des chaînes de caractères, notées `s` (comme *string*) :

    >>> print("atom HN") ; print("atom HDE1")
    atom HN
    atom HDE1
    >>> print("atom {:>4s}".format("HN")) ; print("atom {:>4s}".format("HDE1"))
    atom   HN
    atom HDE1

Vous voyez tout de suite l'énorme avantage de l'écriture formatée. Cela vous permet d'écrire en colonnes parfaitement alignées. Nous verrons que ceci est très pratique si l'on veut écrire les coordonnées des atomes d'une molécule au format PDB.

Pour les réels, il est possible de combiner le nombre de chiffres après la virgule.

    >>> print("{:7.3f}".format(propGC))
     47.804
    >>> print("{:10.3f}".format(propGC))
        47.804

L'instruction `7.3f` signifie que l'on souhaite écrire le réel avec 3 décimales et formaté sur 7 caractères (par défaut justifiés à droite). L'instruction `10.3f` fait la même chose sur 10 caractères. Remarquez que le séparateur décimal `.` compte pour un caractère.

Enfin, si on veut écrire des accolades litérales et utiliser la méthode `format()` en même temps, il faudra doubler les accolades pour échapper au formatage.

    >>> print("Accolades litérales {{}} et accolades pour le formatage {}".format(10))
    Accolades litérales {} et accolades pour le formatage 10

**À retenir** : Comme indiqué ci-dessus, la méthode `.format()` agit sur la chaîne de caractères à laquelle elle est *attachée* par un `.`, et n'a rien à voir avec la fonction `print()`. Si on donne une chaîne suivie d'un `.format()` à la fonction `print()`, Python évalue d'abord le formatage et c'est la chaîne qui en résulte qui est affichée à l'écran. Tout comme dans `print(5*5)`, c'est d'abord la multiplication qui est évaluée puis son résultat qui est affiché à l'écran. On peut s'en rendre compte de la manière suivante dans l'interpréteur :

    >>> "{:10.3f}".format(propGC)
    '    47.804'
    >>> type("{:10.3f}".format(propGC))
    <class 'str'>

Python affiche le résultat de l'instruction `"{:10.3f}".format(propGC)` comme une chaîne de caractères (*string*), et la fonction `type()` nous le confirme.


## Ancienne méthode de formatage des chaînes de caractères

*Conseil* : Pour les débutants, vous pouvez passer cette section.

Sur d'anciens programmes Python, il se peut que vous rencontriez l'écriture formatée dans le style suivant :

    >>> x = 32
    >>> nom = 'John'
    >>> print("%s a %d ans" % (nom,x))

    >>> nbG = 4500
    >>> nbC = 2575
    >>> propGC = (4500.0 + 2575)/14800
    >>> print("On a %d G et %d C -> prop GC = %.2f" % (nbG,nbC,propGC))
    On a 4500 G et 2575 C -> prop GC = 0.48

La syntaxe est légèrement différente. Le symbole `%` est appelé une première fois dans la chaîne de caractères (dans l'exemple ci-dessus `%d`, `%d` et `%.2f`) pour :

- Désigner l'endroit où sera placé la variable dans la chaîne de caractères.
- Préciser le type de variable à formater, `d` pour un entier (`i` fonctionne également) ou `f` (*float*) pour un réel.
- Eventuellement pour indiquer le format voulu. Ici `.2` signifie une précision de deux chiffres après la virgule.

Le signe `%` est rappelé une seconde fois (`% (nbG,nbC,propGC)`) pour indiquer les variables à formater.

Cette ancienne façon de formater vous est présentée à titre d'information. Ne l'utilisez pas dans vos programmes.


## Note sur le vocabulaire et la syntaxe

Revenons quelques instants sur la notion de **méthode** abordée dans ce chapitre avec `.format()`. En Python, on peut finalement considérer chaque variable comme un objet sur lequel on peut appliquer des méthodes. Une méthode est simplement une fonction qui utilise et/ou agit sur l'objet lui-même, les deux étant connectés par un point `.`. La syntaxe générale est du type `objet.méthode()`.

Dans l'exemple suivant :

    >>> "Joe a {} ans".format(20)
    'Joe a 20 ans'

la méthode `.format()` est liée à `"Joe a {} ans"` qui est un objet de type chaîne de caractères (*string*). La méthode renvoie une nouvelle chaîne de caractères avec le bon formatage.

Nous aurons de nombreuses occasions de revoir cette notation `objet.méthode()`.

## Exercices

Conseil : utilisez l'interpréteur Python pour les exercices 2 à 4.

### Affichage dans l'interpréteur et dans un programme

Ouvrez l'interpréteur Python et tapez `1+1`. Que se passe-t-il ? Ecrivez la même chose dans un script `test.py`. Exécutez ce script en tapant `python3 test.py` dans un *shell* Unix. Que se passe-t-il ? Pourquoi ? Faites en sorte d'afficher le résultat de l'addition `1+1` en exécutant le script dans un *shell* Unix.


### Poly-A

Générez une chaîne de caractères représentant un oligonucléotide polyA (AAAA...) de 20 bases de longueurs, sans taper littéralement toutes les bases.


### Poly-A et poly-GC

Suivant le modèle du dessus, générez en une ligne de code un polyA de 20 bases suivi d'un polyGC régulier (GCGCGC...) de 40 bases.


### Écriture formatée

En utilisant l'écriture formatée, affichez en une seule ligne les variables `a`, `b` et `c` dont les valeurs sont respectivement `"salut"`, `102` et `10.318`.


### Écriture formatée 2

Dans un script `propGC.py`, calculez un pourcentage de GC avec l'instruction suivante : `percGC = ((4500 + 2575)/14800)*100`. Ensuite, affichez le contenu de la variable `percGC` à l'écran avec 0, 1, 2, 3 puis 4 décimales sous forme arrondie en utilisant `.format()`. On souhaite que le programme affiche la sortie suivante :

    Le pourcentage de GC est 48      %
    Le pourcentage de GC est 47.8    %
    Le pourcentage de GC est 47.80   %
    Le pourcentage de GC est 47.804  %
    Le pourcentage de GC est 47.8041 %
