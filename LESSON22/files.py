
import os
# r = read
# a = append
# w = write
# x = create

# Read - error if it doesnt exist

# f = open('LESSON22/name.txt', 'r')
f = open('LESSON22/name.txt')
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for i in f:
    print(i)

f.close()

try:
    # f = open('list.txt')
    f = open('LESSON22/name.txt')
    print(f.read())
except:
    print('File does not exit')
finally:
    f.close


# Append - creates a file if it doesn't exist

f = open('LESSON22/name.txt', 'a')
f.write('\nName')
f.close

f = open('LESSON22/name.txt')
print(f.read())
f.close


# Write (overwrite)
f = open('LESSON22/context.txt', 'w')
f.write('I deleted all of the txt')
f.close()

f = open('LESSON22/context.txt', 'r')
print(f.read())
f.close()

# Two ways to create a new file

#####################################################

# Open a file for writing, creates the file if it does not exist
f = open('LESSON22/nme.txt', 'w') 
f.close()

# Creates a specified file, but returns an error if the file exists
if not os.path.exists('LESSON22/me.txt'):
    f = open('LESSON22/me.txt', 'x')
    f.close()

########################################################

# Delete a file

# avoid err if it doesn't not exist
if os.path.exists('LESSON22/me.txt'):
    os.remove('LESSON22/me.txt')
else:
    print('The file you wish to delete does not exist')


with open('LESSON22/more_name.txt') as f:
    content = f.read()
with open('LESSON22/name.txt', 'w') as f:
    f.write(content)