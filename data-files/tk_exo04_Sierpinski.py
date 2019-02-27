import random
import tkinter as tk

class TriangleSierpinski(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        # Création + packing des widgets.
        self.canevas = tk.Canvas(self, width=400, height=400, bg="lightgrey")
        self.bouton1 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton2 = tk.Button(self, text="Launch!", command=self.launch)
        self.label = tk.Label(self, text="Cliquez sur Launch pour afficher "
                              "10000 points supplémentaires !")
        self.label.pack(side=tk.TOP)
        self.canevas.pack(side=tk.LEFT)
        self.bouton1.pack(side=tk.TOP)
        self.bouton2.pack(side=tk.TOP)
        # Definition des sommets
        # (attention au système de coordonnées du canvas !).
        self.sommets = {0: (200, 0), 1: (0, 400), 2: (400, 400)}
        # Coordonnees du point.
        self.x, self.y = (200, 200)
        # Dessin du premier point.
        self.canevas.create_oval(self.x, self.y, self.x, self.y)

    def launch(self):
        for i in range(10000):
            # On tire un entier au hasard.
            nb_alea = random.randint(0,2)
            # On calcule le nouveau point et on le dessine.
            self.x = (self.x + self.sommets[nb_alea][0])/2
            self.y = (self.y + self.sommets[nb_alea][1])/2
            self.canevas.create_oval(self.x, self.y, self.x, self.y)


if __name__ == '__main__':
    app = TriangleSierpinski()
    app.title('Sierpinski')
    app.mainloop()
    
