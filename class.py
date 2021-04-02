class Person:
    # constructr 
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)  

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

# delete an object 
# del p1
# p1.name


# inhetrintce
class Student(Person):
  def __init__(self, fname, lname): 
    super().__init__(fname, lname)  #intialize the parent class value 
    self.graduationyear = 2019  # add new vars


p2= Student('farah','haddar')
print(p2.name)
print(p2.age)
print(p2.graduationyear)

