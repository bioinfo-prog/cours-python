"""Ce script convertit un fichier genbank en plusieurs fichiers fasta.

Il prend en argument un fichier genbank, en extrait les gènes et
écrit leur séquence dans des fichier au format fasta.

Usage :
=======

    $ python genbank2fasta.py [file].gbk

Note de version:
================
    * Passage de python2 vers python3
    * Traduction en français
    * Mise à jours de la syntaxe PEP8
    * Version sans regex
"""

__auteurs__ = ("Benoist Laurent, Jonathan Barnoud, Patrick Fuchs"
               "Hubert Santuz, Pierre Poulain, Romain Retureau")
__version__ = "3.0.0"
__license__ = "BSD 3-Clause"
__date__ = "2018-09-01"


import re
import sys
import os

BASES_COMP = {"a":"t", "t":"a", "c":"g", "g":"c"}


def lit_fichier(nom_fichier):
    """Retourne une liste contenant les lignes du fichier *nom_fichier*."""
    with open(nom_fichier, "r") as fichier:
        return fichier.readlines()


def extrait_organisme(lignes_fichier):
    """Extrait le nom de l'organisme à partir des lignes d'un fichier genbank.

    Paramètres:
    ===========
    * lignes_fichier (*str list*): Liste contenant les lignes d'un fichier
                                   genbank.

    Retour:
    =======
    Retourne le nom de l'organisme (*str*). Si le nom n'est pas compris dans 
    les lignes du fichier genbank, retourne une chaine de caractère vide.  
    """
    organisme = ""
    for ligne in lignes_fichier:
        if ligne[:10] == "  ORGANISM":
            # on recupere l'organisme du caractère 12 jusqu'à l'avant dernier
            organisme = ligne[12:-1] 
    return organisme

def nettoyer_ligne_gene(ligne):
    ligne = ligne[21:].replace("complement","")
    ligne = ligne.replace(">","")
    ligne = ligne.replace("<","")
    ligne = ligne.replace("(","")
    ligne = ligne.replace(")","")
    return ligne
    
def recherche_genes(lignes_fichier):
    """Recherche des gènes à partir des lignes d'un fichier genbank.
    
    Paramètres:
    ===========
    * ligne_fichier (*str list*): Liste contenant les lignes d'un fichier
                                  genbank.

    Retour:
    =======
    Retourne une liste de gène. Chaque gène est un dictionnaire avec trois
    clés:
        * debut : la position de départ
        * fin : la position de fin 
        * orientation : le sens du gène.  
    """
    genes = []
    for ligne in lignes_fichier:
        # trouver les lignes qui contiennent les positions des gènes
        if ligne.startswith("     gene            "):
            # recherche des gènes antisens
            if "complement" in ligne:
                gene = {}
                # nettoyer la ligne (on recupère quelque chose comme: "debut..fin")
                ligne_propre = nettoyer_ligne_gene(ligne)
                # recupérer la position du gène (sous forme d'entier)
                gene["debut"] = int(ligne_propre.split(".")[0])
                gene["fin"] = int(ligne_propre.split(".")[-1])
                # ajouter le gène à la liste
                gene["orientation"] = "antisens"
                genes.append(gene)
            # recherche des gènes sens
            else:
                gene = {}
                # nettoyer la ligne
                ligne_propre = nettoyer_ligne_gene(ligne)
                # recupérer la position du gène (sous forme d'entier)
                gene["debut"] = int(ligne_propre.split(".")[0])
                gene["fin"] = int(ligne_propre.split(".")[-1])
                # ajouter le gène à la liste
                gene["orientation"] = "sens"
                genes.append(gene)
    return genes


def extrait_sequence(lignes_fichier):
    """Extraction de la séquence nucléotidique complète à partir des lignes
    d'un fichier genbank.

    Paramètres:
    ===========
    * lignes_fichier (*str list*): List contenant les lignes d'un fichier
                                   genbank.
    
    Retour:
    =======
    Retourne la séquence (*str*) nucléotidique complète. 
    """
    sequence = ""
    # définition d'un drapeau: si la ligne contient la séquence,
    # on le met à True
    is_sequence = False
    for ligne in lignes_fichier:
        # si la ligne contient //, la sequence est finie
        if ligne[0:2] == "//":
            is_sequence = False
        # récup sequence
        if is_sequence == True:
            sequence += ligne[10:-1].replace(" ","")
        # si la ligne contient ORIGIN, la prochaine ligne 
        # contient la sequence d'ADN!
        if ligne[0:6] == "ORIGIN":
            is_sequence = True
    return sequence

    
def construit_comp_inverse(seq):
    """Retourne la séquence complémentaire inverse."""
    seq = seq.lower()
    seq_comp = []
    for base in seq:
        seq_comp.append(BASES_COMP[base])
    seq_comp.reverse()
    return "".join(seq_comp)


def ecrit_fasta(nom_fichier, commentaire, sequence):
    """Ecrit un fichier au format fasta. 

    Paramètres:
    ===========
    * nom_fichier (*str*): Nom du fichier en sortie. 
    * commentaire (*str*): Commentaire de la première ligne du fasta.
    * sequence (*str*): Séquence à ecrire au format fasta.
    """
    largeur = 80
    with open(nom_fichier, "w") as fichier_fasta:
        fichier_fasta.write(">{}\n".format(commentaire))
        for pos in range(0, len(sequence), largeur):
            fichier_fasta.write("{}\n".format(sequence[pos:pos+largeur]))


def extrait_genes(genes, sequence, organisme):
    """Extrait et écrit une liste de gène au format fasta.

    Paramètres:
    ===========
    * genes (*dict list*): Liste de gènes contenant la position de départ,
                           de fin et le sens de chaque gène.
    * sequence (*str*): Séquence complète issue du fichier genbank. 
    * organisme (*str*): Nom de l'organisme issue du fichier genbank.
    """
    numero = 0
    for gene in genes:
        numero = numero + 1
        sequence_gene = sequence[gene["debut"]-1:gene["fin"]]
        if gene["orientation"] == "antisens":
            sequence_gene = construit_comp_inverse(sequence_gene)
        nom = "gene{}.fasta".format(numero)
        commentaire = "{}|{}|{}|{}|{}".format(organisme, numero, gene["debut"],
                                              gene["fin"], gene["orientation"])
        ecrit_fasta(nom, commentaire, sequence_gene)
        print("Gène {} écrit dans le fichier {}".format(numero, nom))


#===============================================================================
# début du programme
#===============================================================================

if __name__ == "__main__":
    #==== VÉRIFICATION DU FICHIER GENBANK ======================================
    # vérification du bon nombre d'arguments
    if len(sys.argv) == 1:
        exit("Le fichier GenBank en argument est manquant.")
    # récuperation du nom de fichier
    nom_fich = sys.argv[1]
    # vérification que le fichier existe bien
    if not os.path.exists(nom_fich):
        exit("Le fichier GenBank n'existe pas.")
    #==== LECTURE, EXTRACTION et ÉCRITURE DES GÈNES ============================
    # lecture du contenu du fichier
    cont_fichier = lit_fichier(nom_fich)
    print("Nombre de lignes lues {} : {}".format(nom_fich, len(cont_fichier)))
    # extraction du nom de l'organisme
    nom_organisme = extrait_organisme(cont_fichier)
    print("Organisme :", nom_organisme)
    # extraction de la séquence complète
    sequence_complete = extrait_sequence(cont_fichier)
    print("Séquence complète : {} bases".format(len(sequence_complete)))
    # recherche des gènes
    liste_genes = recherche_genes(cont_fichier)
    genes_sens = []
    genes_antisens = []
    for gene in liste_genes:
        if gene["orientation"] == "sens":
            genes_sens.append(gene)
        elif gene["orientation"] == "antisens":
            genes_antisens.append(gene)
        else:
            exit("Erreur dans l'orientation du gène:",gene)
    print("{} gènes trouvés :".format(len(liste_genes)), end=" ")
    print("{} sens / {} antisens".format(len(genes_sens), len(genes_antisens)))
    # extraction des gènes et enregistrement en fichiers fasta
    extrait_genes(liste_genes, sequence_complete, nom_organisme)


