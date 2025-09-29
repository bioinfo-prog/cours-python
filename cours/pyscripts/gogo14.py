class Fruit:
    def __init__(self, taille=None, poids=None, saveur=None, forme=None):
        # création des attributs d'instance de la classe Fruit
        self.taille = taille # str
        self.poids = poids # int en grammes
        self.saveur = saveur # str
        self.forme = forme #str

    def affiche_conseil(self, type_fruit, conseil):
        return ("Instance {}\ntaille: {}, poids: {}, saveur: {}, "
                "forme: {}\nconseil: {}\n"
                .format(type_fruit, self.taille, self.poids, self.saveur,
                        self.forme, conseil))

    def set_attribut(self, taille=None, poids=None, saveur=None, forme=None):
        if taille:
            self.taille = taille
        if poids:
            self.poids = poids
        if saveur:
            self.saveur = saveur
        if forme:
            self.forme = forme


class Citron(Fruit):
    def __init__(self, taille=None, poids=None, saveur=None, forme=None):
        Fruit.__init__(self, taille, poids, saveur, forme)
        #print(self.taille, self.poids, self.saveur, self.forme)
        
    def __repr__(self):
        return Fruit.affiche_conseil(self, "Citron", "Bon en tarte")


class Kaki(Fruit):
    def __init__(self, taille=None, poids=None, saveur=None, forme=None):
        Fruit.__init__(self, taille, poids, saveur, forme)

    def __repr__(self):
        return Fruit.affiche_conseil(self, "Kaki", "Bon à manger cru")


# on crée un citron
citron1 = Citron(taille="petite", saveur="acide", forme="ellipsoïde")
print(citron1)
# on crée un kaki
kaki1 = Kaki(forme="sphérique", saveur="très sucrée", taille="moyenne",
             poids=150)
print(kaki1)
# on met à jour le poids et la forme de kaki1 car on l'a mangé :-p
kaki1.set_attribut(forme="écrasée", poids=20)
print(kaki1)
