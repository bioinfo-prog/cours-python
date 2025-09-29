import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.creer_widgets()
        
    def creer_widgets(self):
        self.label = tk.Label(self.master, text="J'adore Python !")
        self.boutton = tk.Button(self.master, text="Quitter",
                                 fg="green", command=self.quit)
        self.label.pack()
        self.boutton.pack()		

if __name__ == '__main__':
    racine = tk.Tk()
    racine.title("Ma Première App :-)")
    app = Application(racine)
    racine.mainloop()
