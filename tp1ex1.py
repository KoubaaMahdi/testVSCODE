from math import sqrt
a= int(input("donner a\n"))
b= int(input("donner b\n"))
c= int(input("donner c\n"))
if a==0:
    if b==0:
        if c==0:
            print("Tout l'ensemble")
        else:
            print("Impossible")
    else :
        print("la sol est", -c/b)
else :
    d=b**2-4*a*c
    if d==0:
        print("la sol est", -b/(2*a))
    elif d>0:
        x1=(-b-sqrt(d))/(2*a)
        x2=(-b+sqrt(d))/(2*a)
        print("les sols sont",x1,"et",x2)
    else :
        z1=(-b-1j*sqrt(-d))/(2*a)
        z2=(-b+1j*sqrt(-d))/(2*a)
        print("les sols complexe sont",z1,"et",z2)
