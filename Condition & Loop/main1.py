print("Score Range Checker")
print("===================")

score = int(input("Masukkan nilai Anda: "))

if score >= 85 and score <= 100:
    print("Kamu mendapatkan A")
elif score >= 70 and score <=84:
    print("Kamu mendapatkan B")
elif score >= 60 and score <=69:
    print("Kamu mendapatkan C")
else:
    print("Kamu mendapatkan D")    

