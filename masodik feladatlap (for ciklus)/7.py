x = int(input("Adj meg egy egész számot! "))
y = int(input("Adj meg egy egész számot! "))

for i in range(x, y+1):
    if(i % 6 == 0):
        print(i)