# String data type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first)==str)
# print(isinstance(first, str))

# # constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."

print(statement)

# Multi line
multiline = '''
hi, 
it's me, 
Austin!
            Today we are going to talk about 
Coding

'''
print(multiline)

# Escaping special characters
sentence = 'i\'m back at work! \tHey!\n\nWhere\'s this at\\location?'

print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("Austin", "Dave"))
print(multiline)

print(len(multiline))
multiline += "                                                "
multiline = "                         " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffin".ljust(16, '.') + '$1'.rjust(4))
print("Muffin".ljust(16, '.') + '$1'.rjust(4))
print("Cheesecake".ljust(16, '.') + '$4'.rjust(4))

print('')

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some method return bolean data
print(first.startswith('D'))
print(first.endswith('Z'))

# bolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_val = 1 + 2j
print(type(comp_val))
print(type(comp_val.real))
print(type(comp_val.imag))

# built in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a numer
zipcode = '10001'
zip_val = int(zipcode)
print(type(zip_val))

# Error if you atttempt to cast incorrect data
# zip_val = int('new york')

a = False
b =  1 if a else 2
print(b)

import time
x = 'I ain\'t writing all that'
for c in x:
    print(c, end='', flush=True)
    time.sleep(0.02)