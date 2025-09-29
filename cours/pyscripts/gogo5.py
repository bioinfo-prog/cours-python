class Citron:
    def __init__(self):
        self.couleur = "jaune"
        self.affiche_coucou()
        affiche_coucou()

    def affiche_coucou(self):
        print("Coucou interne !")


def affiche_coucou():
    print("Coucou externe")

citron1 = Citron()
citron1.affiche_coucou()
affiche_coucou()
