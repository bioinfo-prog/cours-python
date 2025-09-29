class Citron:
    saveur = "acide"

citron1 = Citron()
print(citron1.saveur)
citron1.saveur = "sucrée"
print(citron1.saveur)
del citron1.saveur
print(citron1.saveur)
del citron1.saveur
