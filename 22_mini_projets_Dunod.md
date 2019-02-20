# Mini-projets

Dans ce chapitre, nous vous proposons quelques scénarios pour développer vos compétences en Python et mettre en oeuvre les concepts que vous avez rencontrés dans les chapitres précédents.

## Mots anglais dans le protéome humain

L'objectif de ce premier projet est de découvrir si des mots anglais peuvent se retrouver dans les séquences du protéome humain, c'est-à-dire dans les séquences de l'ensemble des protéines humaines.

Vous aurez à votre disposition :

- Le fichier [english-common-words.txt](https://python.sdv.univ-paris-diderot.fr/data-files/english-common-words.txt), qui contient les 3000 mots anglais les plus fréquents, à raison d'1 mot par ligne.
- Le fichier [human-proteome.fasta](https://python.sdv.univ-paris-diderot.fr/data-files/human-proteome.fasta) qui contient le protéome humain sous la forme de séquences au format fasta. Attention, ce fichier est assez gros. Ce fichier provient de la banque de données UniProt à partir de cette [page](https://www.uniprot.org/help/human_proteome).

Vous pouvez consulter les caractéristiques du format fasta dans l'annexe *Quelques formats de données rencontrés en biologie*.

Un guide pas à pas est disponible à cette adresse.

Un exemple de correction est téléchargeable ici.


## Genbank2fasta

Ce projet consiste à écrire un convertisseur de fichier, du format GenBank au format fasta.

Pour cela, nous allons utiliser le fichier GenBank du chromosome I de la levure du boulanger *Saccharomyces cerevisiae*. Vous pouvez télécharger ce fichier :

- soit via le lien sur le site du cours [NC_001133.gbk](https://python.sdv.univ-paris-diderot.fr/data-files/NC_001133.gbk);
- soit directement sur la page de [Saccharomyces cerevisiae S288c chromosome I, complete sequence](https://www.ncbi.nlm.nih.gov/nuccore/NC_001133) sur le site du NCBI, puis en cliquant sur *Send to*, puis *Complete Record*, puis *Choose Destination: File*, puis *Format: GenBank  (full)* et enfin sur le bouton *Create File*.

Vous pouvez consulter les caractéristiques des formats fasta et GenBank dans l'annexe *Quelques formats de données rencontrés en biologie*.

Dans la suite, nous vous proposons deux manières de procéder, avec et sans expression régulière selon si vous avez ou non lu et acquis les expressions régulières (Chapitre 15).

Vous pouvez réaliser ce projet sans ou avec des expressions régulières (abordées dans le chapitre 15).

Un guide pas à pas est disponible à cette adresse

Un exemple de correction est téléchargeable pour le projet :

- sans expression régulière
- avec expressions régulière 
