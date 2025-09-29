class Citron:
   def __init__(self, couleur="jaune", masse=0):
       self.couleur = couleur
       self.masse = masse # masse en g

   def get_masse(self):
       return self.masse

   def get_couleur(self):
       return self.couleur

   def set_couleur(self, value):
       self.couleur = value

   def set_masse(self, value):
       if value < 0:
           raise ValueError("Z'avez déjà vu une masse négative ???")
       self.masse = value

if __name__ == '__main__':
    # définition de citron1
    citron1 = Citron()
    print(citron1.get_couleur(), str(citron1.get_masse()))
    # on change les attributs de citron1 avec les setters
    citron1.set_couleur("jaune foncé")
    citron1.set_masse(100)
    print(citron1.get_couleur(), str(citron1.get_masse()))
    # on le rechange sans les setters
    citron1.couleur = "pourpre profond"
    citron1.masse = -15
    print(citron1.get_couleur(), str(citron1.get_masse()))

