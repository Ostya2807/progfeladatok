from math import sqrt

a = int(input("Adja meg a hároszög első odlalának hosszát! "))
b = int(input("Adja meg a hároszög második odlalának hosszát! "))
c = int(input("Adja meg a hároszög harmadik odlalának hosszát! "))

if(a != 0 and b != 0 and c != 0):
    kerulet = a + b + c
    s = kerulet / 2
    terület = sqrt(s * (s-a) * (s-b) * (s-c))
    if a>b:
        a, b = b, a
    if a>c:
        a, c = c, a
    if b>c:
        b, c = c, b

    print(f"A háromszög kerülete {kerulet}")
    print(f"A háromszög területe {terület}")

    if(a**2 + b**2 == c**2):
        print("A háromszög derékszög")
    else:
        print("A háromszög nem derékszögű")
else:
    print("Egy háromszögenk nem lehet 0 hosszú odlala")