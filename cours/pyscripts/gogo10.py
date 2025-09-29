class Citron:
    """Voici la classe Citron.
    
    Il s'agit d'une classe assez impressionnante qui crée des objets citrons.
    Par défaut une instance de Citron contient l'attribut saveur.
    """
    saveur = "acide"
    
    def __init__(self, couleur="jaune", taille="standard"):
        """Constructeur de la classe Citron : prend deux arguments optionnels couleur et taille."""
        self.couleur = couleur
        self.taille = taille

    def get_attributes(self):
        """Cette méthode renvoie un tuple contenant les attributs de l'instance en cours."""
        return self.saveur, self.couleur, self.taille

    def set_attributs(self, taille=None, couleur=None):
        """Méthode permettant de modifier les attributs d'une instance Citron.
        
        Il suffit de passer en argument un ou deux attributs.
        Il est vivement conseillé d'utiliser le(s) nom(s) de l'argument, par exemple:
        instance.set_attributs(couleur="jaunatre", taille="énorme")
        plutôt que instance.set_attributs("jaunatre", "énorme")
        ainsi vous pouvez les passer dans le désordre.
        """
        if couleur:
            self.couleur = couleur
        if taille:
            self.taille = taille

citron1 = Citron()
help(citron1)
