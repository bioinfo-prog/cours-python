class Citron:
   def __init__(self, masse=0):
      print("(2) J'arrive dans le .__init__()")
      self.masse = masse # self.masse appelle .set_masse()
                         # donc on a contrôle de la valeur => mieux
                         # si on met self._masse = masse
                         # il s'agit de la vraie valeur donc
                         # pas d'appel à .set_masse
      
   def get_masse(self):
      print("Coucou je suis dans le get")
      return self._masse # surtout ne pas mettre self.masse 
                         # sinon ça part en récursion et ça plante !!!
                         # RecursionError: maximum recursion depth exceeded

   def set_masse(self, valeur):
      print("Coucou je suis dans le set")
      if valeur < 0:
         raise ValueError("Z'avez déjà vu une masse négative ? C'est nawak")
      self._masse = valeur # surtout ne pas mettre self.masse
                           # sinon ça part en récursion et ça plante !!!
                           # RecursionError: maximum recursion depth exceeded

   def del_masse(self):
      print("Coucou je suis dans le del")
      del self._masse

   masse = property(fget=get_masse, fset=set_masse, fdel=del_masse)


if __name__ == '__main__':
   print("(1) Dans le programme principal, je vais instancier un Citron")
   citron = Citron(masse=100)
   print("(3) Je reviens dans le programme principal")
   print("La masse de notre citron est {} g".format(citron.masse))
   # on mange le citron
   citron.masse = 25
   print("La masse de notre citron est {} g".format(citron.masse))
   print(citron.__dict__)
