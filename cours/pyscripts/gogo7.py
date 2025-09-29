class Citron:
   saveur = "acide"
   
   def __init__(self, couleur="jaune", taille="standard"):
       self.couleur = couleur
       self.taille = taille

   def get_attributes(self):
       return self.saveur, self.couleur, self.taille

   def set_saveur(self, value):
      self.saveur = value

   def set_couleur(self, value):
      self.couleur = value

   def set_taille(self, value):
      self.taille = value

# définition de citron1
citron1 = Citron("jaune pale", "gros")
saveur, couleur, taille = citron1.get_attributes()
print(saveur, couleur, taille)
# changement des attributs de citron1
citron1.set_saveur("très acide")
citron1.set_couleur("jaune foncé")
citron1.set_taille("énorme")
saveur, couleur, taille = citron1.get_attributes()
print(saveur, couleur, taille)
