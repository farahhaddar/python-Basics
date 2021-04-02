for x in range(6):
    pass



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# the else stament will print after the loop is over 
for x in range(len(fruits)):
    print(x)
else:
    print("done")

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
