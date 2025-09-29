import tkinter as tk
import random as rd
import time

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 300
        self.creer_canevas()
        
    def creer_canevas(self):
        # création canevas
        self.canv = tk.Canvas(self, bg="light gray",
                              height=self.size,
                              width=self.size,
                              scrollregion=(0, 0,
                                            self.size+100, self.size+100))
        # barre hozizontale
        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.canv.xview)
        # barre verticale
        self.vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vbar.config(command=self.canv.yview)
        # activer les barres dans le canevas
        self.canv.config(width=self.size, height=self.size)
        self.canv.config(xscrollcommand=self.hbar.set,
                         yscrollcommand=self.vbar.set)
        self.canv.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        # boutton "magique"
        self.boutton_magique = tk.Button(self, text="Abracadabra", command=self.abracadabra)
        self.boutton_magique.pack(side=tk.LEFT)
        self.boutton_quitter = tk.Button(self, text="Quitter", command=self.quit)
        self.boutton_quitter.pack(side=tk.BOTTOM)

    def abracadabra(self):
        for i in range(20):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            col = rd.choice(("black", "red", "green", "blue", "yellow", "magenta", "cyan", "white", "purple"))
            self.canv.create_oval(x, y, x+diameter, y+diameter, fill=col)
    
if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Super Canevas !")
    app.mainloop()
