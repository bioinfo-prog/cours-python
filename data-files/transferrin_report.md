# Création du jeu de donnnées transferrin_report.csv

## Sélectoin des protéines

Sur le site de la PDB <https://www.rcsb.org/>

Cliquez sur "Advanced Search"

Entrez les paramètres de recherche :

- Structure Title Contains: transferrin
- Structure Title Does NOT Contain: transferring
- Chain Length Between 200 and 800
- Number of Chains (Asymetric Unit) Between 1 and 1
- Match All of the above conditions

Note : la transferrine humaine compte 698 residues (d'après Wikipédia https://fr.wikipedia.org/wiki/Transferrine). 

Au 24/10/2018, on obtient 45 structures

## Sélection du rapport 

Dans la rubrique "Reports:", sélectionnez "Customizable Table" puis :

- Dans "Structure Summary", "Deposit Date"
- Dans "Sequence", "Chain Length"
- Dans "Sequence", "Molecular Weight"
- Dans "Biological Details", "Source"

Puis cliquez sur "Create Report" en bas de la page.

On obtient 45 résultats.

Cliquez sur le lien CSV et ouvrez le fichier téléchargé avec Libreoffice Calc (le séparateur est ",")

Dans libreoffice :

- supprimez la colonne "Chain ID"
- supprimer les lignes dont la source est "Actinobacillus pleuropneumoniae"
- renommer la colonne "Dep. Date" en "Deposit Date"
- renommer la colonne "Chain Length" en "Length"
- renommer la colonne "Molecular Weight" en "MW"

Reste 41 lignes + 1 pour l'entête

Puis sauvegardez le fichier sous le nom "transferrin_report.csv"





