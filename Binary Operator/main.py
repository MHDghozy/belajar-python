print("Binary Operator")

number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))

and_operator = number1 & number2
or_operator = number1 | number2
xor_operator = number1 ^ number2
not_operator1 = ~number1
not_operator2 = ~number2

print(f"{number1} & {number2} = {and_operator}")
print(f"{number1} | {number2} = {or_operator}")
print(f"{number1} ^ {number2} = {xor_operator}")
print(f"~{number1} = {not_operator1}")
print(f"~{number2} = {not_operator2}")

