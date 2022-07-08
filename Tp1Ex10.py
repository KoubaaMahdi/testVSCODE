ch=input("donner un texte\n")
ch=ch.upper()
print(ch)
j=1
o=1
for i in ch :
    if (i==' '):
        j+=1
    elif (i=='.'):
        o+=1
print ("nombre de mots = ",j,"\nnombre de phrace = ",o,)
