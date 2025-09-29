class CitronBasique:
    def __init__(self):
        self.couleur = "jaune"
        self.taille = "standard"


class Citron:
    def __init__(self, couleur="jaune", taille="standard"):
        self.couleur = couleur
        self.taille = taille

    def __repr__(self):
        return ("Vous venez de créer un citron de couleur {} et de taille {}"
               .format(self.couleur, self.taille))


citron1 = CitronBasique()
print(citron1)
citron2 = Citron("jaune foncé", "minuscule")
print(citron2)
