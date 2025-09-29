class Citron:
    forme = "ellipsoïde" # attribut de classe
    saveur = "acide" # attribut de classe
	
    def __init__(self, couleur="jaune", taille="standard", masse=0):
        self.couleur = couleur # attribut d'instance
        self.taille = taille # attribut d'instance
        self.masse = masse # attribut d'instance (masse en gramme)

    def augmente_masse(self, masse):
        self.masse += masse

citron1 = Citron()
print("Attributs de classe :", citron1.forme, citron1.saveur)
print("Attributs d'instance :", citron1.taille, citron1.couleur, citron1.masse)
citron1.augmente_masse(100)
print("Attributs d'instance :", citron1.taille, citron1.couleur, citron1.masse)
