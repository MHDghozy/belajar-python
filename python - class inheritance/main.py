class person:
  name = ""
  
  def __init__(self, name):
      self.name = name

  def getinfo(self):
      print("This person's name", self.name)

class student(person):

  nis = ""
  
  def __init__(self, name, nis):
    super().__init__(name)
    self.nis = nis

  def getinfo(self):
    print("This student's name is", self.name)

  def study(self, subject):
    print("This student is studying", subject)

class Doctor(person):
  reg_number = ""

  def __init__(self, name, reg_number):
    self.Doctor = name
  
  def getinfo(self):
   print("This doctor's name is", self.Doctor)

  def diagnose(self, patient):
    print("This doctor is diagnosing", self.patient)

  def treat(self, patient):
    print("This doctor is treating", self.patient)

doctor1 = Doctor("Dr. Ghozy", "123")
patient1.getinfo()
patient1.diagnose()

student1 = student("Ahmad", "123")
student1.getinfo()
student1.study("Math")

person1 = person("Maman")
person1.getinfo()

student1 = student("Agus", "123")
student1.getinfo()

