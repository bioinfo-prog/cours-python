import tkinter as tk

class Application(tk.Frame):
    def __init__(self, racine="haha"):
        tk.Frame.__init__(self)
        self.racine = racine
        print(self)
        print(racine)
        print(self.racine)
        self.creer_widgets()
        
    def creer_widgets(self):
        self.label = tk.Label(self.racine, text="J'adore Python !")
        self.boutton = tk.Button(self.racine, text="Quitter",
                                 fg="green", command=self.quit)
        self.label.pack()
        self.boutton.pack()		
        print(self.racine)
        print(racine)

if __name__ == '__main__':
    app = Application()
    app.mainloop()
