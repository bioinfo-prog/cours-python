class Citronnier:
    def __init__(self, nbcitrons, age):
        self.nbcitrons, self.age = nbcitrons, age

    def __call__(self, nbcitrons, age):
        self.nbcitrons, self.age = nbcitrons, age

    def __repr__(self):
        return "Ce citronnier a {} ans et {} citrons".format(self.age, self.nbcitrons)

citronnier1 = Citronnier(10, 3)
print(citronnier1)
citronnier1(30, 4)
print(citronnier1)
