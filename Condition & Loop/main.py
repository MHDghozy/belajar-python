print("Cek Ganjil Genap")
print("================")

number = int(input("Masukkan angka: "))
mod = number % 2

if mod == 0:
    print(f"{number} adalah angka genap")
else:
    print(f"{number} adalah angka ganjil")
