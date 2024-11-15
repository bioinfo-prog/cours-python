# Avoir la classe avec les objets

\index{programmation orientee objet@programmation orientée objet}
\index{objet}
\index{classe}
\index{instance}
\index{methode@méthode}

La programmation orientée objet (POO) est un concept de programmation très puissant qui permet de structurer ses programmes d'une manière nouvelle. En POO, on définit un « objet » qui peut contenir des « attributs » ainsi que des « méthodes » qui agissent sur lui-même. Par exemple, on définit un objet « citron » qui contient les attributs « saveur » et « couleur », ainsi qu'une méthode « presser » permettant d'en extraire le jus. En Python, on utilise une « classe » pour construire un objet. Dans notre exemple, la classe correspondrait au « moule » utilisé pour construire autant d'objets citrons que nécessaire.

open-box-def

Une **classe** définit des **objets**, qui sont des **instances** (des représentants) de cette classe. Dans ce chapitre, on utilisera les mots *objet* ou *instance* pour désigner la même chose. Les objets peuvent posséder des **attributs** (variables associées aux objets) et des **méthodes** (qui sont des fonctions associées aux objets et qui peuvent agir sur ces derniers, ou encore les utiliser).

close-box-def

Dans les chapitres précédents, nous avons déjà mentionné qu'en Python tout est objet. Une variable de type *int* est en fait un objet de type *int*, donc construit à partir de la classe *int*. Même chose pour les *float* et *string*, mais aussi pour les *list*, *tuple*, *dict*, etc. Voilà pourquoi nous avons rencontré de nombreuses notations et mots de vocabulaire associés à la POO depuis le début de ce cours.

\index{espace de noms}

La POO permet de produire du code plus compact et plus facilement réutilisable. L'utilisation de classes évite l'utilisation de variables globales en créant ce qu'on appelle un *espace de noms*, propre à chaque objet et permettant d'y *encapsuler* des attributs et des méthodes. De plus, la POO amène de nouveaux concepts tels que le *polymorphisme* (capacité à redéfinir le comportement des opérateurs), ou bien encore l'*héritage* (capacité à définir une classe à partir d'une classe pré-existante et d'y ajouter de nouvelles fonctionnalités). Tous ces concepts seront définis dans ce chapitre.

Malgré tous ces avantages, la POO peut paraître difficile à aborder pour le débutant, spécialement dans la conception des programmes. Elle nécessite donc la lecture de nombreux exemples, mais surtout beaucoup de pratique. Bien structurer ses programmes en POO est un véritable art. Il existe même des langages qui formalisent la construction de programmes orientés objets, par exemple le langage [UML](https://fr.wikipedia.org/wiki/UML_(informatique)).

Dans ce chapitre, nous vous donnerons tous les éléments pour démarrer la construction de vos premières classes. Le chapitre 24 *Avoir plus la classe avec les objets* (en ligne) abordera des aspects plus poussés de la POO, comme le polymorphisme, la composition, l'héritage, certains pièges à éviter, ainsi que des bonnes pratiques.

Après la lecture de ces deux chapitres sur la POO avec Python, vous verrez d'un autre œil de nombreux exemples évoqués dans les chapitres précédents, et vous comprendrez sans doute de nombreuses subtilités qui avaient pu vous paraître absconses.

Enfin, il est vivement recommandé de lire ces deux chapitres sur la POO avant d'aborder le chapitre 25 *Fenêtres graphiques et Tkinter* (en ligne).


## Construction d'une classe

Nous allons voir dans cette rubrique comment définir une classe en reprenant notre exemple sur le citron, que nous allons faire évoluer et complexifier. Attention, certains exemples sont destinés à vous montrer comment les classes fonctionnent, mais leur utilisation n'aurait pas de sens dans un vrai programme. Ainsi, nous vous donnerons plus loin dans ce chapitre les pratiques recommandées.

### La classe minimale

\index{class@class (instruction)}

En Python, le mot-clé `class` permet de créer sa propre classe, suivi du nom de cette classe. On se souvient, un nom de classe commence toujours par une majuscule (voir le chapitre 16 *Bonnes pratiques en programmation Python*). Comme d'habitude, cette ligne attend un bloc d'instructions indenté définissant le corps de la classe. Voyons un exemple simple dans l'interpréteur :

\index{pass@pass (instruction)}

```python
>>> class Citron:
...     pass
...
>>> Citron
<class '__main__.Citron'>
>>> type(Citron)
<class 'type'>
>>> citron1 = Citron()
>>> citron1
<__main__.Citron object at 0x7ff2193a20f0>
>>>
```

**Ligne 1.** La classe `Citron` est définie. Pas besoin de parenthèses comme avec les fonctions dans un cas simple comme celui-là (nous verrons d'autres exemples plus loin où elles seront nécessaires).

**Ligne 2.** La classe ne contient rien, mais il faut mettre au moins une ligne, on met donc ici le mot-clé Python `pass` qui ne fait rien (comme dans une fonction qui ne fait rien).

**Lignes 4 et 5.** Quand on tape le nom de notre classe `Citron`, Python nous indique que cette classe est connue.

**Lignes 6 et 7.** Lorsqu'on regarde le type de notre classe `Citron`, Python nous indique qu'il s'agit d'un type au même titre que `type(int)`. Nous avons donc créé un nouveau type !

**Ligne 8.** On crée une instance de la classe `Citron`, c'est-à-dire qu'on fabrique un représentant ou objet de la classe `Citron`, que nous nommons `citron1`.

**Lignes 9 et 10.** Lorsqu'on tape le nom de l'instance `citron1`, l'interpréteur nous rappelle qu'il s'agit d'un objet de type `Citron`, ainsi que son adresse en mémoire.

Il est également possible de vérifier qu'une instance est bien issue d'une classe donnée avec la fonction `isinstance()` :

```python
>>> isinstance(citron1, Citron)
True
```

### Ajout d'un attribut d'instance

\index{attribut instance@attribut d'instance}

Reprenons notre classe `Citron` et l'instance `citron1` créée précédemment. Regardons les attributs et méthodes que cet objet possède, puis tentons de lui ajouter un attribut  :

```python
>>> dir(citron1)
['__class__', '__delattr__', '__dict__', [...], '__weakref__']
>>> citron1.couleur = "jaune"
>>> dir(citron1)
['__class__', '__delattr__', '__dict__', [...], '__weakref__', 'couleur']
>>> citron1.couleur
'jaune'
```

**Lignes 1 et 2.** L'objet possède de nombreuses méthodes ou attributs, qui commencent et qui se terminent par deux caractères *underscores*. On se souvient que les *underscores* indiquent qu'il s'agit de méthodes ou attributs destinés au fonctionnement interne de l'objet. Nous reviendrons sur certains d'entre-eux dans la suite.

**Ligne 3.** Ici on ajoute un attribut `.couleur` à l'instance `citron1`. Notez bien la syntaxe `instance.attribut` et le point qui lie les deux.

**Lignes 4 à 5.** La fonction `dir()` nous montre que l'attribut `.couleur` a bien été ajouté à l'objet.

**Lignes 6.** La notation `instance.attribut` donne accès à l'attribut de l'objet.

\index{dict@.\_\_dict\_\_}

L'attribut nommé `.__dict__` est particulièrement intéressant. Il s'agit d'un dictionnaire qui listera les attributs créés dynamiquement dans l'instance en cours :

```python
>>> citron1 = Citron()
>>> citron1.__dict__
{}
>>> citron1.couleur = "jaune"
>>> citron1.__dict__
{'couleur': 'jaune'}
```

L'ajout d'un attribut depuis l'extérieur de la classe (on parle aussi du côté « client ») avec une syntaxe `instance.nouvel_attribut = valeur`, créera ce nouvel attribut uniquement pour cette instance :

```python
citron1 = Citron()
citron1.couleur = "jaune"
>>> citron1.__dict__
{'couleur': 'jaune'}
>>> citron2 = Citron()
>>> citron2.__dict__
{}
```

Si on crée une nouvelle instance de `Citron`, ici `citron2`, elle n'aura pas l'attribut  
`couleur` à sa création.

open-box-def

Une **variable** ou **attribut d'instance** est une variable accrochée à une instance et qui lui est spécifique. Cet attribut n'existe donc pas forcément pour toutes les instances d'une classe donnée et, d'une instance à l'autre, il ne prendra pas forcément la même valeur. On peut retrouver tous les attributs d'instance d'une instance donnée avec une syntaxe `instance.__dict__`.

close-box-def

\index{del@del (instruction)}

L'instruction `del` fonctionne bien sûr pour détruire un objet (par exemple : 
`del citron1`), mais permet également de détruire un attribut d'instance. Si on reprend notre exemple `citron1` ci-dessus :

```python
>>> citron1.__dict__
{'couleur': 'jaune'}
>>> del citron1.couleur
>>> citron1.__dict__
{}
```

Dans la suite, on montrera du code à tester dans un script : n'hésitez pas, comme d'habitude, à le tester par vous-même.


### Les attributs de classe

\index{attribut de classe}

Si on ajoute une variable dans une classe comme on créait une variable locale dans une fonction, on crée ce qu'on appelle un attribut de classe :

```python
class Citron:
    couleur = "jaune"
```

open-box-def

Une **variable de classe** ou **attribut de classe** est un attribut qui sera identique pour chaque instance. On verra plus bas que de tels attributs suivent des règles différentes par rapport aux attributs d'instance.

close-box-def

À l'extérieur ou à l’intérieur d'une classe, un attribut de classe peut se retrouver avec une syntaxe `NomClasse.attribut` :

```python
print(Citron.couleur)
```

Ce code affiche `jaune`. L'attribut de classe est aussi visible depuis n'importe quelle instance :

```python
class Citron:
    couleur = "jaune"


if __name__ == "__main__":
    citron1 = Citron()
    print(citron1.couleur)
    citron2 = Citron()
    print(citron2.couleur)
```

L'exécution de ce code affichera :

```text
jaune
jaune
```

open-box-warn

Même si on peut retrouver un attribut de classe avec la syntaxe `instance.attribut`, un tel attribut ne peut pas être modifié avec une instruction de cette forme :

```python
instance.attribut = nouvelle_valeur
```
(voir la rubrique *Différence entre les attributs de classe et d'instance*).

close-box-warn


### Les méthodes

\index{methode@méthode}

Dans notre classe, on pourra aussi ajouter des fonctions.

open-box-def

Une fonction définie au sein d'une classe est appelée **méthode**. Pour exécuter une méthode à l'extérieur de la classe, la syntaxe générale est `instance.méthode()`. En général, on distingue attributs et méthodes (comme nous le ferons systématiquement dans ce chapitre). Toutefois, il faut garder à l'esprit qu'une méthode est finalement un objet de type fonction. Ainsi, elle peut être vue comme un attribut également, concept que vous croiserez peut-être en consultant de la documentation externe.

close-box-def

Voici un exemple d'ajout d'une fonction, ou plus exactement d'une méthode, au sein d'une classe (attention à l'indentation !) :

```python
class Citron:
    def coucou(self):
	    print("Coucou, je suis la mth .coucou() dans la classe Citron !")


if __name__ == "__main__":
    citron1 = Citron()
    citron1.coucou()
```

**Lignes 2 et 3.** On définit une méthode nommée `.coucou()`, qui va afficher un petit message. Attention, cette méthode prend obligatoirement un argument que nous avons nommé ici `self`. Nous verrons dans les deux prochaines rubriques la signification de ce `self`. Si on a plusieurs méthodes dans une classe, on saute toujours une ligne entre elles afin de faciliter la lecture (comme pour les fonctions).

**Ligne 7 et 8.** On crée l'instance `citron1` de la classe `Citron`, puis on exécute la méthode `.coucou()` avec une syntaxe `instance.méthode()`.

Une méthode étant une fonction, elle peut bien sûr retourner une valeur :

```python
class Citron:
    def recup_saveur(self):
	    return "acide"


if __name__ == "__main__":
    citron1 = Citron()
    saveur_citron1 = citron1.recup_saveur()
    print(saveur_citron1)
```

Vous l'aurez deviné, ce code affichera `acide` à l'écran. Comme pour les fonctions, une valeur retournée par une méthode est récupérable dans une variable, ici `saveur_citron1`.


### Le constructeur

\index{constructeur@constructeur (d'une classe)}

Lors de l'instanciation d'un objet à partir d'une classe, il peut être intéressant de lancer des instructions, comme, d'initialiser certaines variables. Pour cela, on ajoute une méthode spéciale nommée `.__init__()` : cette méthode s'appelle le « constructeur » de la classe. Il s'agit d'une méthode spéciale dont le nom est entouré de doubles *underscores* : en effet, elle sert au fonctionnement interne de notre classe et, sauf cas extrêmement rare, elle n'est pas supposée être lancée comme une fonction classique par l'utilisateur de la classe. Ce constructeur est exécuté à chaque instanciation de notre classe, et ne renvoie pas de valeur, il ne possède donc pas de `return`.

open-box-rem

Pour les débutants, vous pouvez sauter cette remarque. Certains auteurs préfèrent nommer `.__init__()` « instantiateur » ou « initialisateur », pour signifier qu'il existe une autre méthode appelée `.__new__()`, qui participe à la création d'une instance. Vous n'avez bien sûr pas à retenir ces détails pour continuer la lecture de ce chapitre, retenez simplement que nous avons décidé de nommer la méthode `.__init__()` « constructeur » dans cet ouvrage.

close-box-rem

Pour bien comprendre comment cela fonctionne, nous allons suivre un exemple simple avec le site [*Python Tutor*](http://www.pythontutor.com) (déjà utilisé dans les chapitres 10 et 13 sur les fonctions). N'hésitez pas à copier/coller ce code dans *Python Tutor* pour le tester vous-même :

```python
class Citron:
    def __init__(self):
	    self.couleur = "jaune"


if __name__ == "__main__":
    citron1 = Citron()
    print(citron1.couleur)
```

#### Étape 1 {.unnumbered}

Figure @fig:classe_constructeur1. Au départ, *Python Tutor* nous montre que la classe `Citron` a été mise en mémoire, elle contient pour l'instant la méthode `.__init__()`.

![Fonctionnement d'un constructeur (étape 1).](img/classe_constructeur1.png){ #fig:classe_constructeur1 width=90% }

#### Étape 2 {.unnumbered}

Figure @fig:classe_constructeur2. Nous créons ensuite l'instance `citron1` à partir de la classe `Citron`. Notre classe `Citron` contenant une méthode `.__init__()` (le constructeur), celle-ci est immédiatement exécutée au moment de l'instanciation. Cette méthode prend un argument nommé `self` : cet argument est **obligatoire**. Il s'agit en fait d'une référence vers l'instance en cours (instance que nous appellerons `citron1` dans le programme principal, mais cela serait vrai pour n'importe quel autre nom d'instance). *Python Tutor* nous indique cela par une flèche pointant vers un espace nommé `Citron instance`. La signification du `self` est expliquée en détail dans la rubrique suivante.

![Fonctionnement d'un constructeur (étape 2).](img/classe_constructeur2.png){ #fig:classe_constructeur2 width=90% }

#### Étape 3 {.unnumbered}

Figure @fig:classe_constructeur3. Un nouvel attribut est créé s’appelant `self.couleur`. La chaîne de caractères `couleur` est ainsi « accrochée » (grâce au caractère point) à l'instance en cours référencée par le `self`. *Python Tutor* nous montre cela par une flèche qui pointe depuis le `self` vers la variable `couleur` (qui se trouve elle-même dans l'espace nommé `Citron instance`). Si d'autres attributs étaient créés, ils seraient tous répertoriés dans cet espace `Citron instance`. Vous l'aurez compris, l'attribut `couleur` est donc une variable d'instance (voir rubrique *Ajout d'un attribut d'instance* ci-dessus). La méthode `.__init__()` étant intrinsèquement une fonction, *Python Tutor* nous rappelle qu'elle ne renvoie rien (d'où le `None` dans la case *Return value*), une fois son exécution terminée. Et comme avec les fonctions classiques, l'espace mémoire contenant les variables locales à cette méthode va être détruit une fois son exécution terminée.

![Fonctionnement d'un constructeur (étape 3).](img/classe_constructeur3.png){ #fig:classe_constructeur3 width=90% }

#### Étape 4 {.unnumbered}

Figure @fig:classe_constructeur4. De retour dans le programme principal, *Python Tutor* nous indique que `citron1` est une instance de la classe `Citron` par une flèche pointant vers l'espace `Citron instance`. Cette instance contient un attribut nommé `couleur` auquel on accéde avec la syntaxe `citron1.couleur` dans le `print()`. Notez que si l'instance s'était appelée `enorme_citron`, on aurait utilisé `enorme_citron.couleur` pour accéder à l'attribut `couleur`.

![Fonctionnement d'un constructeur (étape 4).](img/classe_constructeur4.png){ #fig:classe_constructeur4 width=90% }

open-box-adv

Dans la mesure du possible, nous vous conseillons de créer tous les attributs d'instance dont vous aurez besoin dans le constructeur `.__init__()` plutôt que dans toute autre méthode. Ainsi, ils seront visibles dans toute la classe dès l'instanciation.

close-box-adv


### Passage d'argument(s) à l'instanciation

Lors de l'instanciation, il est possible de passer des arguments au constructeur. Comme pour les fonctions, on peut passer des arguments positionnels ou par mot-clé, et en créer autant que l'on veut (voir chapitre 10 *Fonctions*). Voici un exemple :

```python
class Citron:
    def __init__(self, masse, couleur="jaune"):
        self.masse = masse
        self.couleur = couleur


if __name__ == "__main__":
    citron1 = Citron(100)
	print("citron1:", citron1.__dict__)
	citron2 = Citron(150, couleur="blanc")
	print("citron2:", citron2.__dict__)
```

On a ici un argument positionnel (`masse`) et un autre par mot-clé (`couleur`). Le code donnera la sortie suivante :

```python
citron1: {'masse': 100, 'couleur': 'jaune'}
citron2: {'masse': 150, 'couleur': 'blanc'}
```


### Mieux comprendre le rôle du `self`

\index{self}

Cette rubrique va nous aider à mieux comprendre le rôle du `self` à travers quelques exemples simples. Regardons le code suivant dans lequel nous créons une nouvelle méthode `.affiche_attributs()`:

```python
class Citron:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        var = 2

    def affiche_attributs(self):
        print(self)
        print(self.couleur)
        print(var)


if __name__ == "__main__":
    citron1 = Citron()
    citron1.affiche_attributs()
```

**Ligne 3.** On crée l'attribut `couleur` que l'on accroche à l'instance avec `self`.

**Ligne 4.** Nous créons cette fois-ci une variable `var` sans l'accrocher à `self`.

**Ligne 6.** Nous créons une nouvelle méthode dans la classe `Citron` qui se nomme  
`.affiche_attributs()`. Comme pour le constructeur, cette méthode prend comme premier argument une variable obligatoire, que nous avons à nouveau nommée `self`. Il s'agit encore une fois d'une référence vers l'objet ou instance créé(e).

open-box-warn

On peut appeler cette référence comme on veut, toutefois nous vous conseillons vivement de l'appeler `self`, car c'est une convention en Python. Ainsi, quelqu'un qui lira votre code comprendra immédiatement de quoi il s'agit.

close-box-warn

**Ligne 7.** Cette ligne va afficher le contenu de la variable `self`.

**Lignes 8 et 9.** On souhaite que notre méthode `.affiche_attributs()` affiche ensuite l'attribut de classe `.couleur` ainsi que la variable `var` créée dans le constructeur `.__init__()`.

L'exécution de ce code donnera :

```text
$ python classe_exemple1.py
<__main__.Citron object at 0x7f4e5fb71438>
jaune
Traceback (most recent call last):
  File "classe_exemple1.py", line 14, in <module>
    citron1.affiche_attributs()
  File "classe_exemple1.py", line 9, in affiche_attributs
    print(var)
          ^^^
NameError: name 'var' is not defined. Did you mean: 'vars'?
```

**Ligne 2.** La méthode `.affiche_attributs()` montre que le `self` est bien une référence vers l'instance (ou objet) `citron1` (ou vers n'importe quelle autre instance : par exemple, si on crée `citron2 = Citron()`, le `self` sera une référence vers `citron2`).

**Ligne 3.** La méthode `.affiche_attributs()` affiche l'attribut `.couleur`, qui avait été créé précédemment dans le constructeur. Vous voyez ici l'intérêt principal de l'argument `self` passé en premier à chaque méthode d'une classe : il « accroche » n'importe quel attribut qui sera visible partout dans la classe, y compris dans une méthode où il n'a pas été défini.

**Lignes 4 à 9.** La création de la variable `var` dans la méthode `.__init__()` sans l'accrocher à l'objet `self` fait qu'elle n'est plus accessible en dehors de `.__init__()`. C'est exactement comme pour les fonctions classiques, `var` est finalement une variable locale au sein de la méthode `.__init__()` et n'est plus visible lorsque l'exécution de cette dernière est terminée (voir les chapitres 10 et 13 sur les fonctions). Ainsi, Python renvoie une erreur, car `var` n'existe pas lorsque `.affiche_attributs()` est en exécution.

En résumé, le `self` est nécessaire lorsqu'on a besoin d'accéder à différents attributs dans les différentes méthodes d'une classe. Le `self` est également nécessaire pour appeler une méthode de la classe depuis une autre méthode :

```python
class Citron:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        self.affiche_message()

    def affiche_message(self):
        print("Le citron c'est trop bon !")


if __name__ == "__main__":
    citron1 = Citron("jaune pâle")
```

**Ligne 4.** Nous appelons ici la méthode `.affiche_message()` depuis le constructeur. Pour appeler cette méthode interne à la classe `Citron`, on doit utiliser une syntaxe `self.méthode()`. Le `self` sert donc pour accéder aux attributs, mais aussi aux méthodes, ou plus généralement à tout ce qui est accroché à la classe.

**Lignes 6 et 7.** La méthode `.affiche_message()` est exécutée. On peut se poser la question « Pourquoi passer l'argument self à cette méthode alors qu'on ne s'en sert pas dans celle-ci ? »

open-box-warn

Même si on ne se sert d'aucun attribut dans une méthode, l'argument `self` (ou quel que soit son nom) est **strictement obligatoire**. En fait, la notation `citron1.affiche_message()` est équivalente à `Citron.affiche_message(citron1)`.
Testez les deux pour voir ! Dans cette dernière instruction, on appelle la méthode accrochée à la classe `Citron` et on lui passe explicitement l'instance `citron1` en tant qu'argument. La notation `citron1.affiche_message()` contient donc en filigrane un argument, à savoir la référence vers l'instance `citron1` que l'on appelle `self` au sein de la méthode.

close-box-warn

open-box-adv

C'est la première notation `citron1.affiche_attributs()` (ou plus généralement `instance.méthode()`), plus compacte, qui sera toujours utilisée.

close-box-adv

**Ligne 11.** On crée l'instance `citron1` en lui passant l'argument `"jaune pâle"`. La variable d'instance `couleur` prendra ainsi cette valeur au lieu de celle par défaut (`"jaune"`). À noter, l'instanciation affichera le message `Le citron c'est trop bon !` puisque la méthode `.affiche_attributs()` est appelée dans le constructeur `.__init__()`.

Afin de bien comprendre les différentes étapes des codes de cette rubrique, nous vous conseillons de les retester de votre côté dans *Python Tutor*.

### Remarque finale

Dans ce chapitre, nous avons vu les bases pour construire une classe. Toutefois, nous avons encore de nombreuses notions à vous montrer afin de pouvoir utiliser la POO à plein régime. Dans le chapitre 24 *Avoir plus la classe avec les objets* (en ligne), nous verrons les concepts de polymorphisme, composition et héritage qui donnent toute la puissance à la POO. D'autres notions comme les décorateurs `property` seront abordées permettant le contrôle des attributs par un utilisateur de la classe. Nous donnerons également des conseils généraux quand vous utilisez la POO. Le chapitre 25 *Fenêtres graphiques et Tkinter*  (en ligne) illustrera l'utilisation de la POO pour concevoir des fenêtres graphiques avec le module *Tkinter*.

## Exercices

open-box-adv

Pour ces exercices, créez des scripts puis exécutez-les dans un *shell*.

close-box-adv


### Classe `Rectangle`

Téléchargez le script [`rectangle.py`](https://python.sdv.u-paris.fr/data-files/rectangle.py) qui implémente la classe `Rectangle`.

Complétez le programme principal pour que le script :

- crée une instance `rectangle` de la classe `Rectangle` ;
- affiche les attributs d'instance `largeur`, `longueur` et `couleur` ;
- calcule et affiche la surface de `rectangle` ;
- affiche une ligne vide ;
- change le rectangle en carré de 30 m de côté ;
- calcule et affiche la surface de ce carré ;
- crée une autre instance `rectangle2`, aux dimensions et à la couleur que vous souhaitez (soyez créatif !) et qui affiche les attributs et la surface de ce nouveau rectangle.


### Classe `Rectangle` améliorée

Entraînez-vous avec la classe `Rectangle`. Créez la méthode `calcule_perimetre()` qui calcule le périmètre d'un objet rectangle. Testez sur un exemple simple (largeur = 10 m, longueur = 20 m).


### Classe `Atome`

Créez une nouvelle classe `Atome` avec les attributs `x`, `y`, `z`, qui contiennent les coordonnées atomiques, et la méthode `calcul_distance()`, qui calcule la distance entre deux atomes. Testez cette classe sur plusieurs exemples.

### Classe `Atome` améliorée

Améliorez la classe `Atome` en lui ajoutant un nouvel attribut `masse`, qui correspond à la masse atomique, ainsi qu'une nouvelle méthode `.calcule_centre_masse()`. Que se passe-t-il quand vous utilisez l'instruction `print()` avec une instance d'un objet `Atome` ? Dans votre classe, ajoutez la méthode suivante :

```python
def __str__(self):
	"""Redéfinition du comportement avec print()."""
	return f"coords({self.x}, {self.y}, {self.z}) ; mass = {self.masse}"
```

Utilisez à nouveau l'instruction `print()` avec un objet de la classe `Atome`. Que constatez-vous par rapport au précédent `print()` ?
