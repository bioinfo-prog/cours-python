class Citron:
   def __init__(self, couleur="jaune", taille="standard", masse=0):
      self.couleur = couleur
      self.taille = taille

   def get_attributs(self):
      return self.couleur, self.taille

   def set_attributs(self, taille=None, couleur=None):
      if couleur:
         self.couleur = couleur
      if taille:
         self.taille = taille

# définition de citron1
citron1 = Citron("jaune pâle", "gros")
couleur, taille = citron1.get_attributs()
print(couleur, taille)
# on change son attribut taille
citron1.set_attributs(taille="gigantesque")
couleur, taille = citron1.get_attributs()
print(couleur, taille)
# on change ses attributs couleur et taille
citron1.set_attributs(couleur="blanc", taille="petite")
couleur, taille = citron1.get_attributs()
print(couleur, taille)

