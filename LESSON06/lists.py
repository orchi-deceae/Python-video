users = ['andy', 'braddy', 'catty']

data = ['me', 420, True]

empty = []

print('andy' in users)

print(users[0])
print(users[-2])

print(users.index('catty'))

print(users[0:2])
print(users[0:])
print(users[-3:-1])

print(len(data))

users.append('danny')
print(users)

users += ['saya']
print(users)

users.extend(['freddy', 'garry'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'gooey')
print(users)

users[2:2] = ['pop' , 'up']
print(users)

users[1:3] = ['cool', 'japan']
print(users)

users.remove('up')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['Curry']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

numbers = [4, 42, 38, 1, 5]
numbers.reverse()
print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

print(sorted(numbers,reverse=True))
print(numbers)

numberscopy = numbers.copy()
mynumbers = list(numbers)
mycopy = numbers[:]

print(numberscopy)
print(mynumbers)
mycopy.sort()
print(mycopy)
print(numbers)

print(type(numbers))

mylist = list([1, 'nail', True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mylist)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
# newlist.append('dave')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))


# users.append('')
# users.insert([''])
# users.extend(0, '')