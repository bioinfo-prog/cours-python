"""Super appli baballe !!!
Usage: python3 ./tk_baballe.py
- clique gauche: faire grossir la baballe
- clique droit: faire rétrécir
- clique central: relance la baballe (depuis le  point du clique) 
                  dans une direction aléatoire
- touche Esc: quitte l'appli baballe"""

import tkinter as tk
import random as rd

class AppliBaballe(tk.Tk):
    def __init__(self):
        """Constructeur de l'appli"""
        tk.Tk.__init__(self)
        # coord ini baballe
        self.x, self.y = 200, 200
        # rayon ini baballe
        self.size = 50
        # pas de deplacement
        self.dx, self.dy = 20, 20
        # création et packing du canvas
        self.canv = tk.Canvas(self, bg='light gray', height=400, width=400)
        self.canv.pack()
        # création de la baballe
        self.baballe = self.canv.create_oval(self.x, self.y,
                                             self.x+self.size,
                                             self.y+self.size,
                                             width=2, fill="blue")
        # binding des actions (clique gauche: démarre la baballe, esc: quitte)
        self.canv.bind("<Button-1>", self.incr)
        self.canv.bind("<Button-2>", self.boom)
        self.canv.bind("<Button-3>", self.decr)
        self.bind("<Escape>", self.stop)
        # lancer la baballe
        self.move()

    def move(self):
        """Déplace la baballe (rappelée itérativement avec la méthode after)."""
        # incr coord baballe
        self.x += self.dx
        self.y += self.dy
        # vérifier que la baballe ne sort pas du canvas (choc élastique)
        if self.x < 10:
            self.dx = abs(self.dx)
        if self.x > 400-self.size-10:
            self.dx = -abs(self.dx)
        if self.y < 10:
            self.dy = abs(self.dy)
        if self.y > 400-self.size-10:
            self.dy = -abs(self.dy)
        # mise à jour des  coord
        self.canv.coords(self.baballe, self.x, self.y, self.x+self.size,
                         self.y+self.size)
        # rappel de move toutes les 50ms
        self.after(50, self.move)

    def incr(self, lclick):
        """Augmente la taille de la baballe"""
        self.size += 10
        if self.size > 200:
            self.size = 200

    def decr(self, rclick):
        """Diminue la taille de la baballe"""
        self.size -= 10
        if self.size < 10:
            self.size = 10

    def boom(self, mclick):
        """Relance la baballe dans une direction aléatoire au point du clique"""
        self.x = mclick.x
        self.y = mclick.y
        self.canv.create_text(self.x, self.y, text="Boom !", fill="red")
        self.dx = rd.choice([-30, -20, -10, 10, 20, 30])
        self.dy = rd.choice([-30, -20, -10, 10, 20, 30])

    def stop(self, esc):
        """Quitte l'application"""
        self.quit()

if __name__ == "__main__":
    myapp = AppliBaballe()
    myapp.title("Baballe !")
    myapp.mainloop()
