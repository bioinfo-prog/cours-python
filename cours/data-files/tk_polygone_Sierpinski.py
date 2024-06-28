import math
import random
import tkinter as tk

class PolygoneSierpinski(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        # Création des widgets.
        self.canevas = tk.Canvas(self, width=400, height=400, bg="lightgrey")
        self.bouton1 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton2 = tk.Button(self, text="Launch!", command=self.launch)
        self.label = tk.Label(self, text="Cliquez sur Launch pour afficher "
                              "10000 points supplémentaires !")
        self.label2 = tk.Label(self, text="Choix nombre\nde sommets")
        self.listbox = tk.Listbox(self, height=8, width=4)
        # Packing des widgets.
        self.label.pack(side=tk.TOP)
        self.canevas.pack(side=tk.LEFT)
        self.bouton1.pack(side=tk.TOP)
        self.bouton2.pack(side=tk.TOP)
        self.label2.pack(side=tk.BOTTOM)
        self.listbox.pack(side=tk.BOTTOM)
        # On ajoute des items à la listbox (entiers).
        for i in range(3, 10+1):
            self.listbox.insert(tk.END, i)
        # Selectionne premier élément de listbox.
        self.listbox.select_set(0)
        # Lier une méthode quand clic sur listbox.
        self.listbox.bind('<<ListboxSelect>>', self.clic_listbox)
        # Definition des sommets (par défaut, 3 sommets).
        # self.sommets est un dico, par exemple :
        # {0: (200.0, 0.0), 1: (26.8, 300.0), 2: (373.2, 300.0)}
        self.nb_sommets = 3
        self.sommets = self._calc_nb_sommets(self.nb_sommets)
        # Coord initiale du point qui va bouger (on démarre au centre).
        self.x, self.y = (200, 200)
        # Dessin du centre et des sommets.
        self.dessine_centre_sommets()
        
    def launch(self):
        for i in range(10000):
            # On tire un entier au hasard.
            nb_alea = random.randint(0, len(self.sommets)-1)
            # On calcule le nouveau point et on le dessine.
            self.x = (self.x + self.sommets[nb_alea][0])/2
            self.y = (self.y + self.sommets[nb_alea][1])/2
            self.canevas.create_oval(self.x, self.y, self.x, self.y)

    def clic_listbox(self, event):
        # Récup du widget à partir de l'objet event.
        widget = event.widget
        # Récup du choix sélectionné dans la listbox (tuple).
        # (par exemple renvoie `(5,)` si on a cliqué sur `5`)
        selection = widget.curselection()
        # Récup du nombre sélectionné (déjà un entier).
        self.nb_sommets = widget.get(selection[0])
        # Récup coord des sommets.
        self.sommets = self._calc_nb_sommets(self.nb_sommets)
        # Nettoyage du canvas
        self.canevas.delete("all")
        # réinit du point qui se déplace
        self.x, self.y = (200, 200)
        # On dessine le centre et les sommets
        self.dessine_centre_sommets()
        

    # Fonctions qui calcule la position (x,y) des sommets (son nom commence par
    # un underscore car elle n'a pas à être utilisée en dehors de la classe).
    # Le centre du polygone se trouve au point (200, 200).
    # A  partir du centre du polygone et du premier point, nous allons tourner
    # pour trouver les autres sommets (par exemple, tous les 120° pour un
    # triangle).
    def _calc_nb_sommets(self, nb_sommets):
        # Dico de tuple pour contenir les sommets.
        sommets = {}
        # Le premier sommet se trouvera au point (0, 200).
        # (c'est-à-dire à un angle de pi/2 dans le cercle trigonométrique)
        theta = math.pi / 2
        for i in range(nb_sommets):
            # Le rayon de notre polygone est 200. Attention pour la coord y,
            # il faut inverser le sens de l'axe (tkinter descend, en maths
            # ça monte !).
            x = math.cos(theta) * 200
            y = -math.sin(theta) * 200
            # Translation car centre du polygone au point (200, 200).
            x += 200
            y += 200
            # Ouf on a le point du sommet :-) !
            sommets[i] = (x, y)
            # Mise à jour de theta pour le prochain sommet.
            theta += (2*math.pi) / nb_sommets
        print(sommets)
        return sommets

    def dessine_centre_sommets(self):
        # Dessin point central.
        self.canevas.create_oval(self.x, self.y, self.x, self.y, outline="red")
        # Dessin sommets (attention sommets est un dico de tuple !).
        for i in self.sommets:
            x, y = self.sommets[i][0], self.sommets[i][1]
            self.canevas.create_oval(x, y, x, y, outline="red")


if __name__ == '__main__':
    app = PolygoneSierpinski()
    app.title('Polygone de Sierpinski')
    app.mainloop()
