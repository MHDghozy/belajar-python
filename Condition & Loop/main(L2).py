print("Tabel Perkalian")
print("===============")

number = int(input("Mau perkalian berapa? "))
loop = int(input("Mau berapa banyak? "))

for x in range(1,loop+1):
    result = x * number
    print(f"{x} x {number} = {result}")


