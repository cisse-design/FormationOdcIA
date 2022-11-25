
reponse = 'oui'
while(reponse.__eq__('oui')):
    nom=input("Entrez un nom : ")
    n=input("Entrez l'exercice que vous voulez faire, (1 OU 2)  :")

    try:
        n=int(n)
        
    except:
        print("valeur non prise en charge")
    else:
        if n==1:
            print("Hello ",nom," Bienvenue dans l'exo1")
            import Exo1
        elif n==2:
            print("Hello ",nom," Bienvenue dans l'exo2")
            import Exo2
    
    reponse = input("Voulez-vous continuez ?: (oui/non)")
    
    



