
name = 'n'
count = 1

def use1():
    color = 'blue'
    global count
    count += 1
    print(count)
    
    def greeting(name):
        nonlocal color
        color = 'ish'
        print(color)
        print(name)

    greeting('r')

use1()