from math import isqrt

for i in range(10, 100):
    if(i >= 0 and isqrt(i)**2 == i):
        print(f" {i} négyzetszám")