import tkinter as tk

def gogo():
    print("GOGO !")

racine = tk.Tk()
label = tk.Label(racine, text="J'adore Python !")
bouton = tk.Button(racine, text="Quitter", command=racine.destroy)
bouton2 = tk.Button(racine, text="GOGO", fg="green", command=gogo)
bouton["fg"]="red"
label.pack()
bouton.pack()
bouton2.pack()
racine.mainloop()
print("C'est fini !")
