"""Ce script convertit un fichier genbank en plusieurs fichiers fasta.

Il prend en argument un fichier genbank, en extrait les gènes et
écrit leur séquence dans des fichier au format fasta.

Usage :
=======

    $ python genbank2fasta.py_avec_regex [file].gbk
"""

__auteurs__ = ("Benoist Laurent, Jonathan Barnoud, Patrick Fuchs"
               "Hubert Santuz, Pierre Poulain, Romain Retureau")
__date__ = "2021-07-07"
__license__ = "BSD 3-Clause"

import re
import sys
import os


def lit_fichier(nom_fichier):
    """Lit l'intégralité du contenu du fichier."""
    with open(nom_fichier, "r") as fichier:
        return fichier.readlines()


def extrait_organisme(lignes_fichier):
    """Extrait le nom de l'organisme."""
    organisme = ""
    regex = re.compile("ORGANISM +([A-Za-z0-9 -]+)")
    for ligne in lignes_fichier:
        recherche_organisme = regex.search(ligne)
        if recherche_organisme:
            organisme = recherche_organisme.group(1)
    return organisme


def recherche_genes(lignes_fichier):
    """Recherche des gènes."""
    genes = []
    regex_sens = re.compile("^ {5}gene {12}<?([0-9]+)\.\.>?([0-9]+)")
    regex_antisens = re.compile("^ {5}gene {12}complement\(<?([0-9]+)\.\.>?([0-9]+)\)")
    for ligne in lignes_fichier:
        # recherche des gènes sens
        recherche_sens = regex_sens.search(ligne)
        if recherche_sens:
            debut_gene = int(recherche_sens.group(1))
            fin_gene = int(recherche_sens.group(2))
            genes.append([debut_gene, fin_gene, "sens"])
        # recherche des gènes antisens
        recherche_antisens = regex_antisens.search(ligne)
        if recherche_antisens:
            debut_gene = int(recherche_antisens.group(1))
            fin_gene = int(recherche_antisens.group(2))
            genes.append([debut_gene, fin_gene, "antisens"])
    return genes


def extrait_sequence(lignes_fichier):
    """Extraction de la séquence nucléotidique complète."""
    sequence = ""
    regex_seq = re.compile("^ *[0-9]{1,8} +([atcg ]+)$")
    for ligne in lignes_fichier:
        recherche_seq = regex_seq.search(ligne)
        if recherche_seq:
            sequence = sequence + recherche_seq.group(1).replace(" ", "")
    return sequence


def construit_comp_inverse(seq):
    """Construction de la séquence complémentaire inverse."""
    seq = seq.lower()
    seq_comp = []
    for base in seq:
        if base == "a":
            seq_comp.append("t")
        elif base == "t":
            seq_comp.append("a")
        elif base == "g":
            seq_comp.append("c")
        elif base == "c":
            seq_comp.append("g")
    seq_comp.reverse()
    return "".join(seq_comp)


def ecrit_fasta(nom_fichier, commentaire, sequence):
    """Ecriture d'un fichier fasta."""
    largeur = 80
    with open(nom_fichier, "w") as fichier_fasta:
        fichier_fasta.write(f">{commentaire}\n")
        for pos in range(0, len(sequence), largeur):
            fichier_fasta.write(f"{sequence[pos:pos+largeur]}\n")


def extrait_genes(genes, sequence, organisme):
    """Extraction et sauvegarde des gènes."""
    numero = 0
    for gene in genes:
        debut = gene[0]
        fin = gene[1]
        sens = gene[2]
        numero = numero + 1
        sequence_gene = sequence[debut-1:fin]
        if sens == "antisens":
            sequence_gene = construit_comp_inverse(sequence_gene)
        nom = f"gene{numero}.fasta"
        commentaire = f"{organisme}|{numero}|{debut}|{fin}|{sens}"
        ecrit_fasta(nom, commentaire, sequence_gene)
        print(f"Gène {numero} écrit dans le fichier {nom}")


# ============================================================================
# début du programme
# ============================================================================

if __name__ == "__main__":
    # Vérification du bon nombre d'arguments?
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
    genes_sens = [gene for gene in liste_genes if gene[2] == "sens"]
    genes_antisens = [gene for gene in liste_genes if gene[2] == "antisens"]
    print(f"{len(liste_genes)} gènes trouvés : "
          f"{len(genes_sens)} sens / {len(genes_antisens)} antisens")

    # Extraction de la séquence complète.
    sequence_complete = extrait_sequence(contenu_fichier)
    print(f"Séquence complète : {len(sequence_complete)} bases")

    # Extraction des gènes et enregistrement en fichiers fasta.
    extrait_genes(liste_genes, sequence_complete, nom_organisme)
