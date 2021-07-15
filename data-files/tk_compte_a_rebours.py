import sys
import time
import tkinter as tk

class CompteARebours(tk.Tk):
    def __init__(self, minutes_rebours):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        # Calcul du temps en secondes.
        self.secondes_rebours = minutes_rebours * 60
        # Création label.
        temps_affiche = self.seconds2time(self.secondes_rebours)
        self.label_heure = tk.Label(self, text=temps_affiche, fg="blue",
                                    font=("Arial", 50))
        self.label_heure.pack()
        # Création bouton quitter.
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.pack()
        # Création bouton lancer le compte à rebours !
        self.bouton2 = tk.Button(self, text="Lancer",
                                 command=self.mise_a_jour_rebours)
        self.bouton2.pack()

    # Fonction qui prend un nb de secondes en arguments et renvoie
    # une string formatée HH:MM:SS.
    def seconds2time(self, total_secondes):
        h = total_secondes // (60*60)
        secondes_restantes = total_secondes % (60*60)
        m = secondes_restantes // 60
        s = secondes_restantes % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def mise_a_jour_rebours(self):
        # Fini ?
        if self.secondes_rebours == 0:
            for i in range(10):
                print("C'est fini !!!")
            self.quit()
        # Mise à jour nombre de secondes.
        self.secondes_rebours -= 1
        # Mise à jour affichage.
        temps_affiche = self.seconds2time(self.secondes_rebours)
        self.label_heure.configure(text=temps_affiche)
        # Relance après 1000 ms.
        self.after(1000, self.mise_a_jour_rebours)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: tk_compte_rebours.py temps_rebours\n"
             "temps_rebours = nombre de minutes entre 1 et 240 (entier)")
    try:
        temps_rebours = int(sys.argv[1])
    except:
        exit("Entrez un nombre de minutes entre 1 et 240")
    if temps_rebours < 1 or temps_rebours > 240:
        raise ValueError("Entrez un nombre de minutes entre 1 et 240")
    app = CompteARebours(temps_rebours)
    app.title("Compte à rebours")
    # Règle la taille de la fenêtre initiale.
    app.geometry("300x150")
    app.mainloop()
