year = int(input("Adjon meg egy évszámot. "))
if(year % 400 == 0):
    print(f"Ez egy szökőév! {year}")
elif(year % 100 == 0):
    print(f"Ez nem szökőév! {year}")
elif(year % 4 == 0):
    print(f"Ez egy szökőév! {year}")
else:
    print(f"Ez nem szökőév! {year}")

print(f"{year % 100} {year % 4} {year % 400}")