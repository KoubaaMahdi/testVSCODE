from random import randint
from sys import exit
x=randint(1,100)
choix=0
niveau=''
attemps=0
while(True):
    niveau=input("Choisissez la difficulté du jeu\n facile pour 12 tentatives\n moyen pour 7 tentatives\n difficile pour 4 tentatives\n")
    if (niveau=="facile" or niveau=="moyen" or niveau=="difficile"):
        break
if (niveau=="facile"):
    while(attemps<12 and x!=choix):
        while(True):
            choix=int(input("donner un entier entre 1 et 100\n"))
            if (choix>=1 and choix <=100):
                break
        if(choix==x):
            print("votre choix est correct")
            exit(d)
        elif (choix>x):
            print("votre choix est plus grand")
        else:
            print("votre choix est inferieur")
        attemps+=1
    print("vous avez perdu")
elif (niveau=="moyen"):
    while(attemps<7 and x!=choix):
        while(True):
            choix=int(input("donner un entier entre 1 et 100\n"))
            if (choix>=1 and choix <=100):
                break
        if(choix==x):
            print("votre choix est correct")
            exit()
        elif (choix>x):
            print("votre choix est plus grand")
        else:
            print("votre choix est inferieur")
        attemps+=1
    print("vous avez perdu")
elif(niveau=="difficile"):
    while(attemps<4 and x!=choix):
        while(True):
            choix=int(input("donner un entier entre 1 et 100\n"))
            if (choix>=1 and choix <=100):
                break
        if(choix==x):
            print("votre choix est correct")
            exit()
        elif (choix>x):
            print("votre choix est plus grand")
        else:
            print("votre choix est inferieur")
        attemps+=1
    print("vous avez perdu")

    
    
