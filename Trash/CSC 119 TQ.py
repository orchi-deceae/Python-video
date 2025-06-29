import time

def use1(txt):
    for i in txt:
        print(i , flush=True, end='')
        time.sleep(0.005)

use1('''
Twinkle, twinkle, little star,
    How I wonder what you are! 
        Up above the world so high, 
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are
''')

# pi r^2
import math

pi = math.pi
r = float(input('r = '))

area = pi * r**2
print(area)

first_name = input('first name: ') + ' '
last_name = input('last name: ')  + ' '

name = []
name += first_name + last_name
name.reverse()

new_name = ''
for i in name: 
    new_name += i + ' '

print(new_name)

# print(time.localtime(1000))

base = float(input('base = '))
height = float(input('height = '))

area = 0.5 * base * height
print(area)