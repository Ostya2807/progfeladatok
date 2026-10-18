number = int(input("Adj meg egy számot! "))
if(number < 0):
    print(f"Ez egy negatív szám! {number}")
elif(number > 0 ):
    print(f"Ez egy pozitív szám! {number}")
else:
    print(f"Ez nulla! {number}")