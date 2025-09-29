class Mere:
    def bonjour(self):
        return "Vous avez le bonjour de la classe mère"

class Fille(Mere):
    def salut(self):
        return "Un salut cordial de la classe fille"

fille = Fille()
print(fille.salut())
print(fille.bonjour())
