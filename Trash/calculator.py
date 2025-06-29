
# x = (-b+- (| (b^2 - 4ac)))/2a
# x^2 + 5x + 6 = 0

a = 1
b = -2
c = -8

d = (b**2) - (4*a*c)
d_ = d**0.5
set1 = (-b + d_) / 2*a
set2 = (-b - d_) / 2*a

print(str(set1), 'and' , str(set2))

print('Hello')


# # quad-ver2
# print('ax^2 + bx + c')

# print()
# a = input("a = ")
# b = input("b = ")
# c = input("c = ")
# print()
# b and print(a + 'x^2 + ' + b + 'x + ' + c + ' =')

# if b and c :
#     if not(a) : a = 1
#     a, b , c = int(a), int(b), int(c)
#     d = (b**2) - (4*a*c)
#     d_ = d**0.5
#     set1 = (-b + d_) / 2*a
#     set2 = (-b - d_) / 2*a

#     print(str(set1), 'or', str(set2))
# else:
#     print('This is not a quadratic equation')