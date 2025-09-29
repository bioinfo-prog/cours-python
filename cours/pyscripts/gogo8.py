class Citron:
   def __init__(self, couleur="jaune", taille="standard"):
       self.couleur = couleur
       self.taille = taille

   def get_attributs(self):
       return self.couleur, self.taille

   def set_couleur(self, value):
      self.couleur = value

   def set_taille(self, value):
      self.taille = value

# définition de citron1
citron1 = Citron("jaune pâle", "gros")
couleur, taille = citron1.get_attributs()
print(couleur, taille)
# changement des attributs de citron1
citron1.set_couleur("jaune foncé")
citron1.set_taille("énorme")
couleur, taille = citron1.get_attributs()
print(couleur, taille)
