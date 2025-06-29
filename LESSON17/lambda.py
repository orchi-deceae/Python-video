
sqr = lambda n: n * n
# def sqr(n): return n * n
print(sqr(2))

addTwo = lambda n: n + 2
# def addTwo(n): return n + 2

print(addTwo(12))

sumTotal_ = lambda a, b: a + b
# def sumTotal_(a, b): return a + b

print(sumTotal_(10, 8))


##########################################

def funcBuilder(x):
    return lambda n: n + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


##########################################

lambda n: n * n

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sqrd_n = map(lambda n: n * n, n)

print(list(sqrd_n))


############################################

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_n = filter(lambda n: n % 2 != 0, n)

print(list(odd_n))


#############################################

from functools import reduce

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers))
print(sum(numbers, 10))

lambda acc, curr: acc + curr

names = ['paradise wanda', 'crystal muu', 'rbll', 'daily dose']

char_count = (reduce(lambda acc, curr: acc + len(curr), names, 0))

# char_count = len((reduce(lambda acc, curr: acc + curr, names)))

print(char_count)