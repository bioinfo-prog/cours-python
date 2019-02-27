import tkinter as tk

class MaListBox(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        self.listbox = tk.Listbox(self, height=10, width=4)
        self.listbox.pack()
        # On ajoute des items à la listbox (entiers).
        for i in range(1, 10+1):
            # Utilisation de ma méthode .insert(index, element)
            # On ajoute l'entier i (tk.END signifie en dernier).
            self.listbox.insert(tk.END, i)
        # Selectionne premier élément de listbox.
        self.listbox.select_set(0)
        # Lier une méthode quand clic sur listbox.
        self.listbox.bind('<<ListboxSelect>>', self.clic_listbox)

    def clic_listbox(self, event):
        # Récup du widget à partir de l'objet event.
        widget = event.widget
        # Récup du choix sélectionné dans la listbox (tuple).
        # (par exemple renvoie `(5,)` si on a cliqué sur `5`)
        selection = widget.curselection()
        # Récup du nombre sélectionné (déjà un entier).
        choix_select = widget.get(selection[0])
        # affichage
        print("Le choix sélectionné est {}, son type est {}"
              .format(choix_select, type(choix_select)))


if __name__ == '__main__':
    app = MaListBox()
    app.title('MaListBox')
    app.mainloop()
