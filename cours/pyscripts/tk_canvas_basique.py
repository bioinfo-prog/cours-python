import tkinter as tk

racine = tk.Tk()
canv = tk.Canvas(racine, bg="white", height=200, width=200)
canv.pack()
canv.create_oval(0, 0, 200, 200, outline="red", width=10)
canv.create_line(0, 0, 200, 200, fill="black", width=10)
canv.create_line(0, 200, 200, 0, fill="black", width=10)
racine.mainloop()
