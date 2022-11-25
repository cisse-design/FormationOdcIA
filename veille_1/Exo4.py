import random
import statistics

L = []
S = 100
def generator():
    for t in range(0, S):
        number = random.random()
        L.append(number)
    print("la liste est :")
    print(L)
generator()

def moy():
    moyenne=(statistics.mean(L))
    print("la moyenne de cette liste est :")
    print(moyenne)
moy()

def medianne():
    medianne=(statistics.median(L))
    print("la medianne de cette liste est :")
    print(medianne)
medianne()

def variance():
    variance=(statistics.variance(L))
    print('la variance de cette liste est :')
    print(variance)
variance()

def ecart_type():
    ecart_type=(statistics.pstdev(L))
    print("l'ecart_type de cette liste est :")
    print(ecart_type)
ecart_type()