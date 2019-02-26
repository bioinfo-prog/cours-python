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