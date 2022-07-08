from random import randint
x=randint(1,100)
choix=0
niveau=''
attemps=0
tentatives=0
while(True):
    niveau=input("Choisissez la difficulté du jeu\n facile pour 12 tentatives\n moyen pour 7 tentatives\n difficile pour 4 tentatives\n")
    if (niveau=="facile" or niveau=="moyen" or niveau=="difficile"):
        break
if (niveau=="facile" ): 
        tentatives=12
elif (niveau=="moyen" ): 
        tentatives=7
elif (niveau=="difficile" ): 
        tentatives=4
while(attemps<tentatives):
    choix=int(input("donner un entier entre 1 et 100\n"))
    if(choix==x):
        print("votre choix est correct")
        break
    elif (choix>x):
        print("votre choix est plus grand")
    else:
        print("votre choix est inferieur")
    attemps+=1
if (attemps==tentatives):
    print("vouz avez perdu")

         
        
        
   
    
    
