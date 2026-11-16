import random

sziget = []
for i in range(23):
    sziget.append(random.randint(0,3)) 

#print(sziget)
szigetekString = "".join(map(str, sziget))
print(szigetekString)

#Szigetek létrehozása
csakSzigetek = szigetekString.split("0")
#print(csakSzigetek)
szigetCount=0
for i in csakSzigetek:
    if (i != ""):
        szigetCount += 1
print(f"{szigetCount} db sziget van!")

#Sziget hossza
szigetHossz = 0
for i in csakSzigetek:
    if(len(i) > szigetHossz):
        szigetHossz = len(i)
print(f"A leghosszabb sziget {szigetHossz} egysegnyi!")

#Legmagasabb pont előfordulása
legmagasabbSzint = 0
for i in csakSzigetek:
    if("3" in i):
        legmagasabbSzint += 1

print(f"{legmagasabbSzint} szigeten fordul elo!")

#Szintkülönbségek
szintkulonbseg = []
for i in csakSzigetek:
    if(i !=""):
        szintkulonbseg.append(int(max(i))-int(min(i)))
print(f"A szintkulonbsegek a szigeteken rendre{szintkulonbseg}")


#Legnagyobb tavolsag
legnagyobbTavolsag = 0
currentTavolsag = 0
for i in szigetekString:
    if(i == "0"):
        currentTavolsag += 1
        if(currentTavolsag > legnagyobbTavolsag):
            legnagyobbTavolsag = currentTavolsag
    else:
        currentTavolsag = 0
print(f"A szigetek kozotti legnagyobb tavolsag {legnagyobbTavolsag} egysegnyi!")