"""Ce script convertit un fichier genbank en plusieurs fichiers fasta.

Il prend en argument un fichier genbank, en extrait les gènes et
écrit leur séquence dans des fichier au format fasta.

Usage :
=======

    $ python genbank2fasta.py [file].gbk
"""

__auteurs__ = ("Benoist Laurent, Jonathan Barnoud, Patrick Fuchs"
               "Hubert Santuz, Pierre Poulain, Romain Retureau")
__date__ = "2021-07-07"
__license__ = "BSD 3-Clause"


import sys
import os

BASES_COMP = {"a": "t", "t": "a", "c": "g", "g": "c"}


def lit_fichier(nom_fichier):
    """Lit l'intégralité du contenu du fichier."""
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
    """Supprime des caractères de la ligne."""
    ligne = ligne[21:].replace("complement", "")
    ligne = ligne.replace(">", "")
    ligne = ligne.replace("<", "")
    ligne = ligne.replace("(", "")
    ligne = ligne.replace(")", "")
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
                # nettoyer la ligne
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
    """Extraction de la séquence nucléotidique complète.

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
        if is_sequence:
            sequence += ligne[10:-1].replace(" ", "")
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
        fichier_fasta.write(f">{commentaire}\n")
        for pos in range(0, len(sequence), largeur):
            fichier_fasta.write(f"{sequence[pos:pos+largeur]}\n")


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
        nom = f"gene{numero}.fasta"
        commentaire = (f"{organisme}|{numero}|{gene['debut']}|{gene['fin']}|"
                       f"{gene['orientation']}")
        ecrit_fasta(nom, commentaire, sequence_gene)
        print(f"Gène {numero} écrit dans le fichier {nom}")


# ============================================================================
# Début du programme.
# ============================================================================

if __name__ == "__main__":
    # Vérification du bon nombre d'arguments.
    if len(sys.argv) == 1:
        sys.exit("Le fichier GenBank en argument est manquant.")

    # Récuperation du nom de fichier.
    nom_fichier_genbank = sys.argv[1]

    # Vérification que le fichier existe bien.
    if not os.path.exists(nom_fichier_genbank):
        sys.exit("Le fichier GenBank n'existe pas.")

    # Lecture du contenu du fichier.
    contenu_fichier = lit_fichier(nom_fichier_genbank)
    print(f"Nombre de lignes lues dans le fichier {nom_fichier_genbank} : "
          f"{len(contenu_fichier)}")

    # Extraction du nom de l'organisme.
    nom_organisme = extrait_organisme(contenu_fichier)
    print("Organisme :", nom_organisme)

    # Recherche des gènes.
    liste_genes = recherche_genes(contenu_fichier)
    genes_sens = []
    genes_antisens = []
    for gene in liste_genes:
        if gene["orientation"] == "sens":
            genes_sens.append(gene)
        elif gene["orientation"] == "antisens":
            genes_antisens.append(gene)
        else:
            sys.exit("Erreur dans l'orientation du gène:", gene)
    print(f"{len(liste_genes)} gènes trouvés : "
          f"{len(genes_sens)} sens / {len(genes_antisens)} antisens")

    # Extraction de la séquence complète.
    sequence_complete = extrait_sequence(contenu_fichier)
    print(f"Séquence complète : {len(sequence_complete)} bases")

    # Extraction des gènes et enregistrement en fichiers fasta.
    extrait_genes(liste_genes, sequence_complete, nom_organisme)
