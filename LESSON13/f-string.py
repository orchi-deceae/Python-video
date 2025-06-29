person = 'Ben'
coins = 3

print('\n' + person + ' has ' + str(coins) + ' coins left.')

txt = '\n%s has %s coins left.' %(person, coins)
print(txt)

txt = '\n{} has {} coins left.'.format(person, coins)
print(txt)

txt = '\n{1} has {0} coins left.'.format(coins, person)
print(txt)

txt = '\n{person} has {coins} coins left.'.format(coins=coins, person=person)
print(txt)

player = { 
    'person': 'Ben', 'coins': 3
}
txt = '\n{person} has {coins} coins left.'.format(**player)
print(txt)

############################
# f-strings! This is the way.

print(f'\n{person} has {coins} coins left.')

print(f'\n{person} has {2 * 5} coins left.')

print(f'\n{person.lower()} has {coins} coins left.')

print(f'\n{player["person"]} has {coins} coins left.')

#################################
# You can pass formatting options.

n = 10
print(f'\n2.25 times {n} is {2.25 * n:.2f}\n')

for i in range(1, 11):
    print(f'2.25 times {i} is {2.25 * i:.2f}')

for i in range(1, 11):
    print(f'{i} divided by 4.52 is {i / 4.52:.2%}')
