import math

class Exo1:

    def __init__(self):
        self.l1 = None  #une liste de valeur comprise entre -N et N
        self.N = 0

    def calcul_f(self,x):
        return (x / (x ** 2 + 1))

    def calcul_g(self,x):
        return math.atan(x)

    def create_liste(self):
        self.l1=[]
        self.N = int(input("Entrez un nombre : "))
        for i in range(-self.N, self.N + 1):
            self.l1.append(i)
        print("La liste : ")
        print(self.l1)

    def somme_function(self):
        R = 0
        for i in self.l1:
            R += (self.calcul_f(i) - self.calcul_g(i)) ** 2
        return R


d1= Exo1()

d1.create_liste()

print(d1.somme_function())

