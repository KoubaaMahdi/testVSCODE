t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre','Novembre', 'Décembre']
t3=[]
x=0
i=0
for i in range(0,24,2):
    t3=t3+[t2[x]]+[t1[x]]
    x+=1  
print (t3)