#! /usr/bin/env python3

"""Application TKinter de pendule.

Ce script lance une application tkinter montrant le mouvement d'un
pendule. L'utilisateur peut régler l'angle de départ du pendule avec
la règle. En cliquant sur démarrer, le pendule se met en marche. En
cliquant sur arrêter le pendule s'arrête, et si on clique à nouveau
sur démarrer il se remet en marche depuis là où il était. Si on touche
à la règle au cours de son mouvement, celui-ci est stoppé et il faut
cliquer sur démarrer pour le remettre en marche. A chaque mise en
mouvement, une nouvelle couleur est choisie au hasard montrant le
mouvement de la boule. Enfin, l'angle theta en cours est affiché ainsi
que la vitesse angulaire.

Le pendule est considéré comme idéal (mouvement dans un plan 2D, tige
sans masse et rigide, pas de frottement, champ gravitationnel
uniforme). Le mouvement du pendule est calculé en résolvant
numériquement l'équation du mouvement pour un tel pendule :
d^2theta/dt^2 + (g/l)*sin(theta) = 0.

Lancement: python3 ./tk_pendule.py

Auteur: Patrick Fuchs (Sept 2018)

Inspiré des sites suivants:
http://pages.physics.cornell.edu/~sethna/StatMech/ComputerExercises/Pendulum/
https://en.wikipedia.org/wiki/Pendulum_(mathematics)#math_Eq._1
"""

import tkinter as tk
import random as rd
import numpy as np

COLORS = ['black', 'white', 'red', 'orange', 'yellow', 'green',
          'turquoise', 'blue', 'purple', 'magenta']


# Classe principale qui hérite de la classe Tk.
class AppliPendule(tk.Tk):
    """Classe principale de l'application (contient la fenêtre Tk)."""

    def __init__(self):
        """Constructeur de la classe, aucun argument n'est nécessaire."""
        # Appel du constructeur de la classe mère.
        # L'instance de la fenêtre principale se retrouve dans le self.
        tk.Tk.__init__(self)
        # Drapeau pour le mouvement (0 immobile, > 0 en mouvement).
        self.is_moving = 0
        # Grandeurs physiques.
        self.t = 0  # temps (s)
        self.dt = 0.05  # time step (s)
        self.g = 9.8   # acc gravitationnelle (m s^-2)
        self.theta = 0.75*np.pi  # angle initial
        self.dtheta = 0.0   # vitesse angulaire = derivée première
                            # (pendule au repos au départ)
        self.L = 1  # longueur de la tige dans le repère canvas (m)
        self.x = np.sin(self.theta) * self.L   # qd theta = 0 le pendule
        self.y = -np.cos(self.theta) * self.L  # pointe vers le bas.
        # Conversion x, y en coord ds le canevas (attention, les y
        # descendent alors que ds notre repère ils montent !!!).
        self.x_c, self.y_c = self.map_realcoor2canvas(self.x, self.y)
        # Création du canevas (inclus dans la fenêtre mère).
        self.canv = tk.Canvas(self, bg='gray', height=400, width=400)
        # Dessin du pivot.
        self.canv.create_oval(190, 190, 210, 210, width=1, fill="blue")
        # Dessin de la baballe.
        self.size = 30  # Taille de la baballe ds le repère du canvas.
        self.baballe = self.canv.create_oval(self.x_c-(self.size/2),
                                             self.y_c-(self.size/2),
                                             self.x_c+(self.size/2),
                                             self.y_c+(self.size/2),
                                             width=1, fill="blue")
        # Création de la tige.
        self.tige = self.canv.create_line(200, 200, self.x_c,
                                          self.y_c, fill="blue")
        # Création d'une ligne à x = 0 et y = 0.
        self.canv.create_line(0, 200, 400, 200, dash=(3, 3))
        self.canv.create_line(200, 0, 200, 400, dash=(3, 3))
        # Création des boutons.
        btn1 = tk.Button(self, text="Quitter", command=self.quit)
        btn2 = tk.Button(self, text="Demarrer", command=self.start)
        btn3 = tk.Button(self, text="Arrêter", command=self.stop)
        # Création d'une règle pour la valeur initiale de theta
        # (on lui met la valeur initiale 0.9*pi).
        self.theta_scale = tk.Scale(self, from_=-np.pi, to=np.pi,
                                    resolution=0.001,
                                    command=self.update_theta_scale)
        self.theta_scale.set(self.theta)
        scale_description = tk.Label(self, text="valeur\ninitiale\nde theta",
                                     fg="blue")
        # Création d'un Label pour voir les caractéristiques de la Baballe.
        # On utilise une Stringvar (permet de mettre à jour l'affichage).
        self.stringvar_pos_display = tk.StringVar()
        display_theta = tk.Label(self, textvariable=self.stringvar_pos_display,
                                 fg="blue", font=("Courier New", 12))
        # Placement des widgets dans la fenêtre Tk.
        # D'abord le canevas puis les bouttons.
        self.canv.pack(side=tk.LEFT)
        btn1.pack(side=tk.BOTTOM)  # boutton quitter
        btn2.pack()
        btn3.pack()
        display_theta.pack()
        # Puis la règle et sa description.
        scale_description.pack(side=tk.LEFT)
        self.theta_scale.pack(side=tk.RIGHT)
        # Une fois le label "packé", on peut mettre une valeur à l'intérieur.
        self.stringvar_pos_display.set(self.get_pos_displ())

    def get_pos_displ(self):
        """Renvoie une chaine avec la position et la vitesse (angulaire)."""
        return (f"{'theta':>5s} {'dtheta':>10s}\n"
                f"{'(rad)':>5s} {'(rad/dt)':>10s}\n"
                f"{self.theta:>5.1f} {self.dtheta:>10.1f}")

    def map_realcoor2canvas(self, x, y):
        """Transforme les coordonnées réelles en coordonnées dans le canevas."""
        # L = 1 m --> 100 pix dans le canvas.
        conv_factor = 100
        xprime = x*conv_factor + 200
        yprime = -y*conv_factor + 200
        return xprime, yprime

    def update_theta_scale(self, value):
        """Met à jour la position de la baballe quand la règle est touchée."""
        # On arrête le mouvement du pendule.
        self.stop()
        self.dtheta = 0.0
        # On met à jour le pendule avec la nouvelle valeur.
        self.theta = float(value)
        self.x = np.sin(self.theta) * self.L
        self.y = -np.cos(self.theta) * self.L
        # Conversion ds le repère du canvas.
        self.x_c, self.y_c = self.map_realcoor2canvas(self.x, self.y)
        # On met à jour les coordonnées (baballe + tige).
        self.canv.coords(self.baballe,
                         self.x_c-(self.size/2),
                         self.y_c-(self.size/2),
                         self.x_c+(self.size/2),
                         self.y_c+(self.size/2))
        self.canv.coords(self.tige, 200, 200, self.x_c, self.y_c)
        # On met à jour la zone de texte.
        self.stringvar_pos_display.set(self.get_pos_displ())
        # On remet à 0 le temps.
        self.t = 0

    def move(self):
        """Déplace la baballe et met à jour les coordonnées.

        S'auto-rappelle après 20 ms.
        """
        # Calcul du nouveau theta avec un Euler semi-implicite.
        # (d2theta = dérivée seconde).
        self.d2theta = -(self.g/self.L) * np.sin(self.theta)
        self.dtheta += self.d2theta * self.dt
        self.theta += self.dtheta * self.dt
        # Conversion theta -> x & y.
        self.x = np.sin(self.theta) * self.L
        self.y = -np.cos(self.theta) * self.L
        # Conversion ds le repère du canvas.
        self.x_c, self.y_c = self.map_realcoor2canvas(self.x, self.y)
        # On met à jour les coordonnées (baballe + tige).
        self.canv.coords(self.baballe,
                         self.x_c-(self.size/2),
                         self.y_c-(self.size/2),
                         self.x_c+(self.size/2),
                         self.y_c+(self.size/2))
        self.canv.coords(self.tige, 200, 200, self.x_c, self.y_c)
        # Laisser une trace.
        self.canv.create_line(self.x_c, self.y_c, self.x_c+1,
                              self.y_c+1, fill=self.color_trace)
        # On met à jour la zone de texte.
        self.stringvar_pos_display.set(self.get_pos_displ())
        self.t += self.dt
        # On refait appel à la méthode .move().
        if self.is_moving > 0:
            self.after(20, self.move)  # boucle toutes les 20ms

    def start(self):
        """Démarre l'animation."""
        self.color_trace = rd.choice(COLORS)
        self.is_moving += 1  # préférable à is_moving = 1
                             # (1 seul appel de la fct move)
        if self.is_moving == 1:
            self.move()

    def stop(self):
        """Arrête l'animation."""
        self.is_moving = 0


if __name__ == "__main__":
    """Programme principal.

    Instancie la classe principale, donne un titre et lance le gestionnaire
    d'évènements.
    """
    app_pendule = AppliPendule()
    app_pendule.title("Pendule")
    app_pendule.mainloop()
