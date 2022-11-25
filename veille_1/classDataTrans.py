import random

class DataTrans:
    def min_list(self,L,t):
        minV = L[0]
        for i in range(0, t):
                if (minV > L[i]):
                    minV = L[i]
        return minV


    def max_list(self,L,t):
            maxV = L[0]
            for i in range(0, t):
                if (maxV < L[i]):
                    maxV = L[i]
            return maxV

    def max_and_min(self):
            minGlobalD = []
            maxGlobalD = []
            print("Les minimum des listes de D sont: ")
            for i in range(0, self.n):
                minG = self.min_list(self.D[i],self.S)
                print(minG)
                minGlobalD.append(minG)

            print("Les Maximum des listes de D sont: ")
            for i in range(0, self.n):
                maxG = self.max_list(self.D[i],self.S)
                print(maxG)
                maxGlobalD.append(maxG)

            print("Le minimum Global de D est: ")
            print(self.min_list(minGlobalD,self.n))

            print("Le Maximum Global de D est: ")
            print(self.max_list(maxGlobalD,self.n))


    def lacalcul_D(self):
            Dprime = []
            for i in range(0, self.n):
                l = []
                for j in range(0, self.S):
                    l.append(self.function_f(self.D[i][j]))
                Dprime.append(l)
            print(Dprime)


    def function_f(self,x):
        return (x ** 3 + 3 * (x ** 2) - 5)

    def __init__(self):
        self.D = None

    def __int__(self):
        self.D= None
        self.n=0
        self.S=0

    def create_liste(self):
        try:
            S = int(input("Entrez une Taille : "))
            n = int(input("Entrez le nombre de sous liste : "))
        except:
            print("Valeur non prise en charge")
        else:
            self.D=[]
            self.S = S
            self.n = n

            for i in range(0, n):
                l = []
                for j in range(0, S):
                    number = random.randint(0, 50)
                    l.append(number)
                self.D.append(l)
            print(self.D)

d1 = DataTrans()
d1.create_liste()
d1.max_and_min()
print("Les valeurs de D' :")
d1.lacalcul_D()
