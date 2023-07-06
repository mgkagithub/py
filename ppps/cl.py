class Person:
  def __init__(self, name, age,gender):
    self.name = name
    self.age = age+2
    self.gender = gender
  def __str__(self):
    return f"{self.name} \n-> {self.age}\n-> {self.gender}"

p1 = Person("ash", 12,'t327')
p2 = Person("jois", 19,'m')
print(p1)
print(p2)