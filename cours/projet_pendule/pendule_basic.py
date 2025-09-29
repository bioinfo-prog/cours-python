import numpy as np

L = 1          # longueur tige en m
g = 9.8        # accélération gravitationnelle en m/s^2
t = 0          # temps initial en s
theta = np.pi / 4 # angle initial en rad
dtheta = 0     # vitesse angulaire initiale en rad/s
dt = 0.05      # pas de temps en s

print(t, theta*(180/np.pi))

for i in range(200):
    # acc angulaire au tps t (en rad/s^2)
    d2theta = -(g/L) * np.sin(theta)
    # v angulaire mise à jour de t -> t + dt
    dtheta = dtheta + d2theta * dt
    # theta mis à jour de t -> t + dt
    theta = theta + dtheta * dt
    # t mis à jour
    t = t + dt
    # mettre à jour l'affichage
    print(t, theta*(180/np.pi))
