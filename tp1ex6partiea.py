from random import randint
x=randint(1,100)
choix=0
while(x!=choix):
    choix=int(input("donner un entier entre 1 et 100\n"))
    if(choix==x):
        print("votre choix est correct")
    elif (choix>x):
        print("votre choix est plus grand")
    else:
        print("votre choix est inferieur")
    
