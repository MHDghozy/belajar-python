print("My To Do List")
print("=============")

active = True

while active:
  todo = input("Apa yang ingin Anda lakukan? ")
  
  file = open ("todolist.txt", "a")
  file.write(todo+"\n")
  file.close()
  
  file = open("todolist.txt", "r")
  print(file.read())
  
  active = input("ingin lanjut? y/n")




