#! /usr/bin/env python3

import tkinter as tk

racine = tk.Tk()

text = tk.Text(racine)
text.pack(side=tk.LEFT)
text.insert(tk.INSERT, "Ici s'affichera la sortie")

boutton_ouvrir = tk.Button(racine, text="Ouvrir fichier")
boutton_ouvrir.pack()

label = tk.Label(racine, text="option 1")
label.pack()

listbox = tk.Listbox(racine, height=4)
listbox.pack()
listbox.insert(1, "blabla")
listbox.insert(2, "blabla2")
listbox.insert(3, "blabla3")

label2 = tk.Label(racine, text="option 2")
label2.pack()

listbox2 = tk.Listbox(racine, height=4)
listbox2.pack()
listbox2.insert(1, "blublu")
listbox2.insert(2, "blublu2")
listbox2.insert(3, "blublu3")

boutton_quitter = tk.Button(racine, text="Quitter", command=racine.quit)
boutton_quitter.pack(side=tk.BOTTOM)

racine.title("Ma super GUI pour mon_script.py")
racine.mainloop()
