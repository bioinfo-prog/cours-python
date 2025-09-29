class Citron:
    def __init__(self):
        self.couleur = "jaune"
        var = 2

    def affiche_attributs(self):
        print(self)
        print(self.couleur)
        print(var)

citron1 = Citron()
citron1.affiche_attributs()
