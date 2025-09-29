import tkinter as tk
import random as rd

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 500
        self.creer_widgets()
        
    def creer_widgets(self):
        # création canevas
        self.canv = tk.Canvas(self, bg="light gray", height=self.size,
                              width=self.size)
        self.canv.pack(side=tk.LEFT)
        # bouttons
        self.boutton_cercles = tk.Button(self, text="Cercle !",
                                         command=self.dessine_cercles)
        self.boutton_cercles.pack(side=tk.TOP)
        self.boutton_lignes = tk.Button(self, text="Lignes !",
                                        command=self.dessine_lignes)
        self.boutton_lignes.pack()
        self.boutton_quitter = tk.Button(self, text="Quitter",
                                         command=self.quit)
        self.boutton_quitter.pack(side=tk.BOTTOM)

    def rd_col(self):
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))
    
    def dessine_cercles(self):
        for i in range(20):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            self.canv.create_oval(x, y, x+diameter, y+diameter, fill=self.rd_col())

    def dessine_lignes(self):
        for i in range(20):
            x, y, x2, y2 = [rd.randint(1, self.size) for j in range(4)]
            self.canv.create_line(x, y, x2, y2, fill=self.rd_col())
            
if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Mon Canevas Psychédélique !")
    app.mainloop()
