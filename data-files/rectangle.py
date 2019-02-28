class Rectangle:
    """Ceci est la classe Rectangle."""

    def __init__(self, long=0.0, larg=0.0, coul="blanc"):
        """Initialisation d'un objet.

        Définition des attributs avec des valeurs par défaut.
        """
        self.longueur = long
        self.largeur = larg
        self.couleur = coul

    def calcule_surface(self):
        """Méthode qui calcule la surface."""
        return self.longueur * self.largeur

    def change_carre(self, cote):
        """Méthode qui transforme un rectangle en carré."""
        self.longueur = cote
        self.largeur = cote


if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe Rectangle.
    
