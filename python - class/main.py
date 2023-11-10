class Animal:
    name = "" #properties / attribute
    color = ""

    def makeSound(sound):
      print("Animal is making sound")

    def eat(self, food):
      print("Animal is eating", food)

    def sleep(self):
      print("Animal is sleeping")

cat = Animal()
cat.name = "Agus"
cat.color = "white"
cat.sleep()
cat.eat("fish")



  

