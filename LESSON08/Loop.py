val = 1
# while val <= 10:
#     print(val)
#     if val == 5:
#         break
#     val+=1

# while val <= 10:
#     val+=1
#     if val == 5:
#         continue
#     print(val)
# else:
#     print('value = ' + str(val))
#     print('value =', val)
#     print(f'value = {val}')


names = ['andy', 'becky', 'catty']
# for i in names:
#     print(i)

# for i in 'Mississippi':
#     print(i)

# for i in names:
#     if i == 'becky':
#         continue
#     print(i)

# for i in range(4):
#     print(i)

# for i in range(2, 4):
#     print(i)

for i in range(0, 101, 5):
    print(i)
else:
    print('Glad that\'s over!')

names = ['andy', 'becky', 'catty']
actions = ['codes', 'eats', 'sleeps']

for action in actions:
    for name in names:
        print(name + ' ' + action + '.')

# you cant add to a tuple
