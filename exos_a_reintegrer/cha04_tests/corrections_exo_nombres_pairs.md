### Nombres pairs

On construit la liste des nombres pairs compris entre 2 et 10000 puis on calcule la taille de cette liste (donc le nombre d'éléments qu'elle contient) :

```python
>>> len(list(range(2, 10001, 2)))
5000
```

Dans la mesure où on ne manipule pas directement les éléments de la liste, on peut écrire directement :

```python
>>> len(range(2,10001,2))
5000
```
