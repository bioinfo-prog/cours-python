class Fruit:
    def __init__(self, taille=None, masse=None, saveur=None, forme=None):
        print("(2) Je suis dans le constructeur de la classe Fruit")
        self.taille = taille
        self.masse = masse # en gramme
        self.saveur = saveur
        self.forme = forme
        print("Je viens de créer self.taille, self.masse, self.saveur et "
              "self.forme")

    def affiche_conseil(self, type_fruit, conseil):
        print("(2) Je suis dans la méthode .affiche_conseil() de la classe "
              "Fruit\n")
        return ("Instance {}\ntaille: {}, masse: {},\n"
                "saveur: {}, forme: {}\nconseil: {}\n"
                .format(type_fruit, self.taille, self.masse, self.saveur,
                        self.forme, conseil))


class Citron(Fruit):
    def __init__(self, taille=None, masse=None, saveur=None, forme=None):
        print("(1) Je rentre dans le constructeur de Citron, et je vais appeler\n"
              "le constructeur de la classe mère Fruit !")
        Fruit.__init__(self, taille, masse, saveur, forme)
        print("(3) J'ai fini dans le constructeur de Citron, "
              "les attributs sont: \nself.taille: {}, self.masse: {},\n"
              "self.saveur: {}, self.forme: {}\n"
              .format(self.taille, self.masse, self.saveur, self.forme))

    def __repr__(self):
        print("(1) Je rentre dans la méthode .__repr__() de la classe Citron")
        print("Je vais lancer la méthode .affiche_conseil() héritée "
              "de la classe Fruit")
        return self.affiche_conseil("Citron", "Bon en tarte :-p !")


if __name__ == '__main__':
    # on crée un citron
    citron1 = Citron(taille="petite", saveur="acide", forme="ellipsoïde", masse=50)
    print(citron1)
