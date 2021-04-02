# declare a function by def word
def my_function():
  print("Hello from a function")


# you need to call the fn by name to excute 
# my_function()


# if a fn have parameters it should becalled  and passed the exact nb of params
# the params in  a fn are defined by name only 
def my_function(name):
  print("Hello from "+name+" "+"function")

# my_function("farah")

# if the number of arguments is unknown, add a * before the parameter name:
# it will sent them AS A TUPLE 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")