class Fruit:
    def __init__(self):
        self.__mass = 100

        
class Citron(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        self.__mass = 200

    def print_masse(self):
        print(self._Fruit__mass)
        print(self.__mass)
        
if __name__ == '__main__':
    citron1 = Citron()
    citron1.print_masse()
