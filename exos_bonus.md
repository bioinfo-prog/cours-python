## Fonction


### Aire sous la courbe (exercice +++)

La [méthode des trapèzes](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_trap%C3%A8zes) permet de calculer numériquement l'intégrale d'une fonction. Elle consiste à évaluer l'aire sous une fonction en évaluant l'aire de trapèzes successifs. On souhaite créer une fonction `calc_aire()` qui prend en argument deux listes de *floats* `list_x` et `list_y` représentant les coordonnées d'une fonction (par exemple $x$ et $sin(x)$) et qui renvoie l'aire sous la courbe. On calculera les intégrales suivantes :

- $\int_{0}^{1} x \, dx$

- $\int_{0}^1 \sqrt{x} \, dx$

- $\int_{-\pi}^{+\pi} sin(x) \,dx$

- $\int_{-\pi}^{+\pi} cos(x) \,dx$



## Regex


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
