class Mere1:
    def __init__(self):
        print("coucou dans mere 1")
        self.gogo = 1

class Mere2:
    def __init__(self):
        print("coucou dans mere 2")
        self.gogo = 2

class Mere3:
    def __init__(self):
        print("coucou dans mere 3")
        self.gogo = 3
        
class Fille(Mere1, Mere2, Mere3):
    def __init__(self):
        super().__init__() # revient au même que Mere1.__init__(self)
        #Mere1.__init__(self)
        #Mere2.__init__(self)
        #Mere3.__init__(self)
        self.gigi = self.gogo
        
f = Fille()
print(f.gigi, f.gogo)
