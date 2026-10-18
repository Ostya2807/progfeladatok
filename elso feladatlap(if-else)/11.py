a = int(input("Adja meg a hároszög első odlalának hosszát! "))
b = int(input("Adja meg a hároszög második odlalának hosszát! "))
c = int(input("Adja meg a hároszög harmadik odlalának hosszát! "))

if((a+b>c) and (b+c>a) and (c+a>b)):
    print("A háromszög megszerkeszthető!")
else:
    print("A háromszög nem szerkeszthető meg!")