import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()
        print(self)
        print(type(self))

    def creer_widgets(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.boutton = tk.Button(self, text="Quitter", fg="red", command=self.quit)
        self.label.pack()
        self.boutton.pack()		

if __name__ == '__main__':
    app = Application()
    app.title('Ma Première App :-)')
    app.mainloop()
