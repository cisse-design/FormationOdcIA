import random


def function_f(x):
    return (x**3+3*(x**2)-5)

D=[]
#S est la taille des sous listes de D et n le nombre de sous listes que contients D
S=input("Entrez une Taille : ")
n=input("Entrez le nombre de sous liste : ")

try:
    S = int(S)
    n = int(n)
except:
    print("Valeur non prise en charge")
else:
    #Fonction de génération aléatoire des sous listes de D
    #l est la liste créer pour remplir D et numbre le nombre générer pour remplir l
    def create_liste(list,nb_sous_list,taille_sous_list):
        for i in range(nb_sous_list):
            l=[]
            for j in range(taille_sous_list):
                number = random.randint(0,10)
                l.append(number)
            list.append(l)
        print(D)

    create_liste(D,n,S)

    #Fonction de calcul du minimum d'une liste passée en paramètre et nombre d'iteration
    def min_list(L,t):
        minV=L[0]
        for i in range(0,t):
            if(minV>L[i]):
                minV=L[i]
        return minV

    #Fonction de calcul du maximum d'une liste passée en paramètre et nombre d'iteration
    def max_list(L,t):
        maxV=L[0]
        for i in range(0,t):
            if(maxV<L[i]):
                maxV=L[i]
        return maxV

    minGlobalD=[]   #Est une liste qui contient le minimum de chaque sous liste de D
    maxGlobalD=[]   #Est une liste qui contient le maximum de chaque sous liste de D
    print("Les minimum des listes de D sont: ")
    for i in range(n):
        minG = min_list(D[i],S)   #Appel de la fonction min_list() avec en argument les différentes sous listes de D
        print(minG)
        minGlobalD.append(minG)

    print("Les Maximum des listes de D sont: ")
    for i in range(n):
        maxG= max_list(D[i],S)    #Appel de la fonction max_list() avec en argument les différentes sous listes de D
        print(maxG)
        maxGlobalD.append(maxG)

    print("Le minimum Global de D est: ")
    print(min_list(minGlobalD,n))     #Affichage du minimum des minimums des sous listes de D

    print("Le Maximum Global de D est: ")
    print(max_list(maxGlobalD,n))     #Affichage du maximum des maximums des sous listes de D

    #Dprime est une liste qui contient les images de D par la fonction f(x)=x**3+3*(x**2)-5
    #l est une liste temporaire utiliser pour remplir Dprime
    def calcul_Dprime(list):
        Dprime = []
        for i in range(0,n):
            l = []
            for j in range(0,S):
                l.append(function_f(list[i][j]))
            Dprime.append(l)
        print(Dprime)

    print("Les valeurs de D' :")
    calcul_Dprime(D)
        
