import time
import tkinter as tk

class MonApp(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        # Création label.
        heure = time.strftime("%H:%M:%S")
        label_heure = tk.Label(self, text=heure, fg="blue", font=("Arial", 30))
        label_heure.pack()
        # Création bouton quitter.
        bouton = tk.Button(self, text="Quitter", command=self.quit)
        bouton.pack()


if __name__ == '__main__':
    app = MonApp()
    app.title('Appli de base')
    app.geometry('250x80')
    app.mainloop()
