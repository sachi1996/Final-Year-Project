from array import *

vals = array('i', [4, 7, -8, 2])

print(vals.buffer_info())
print(vals.typecode)
print(len(vals))
print("::::::::::::::::::::::::::::::")


for val in vals:
    print(val)


print("::::::::::::::::::::::::::::::")

chars = array('u', ['a', 'b', 'c', 'd'])

for char in chars:
    print(char)

print("##############################")

copied = array(vals.typecode, (a for a in vals))

for x in copied:
    print(x)




userVal = int(input("Enter a value to check "))

print(copied.index(userVal)) #function to check index of searching value...

# manually searching values...
k = 0
for checkNum in copied:
    if checkNum == userVal:
        print(k)
    else:
        k = k+1


