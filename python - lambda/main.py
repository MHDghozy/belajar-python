# def sayHello(name):
#   print("Selamat Datang", name)
  
sayHello = lambda name : print("Selamat Datang", name)

sayHello("Ghozy")

# def addition(num1, num2):
#   result = num1 + num2
#   print(result)

addition = lambda num1, num2 : print(num1+num2)

addition(10,12)

# lambda tanpa argument
(lambda : print("Selamat Datang"))()

# lambda dengan argument
(lambda fruit : print("Saya suka", fruit))("Pisang")

# lambda dengan default argument
(lambda name="" : print("Selamat Datang", name))()