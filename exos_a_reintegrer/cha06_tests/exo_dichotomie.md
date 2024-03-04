### Recherche d'un nombre par dichotomie (exercice +++)

La recherche par [dichotomie](https://fr.wikipedia.org/wiki/Dichotomie) est une méthode qui consiste à diviser (en général en parties égales) un problème pour en trouver la solution. À titre d'exemple, voici une discussion entre Pierre et Patrick dans laquelle Pierre essaie de deviner le nombre (compris entre 1 et 100 inclus) auquel Patrick a pensé.

- [Patrick] « C'est bon, j'ai pensé à un nombre entre 1 et 100. »
- [Pierre]  « OK, je vais essayer de le deviner. Est-ce que ton nombre est plus petit ou plus grand que 50 ? »
- [Patrick] « Plus grand. »
- [Pierre]  « Est-ce que ton nombre est plus petit, plus grand ou égal à 75 ? »
- [Patrick] « Plus grand. »
- [Pierre]  « Est-ce que ton nombre est plus petit, plus grand ou égal à 87 ? »
- [Patrick] « Plus petit. »
- [Pierre]  « Est-ce que ton nombre est plus petit, plus grand ou égal à 81 ? »
- [Patrick] « Plus petit. »
- [Pierre]  « Est-ce que ton nombre est plus petit, plus grand ou égal à 78 ? »
- [Patrick] « Plus grand. »
- [Pierre]  « Est-ce que ton nombre est plus petit, plus grand ou égal à 79 ? »
- [Patrick] « Égal. C'est le nombre auquel j'avais pensé. Bravo ! »


Pour arriver rapidement à deviner le nombre, l'astuce consiste à prendre à chaque fois la moitié de l'intervalle dans lequel se trouve le nombre. Voici le détail des différentes étapes :


1. le nombre se trouve entre 1 et 100, on propose 50 (100 / 2).
2. le nombre se trouve entre 50 et 100, on propose 75 ( 50 + (100-50)/2 ).
3. le nombre se trouve entre 75 et 100, on propose 87 ( 75 + (100-75)/2 ).
4. le nombre se trouve entre 75 et 87, on propose 81 ( 75 + (87-75)/2 ).
5. le nombre se trouve entre 75 et 81, on propose 78 ( 75 + (81-75)/2 ).
6. le nombre se trouve entre 78 et 81, on propose 79 ( 78 + (81-78)/2 ).


Créez un script qui reproduit ce jeu de devinettes. Vous pensez à un nombre entre 1 et 100 et l'ordinateur essaie de le deviner par dichotomie en vous posant des questions.

Votre programme utilisera la fonction `input()` pour interagir avec l'utilisateur. Voici un exemple de son fonctionnement :

```python
>>> lettre = input("Entrez une lettre : ")
Entrez une lettre : P
>>> print(lettre)
P
```

Pour vous guider, voici ce que donnerait le programme avec la conversation précédente :

```text
Pensez à un nombre entre 1 et 100.
Est-ce votre nombre est plus grand, plus petit ou égal à 50 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 75 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 87 ? [+/-/=] -
Est-ce votre nombre est plus grand, plus petit ou égal à 81 ? [+/-/=] -
Est-ce votre nombre est plus grand, plus petit ou égal à 78 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 79 ? [+/-/=] =
J'ai trouvé en 6 questions !
```

Les caractères `[+/-/=]` indiquent à l'utilisateur comment il doit interagir avec l'ordinateur, c'est-à-dire entrer soit le caractère `+` si le nombre choisi est plus grand que le nombre proposé par l'ordinateur, soit le caractère `-` si le nombre choisi est plus petit que le nombre proposé par l'ordinateur, soit le caractère `=` si le nombre choisi est celui proposé par l'ordinateur (en appuyant ensuite sur la touche *Entrée*).
