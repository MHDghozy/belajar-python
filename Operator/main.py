print("Operator Perbandingan")
number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))

equal = number1 == number2
notEqual = number1 != number2
greaterThan = number1 > number2
lessThan = number1 < number2
greaterEqual = number1 >= number2
lessEqual = number1 <= number2

print(f"{number1} == {number2} : {equal}")
print(f"{number1} != {number2} : {notEqual}")
print(f"{number1} > {number2} : {greaterThan}")
print(f"{number1} < {number2} : {lessThan}")
print(f"{number1} >= {number2} : {greaterEqual}")
print(f"{number1} <= {number2} : {lessEqual}")