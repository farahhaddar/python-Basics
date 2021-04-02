# string
# you can assign a multiple line string to a variable ny using """ or '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

# to print a specific  char 
# print(a[1])

# loop through and print each variable
# for x in a:
    # print(x)

# to get the length
# print(len(a))

# to check if a string exists in the  main string => it return a boolen true/false
txt = "The best things in life are free!"
# print("free" in txt) 

# if you want to check if its not in the string use the not statment 
txt = "The best things in life are free!"
# print("free" not  in txt) 

# slicing 

# Get the characters from position 2 to position 5 (not included the 5th postion  only 2 3 4):

b = "Hello,World!"
# print(b[2:5])

# Get the characters from the start to position 5 (not included the 5th postion only from 0 to 4):
# print(b[:5])

# Get the characters from position 2, and all the way to the end:
# print(b[2:])

# Use negative indexes to start the slice from the end of the string:
# -5 will go from the start till the  end so hello is 5 chars it will skip them to world!
# world! has -2 so the answer will be : orld
# print(b[-5:-2])


# string modification:
# .upper() upercase
# .lower() lowecase
# strip() method removes any whitespace from the beginning or the end
# The replace(a,b) method replaces the first  string with second string
# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
# print(a.split(","))
# it returns ['Hello', ' World!']

# you cannot concat a string with a number it will give a error 
a='farah'
b='haddar'
# print(a+b) will print them with no space
# print(a+" "+b)  will print them with space

# to combine strings and numbers we use the format() method 
# to use it:
# the text string should have a placeholder for the numric value by : {}
# to print we do txt.format(number)
age = 36
txt = "My name is John, and I am {}"
# print(txt.format(age))

# if we pass a multiple values in the format function we can use indexes in the place holder to ensure the correct placement 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


# escape char \"\" to use actual quates in the text 
txt = "We are the so-called \"Vikings\" from the north."
# print(txt)



# sort  a function by comaring lower case if without the key it will list the upper letter fisrt 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# tuple is a datatype that hold multiple values
# the values are unchangable and same order the order connt change
# it allow duplicate values
thistuple = ("apple",) #tuple one item 
# print(type(thistuple))

#NOT a tuple
thistuple = ("apple")#string 
# print(type(thistuple))

# Convert the tuple into a list to be able to change it,add items  by append ,join

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)

# unpack and Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



# key value dectinary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
# 


