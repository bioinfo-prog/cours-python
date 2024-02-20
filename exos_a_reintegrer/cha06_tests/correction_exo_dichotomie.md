### Recherche d'un nombre par dichotomie (exercice +++)

```python
print("Pensez à un nombre entre 1 et 100.")
trouve = False
mini = 1
maxi = 100
pas = 0
while not trouve:
    pas += 1
    val = int( mini + (maxi - mini)/2.0)
    aide = input(f"Est-ce votre nombre est plus grand, plus petit ou égal à {val} ? [+/-/=] ")
    if aide == "+":
        mini = val
    if aide == "-":
        maxi = val
    if aide == "=":
        print(f"J'ai trouvé en {pas} questions !")
        trouve = True
```

Premièrement, on retrouve ici le mécanisme du drapeau. On commence avec le drapeau `trouve` à `False`, puisque bien sûr on ne connait pas encore la solution avant de démarrer. Ensuite la boucle while est basée sur la proposition en français "tant qu'on n'a pas trouvé la solution on continue à poser des questions", ainsi le `while not trouve:` : `trouve` est à `False`, donc `not trouve` vaut `True` (i.e. "pas trouvé" est vrai) et on rentre ainsi dans la boucle. Lorsqu'on trouve la solution, il suffit de mettre le drapeau `trouve` à `True` et la boucle se termine. On voit ici l'utilisation d'un simple booléen avec une boucle while.

Une difficulté particulière dans cet exercice consiste à bien calculer la valeur proposée par l'ordinateur :

```python
val = int( mini + (maxi - mini)/2.0)
```

et à bien décider quand modifier les variables `mini` et `maxi` qui déterminent l'intervalle dans lequel se trouve le nombre à trouver par l'ordinateur.

Réponse attendue pour le nombre 39 trouvé par l'ordinateur :

```text
Est-ce votre nombre est plus grand, plus petit ou égal à 50 ? [+/-/=] -
Est-ce votre nombre est plus grand, plus petit ou égal à 25 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 37 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 43 ? [+/-/=] -
Est-ce votre nombre est plus grand, plus petit ou égal à 40 ? [+/-/=] -
Est-ce votre nombre est plus grand, plus petit ou égal à 38 ? [+/-/=] +
Est-ce votre nombre est plus grand, plus petit ou égal à 39 ? [+/-/=] =
J'ai trouvé en 7 questions !
```
