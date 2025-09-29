class Citron:
    def __init__(self, couleur="jaune"):
        self.couleur = couleur
        var = 2

    def affiche_attributs(self):
        print(self)
        print(self.couleur)
        print(var)


if __name__ == '__main__':
    citron1 = Citron()
    citron1.affiche_attributs()
