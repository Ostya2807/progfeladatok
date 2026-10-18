number = int(input("Adja meg a kártyaszámát: "))
firstNumber = number // 10
secondNumber = number % 10

if(firstNumber % 2 == 0 and secondNumber % 2 == 0):
    print("Beléphet az egyes helységbe!")
elif(firstNumber % 2 == 0 and secondNumber % 2 != 0):
    print("Beléphet a kettes helységbe!")
elif(firstNumber % 2 != 0 and secondNumber % 2 == 0):
    print("Beléphet a hármas helységbe!")
elif(firstNumber % 2 != 0 and secondNumber % 2 != 0):
    print("Beléphet a négyes helységbe!")