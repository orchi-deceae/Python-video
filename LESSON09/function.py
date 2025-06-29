def hello():
    print('hello')

hello()

def sum(n1=0, n2=0):
    # if type(n1)!=int or type(n2)!=int:
    if (type(n1) is not int or type(n2) is not int):
        return
    return n1 + n2

total = sum(7, 2)

print(total)

def multi_items(*args):
    print(args)
    print(type(args))

multi_items('n', 'k', 'pm')

def multi_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_name_items(first = 'n', last = 'k', time = 'pm')

# you cant edit a set
# or look for its indexes