szam1 = int(input("Adj meg egy számot! "))
szam2 = int(input("Adj meg egy számot! "))
szam3 = int(input("Adj meg egy számot! "))

if szam1>szam2:
    szam1, szam2 = szam2, szam1
if szam1>szam3:
    szam1, szam3 = szam3, szam1
if szam2>szam3:
    szam2, szam3 = szam3, szam2

if(szam2 == ((szam1 + szam3) / 2)):
    print(f"Ez egy számtani sorozat: {szam1} {szam2} {szam3}")

if(szam2**2 == (szam1 * szam3)):
    print(f"Ez egy mértani sorozat: {szam1} {szam2} {szam3}")