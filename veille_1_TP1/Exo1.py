import math

def calcul_f(x):
    return (x/(x**2+1))

def calcul_g(x):
    x= math.atan(x)
    return x

N= input("Entrez un nombre : ")

try:
    N =int(N)
except:
    print("Valeur non prise en charge")
else:
    #l1 est une liste qui a pour valeur (-N,-(N-1),-(N-2),...,0,1,2,....,N)
    l1 = list(range(-N, N+1))
    print("LA liste")
    print(l1)

    #Cette fonction permet de retourner la valeur de R qui est égale à somme(f(x)-g(x))**2
    def somme_function():
        R=0
        for i in l1:
            R+=(calcul_f(i)-calcul_g(i))**2
        return R

    print("Valeur de R = ",somme_function())