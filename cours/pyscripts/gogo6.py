class Citron:
    def __init__(self, saveur="acide", couleur="jaune"):
        self.saveur = saveur
        self.couleur = couleur
        print("Dans __init__(), vous venez de créer un citron:",
              self.affiche_attributs())

    def affiche_attributs(self):
        return "{}, {}".format(self.couleur, self.saveur)

if __name__ == '__main__':
    saveur = "sucrée"
    couleur = "orange"
    print("Dans prog principal: {}, {}".format(saveur, couleur))
    citron1 = Citron("très acide", "jaune foncé")
    print("Dans citron1.affiche_attributs():", citron1.affiche_attributs())
    print("Dans prog principal: {}, {}".format(saveur, couleur))
