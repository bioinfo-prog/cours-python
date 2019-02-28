import time
import tkinter as tk

class Horloge(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        # Création label.
        heure = time.strftime("%H:%M:%S")
        self.label_heure = tk.Label(self, text=heure, fg="blue",
                                    font=("Arial", 50))
        self.label_heure.pack()
        # Création bouton quitter.
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.pack()
        # On met en marche l'horloge !
        self.mise_a_jour_heure()

    def mise_a_jour_heure(self):
        heure = time.strftime("%H:%M:%S")
        self.label_heure.configure(text=heure)
        self.after(1000, self.mise_a_jour_heure)


if __name__ == "__main__":
    app = Horloge()
    app.title("Horloge")
    app.geometry("300x120")
    app.mainloop()
