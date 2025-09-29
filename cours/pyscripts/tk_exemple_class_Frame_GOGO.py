import tkinter as tk

class Application(tk.Frame):
    def __init__(self, gogo=None):
        tk.Frame.__init__(self)
        self.gogo = gogo
        print(self.gogo)
        print(str(self.gogo))
        print(type(self.gogo))
        self.creer_widgets()
        
    def creer_widgets(self):
        self.label = tk.Label(self.gogo, text="J'adore Python !")
        self.boutton = tk.Button(self.gogo, text="Quitter",
                                 fg="green", command=self.quit)
        self.label.pack()
        self.boutton.pack()		


if __name__ == '__main__':
    app = Application()
    app.mainloop()
