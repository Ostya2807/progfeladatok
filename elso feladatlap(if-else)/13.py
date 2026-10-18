from math import sqrt

print("Adj meg három számot a másodfokú egyenlet megoldásához.")
a = int(input("Adja meg az első számot "))
b = int(input("Adja meg a második számot "))
c = int(input("Adja meg a harmadik számot "))
x1 = 0
x2 = 0

if(a != 0):
    D = b**2 - (4*a*c)

    if(D>0):
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        print(f"A megoldás x1 = {x1}")
        print(f"A megoldás x2 = {x2}")
    elif(D==0):
        x1 = (-b + sqrt(D))/2*a
        print(f"A megoldás x = {x1}")
    else:
        print("A valós számok halmazán az egyenletnek nincs megoldása.")
else:
    print("a értéke nem lehet nulla!")