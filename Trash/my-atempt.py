import time
def findD(d):
    if d<0:
        return complex(0, (-d)**0.5)
    if not(d):
        return 0
    d = d**0.5
    return d
    

# x = -b +- | b^2 - 4ac / 2a
def values(a, b, c):
    d = b**2 - 4*a*c
    d_ = findD(d)
    set1 = -b + d_
    set2 = -b - d_
    x1 = set1 / 2*a
    x2 = set2 / 2*a
    return d, d_, set1, set2, x1, x2

def typewriter(text):
    for txt in text:
        print(txt, end='', flush=True)
        time.sleep(0.03)

    print()

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print()
typewriter('-b ± √b² - 4ac')
typewriter('--------------')
typewriter('      2*a')

d, d_, set1, set2, x1, x2 = values(a, b, c)
print(d, d_, set1, set2, x1, x2)

set = [set1, set2]
n = 2
for sit in set:
    n = n-1
    i = '+' if n else '-'
    x = x1 if n else x2
    print()
    typewriter(f'{-b} {i} √{b}² - 4*{a}*{c}')
    typewriter('------------------')
    typewriter(f'      2*{a}')
    typewriter(f'{-b} {i} √{b**2} + {-4*a*c}')
    typewriter('-------------')
    typewriter(f'     2*{a}')
    typewriter(f'    {-b} {i} {d_}')
    typewriter('--------------')
    typewriter(f'       {2*a}')
    typewriter(f'    {sit}')
    typewriter('-------------')
    typewriter(f'      {2*a}')
    print()
    typewriter(f'x = {x}')
