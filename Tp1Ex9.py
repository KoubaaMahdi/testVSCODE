#1)
listAut=["Mohamed","Ali","Sami","Olfa","Atef"]
dictLiv={'liv1':["Analyse",1999,1],'liv2':["Algébre",1989,3],'liv3':["Base de données",2003,2],'liv4':["Mécanique",2000,4],'liv5':["Analyse2",2003,1]}
print(dictLiv)
if ("Rossum" not in listAut):
    listAut.append("Rossum")

dictLiv["liv"+str(len(dictLiv)+1)]=["python",1980,listAut.index("Rossum")+1]
print(dictLiv)
ch=''


# 2)

ch=input("donner nom d'auteur\n")
if(ch in listAut):
    for i in dictLiv.values():
        if(i[2]==listAut.index(ch)+1):
            print(i[0])
else:
    print("cette auteur n'existe pas")
        

#3)
for i in dictLiv.values():
    ch=input("donner la specialité pour le livre "+i[0]+"\n")
    i.append(ch)
    
print(dictLiv)


#4)
l=[]
ch=input("donner une specialité\t")
for i in dictLiv.values():
    if(i[3]==ch and listAut[i[2]-1] not in l):
        l.append(listAut[i[2]-1])
print (l)
del l[:]


#5)
l=[]
for i in dictLiv.values():
    if(i[3] not in l):
        l.append(i[3])
print (l)
del l[:]