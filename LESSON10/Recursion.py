
def add_one(n):
    if n>=9:
        return n + 1
    total = n + 1
    print(total)
    return add_one(total)

new_total = add_one(0)
print(new_total)

def use1(n=0):
    while True:
        if n==9:break
        n+=1
        print(n)
use1()