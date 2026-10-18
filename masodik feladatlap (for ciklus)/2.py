x = int(input("Adj meg egy egész számot! "))
y = int(input("Adj meg egy egész számot! "))

if(x > y):
    x , y = y,x

for i in range ( x + 1, y ):
    print(i)