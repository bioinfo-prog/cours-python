class Citron:
    def __init__(self):
        self.__mass = 100

    def get_mass(self):
        return self.__mass

if __name__ == '__main__':
    citron1 = Citron()
    #print(citron1.get_mass())
    #print(citron1.__mass)
    print(citron1.__dict__)
    citron1._Citron__mass = -100
    print(citron1.get_mass())
    print(citron1._Citron__mass)
