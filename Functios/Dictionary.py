data = {1: "sachith", 3: "samith", 4: "sandun"}

print(data)
print(data.get(1, 'Not Found'))
print(data.get(2, 'Not Found'))

print()
print("combine two lists")

keys = ['Sachi', 'Sami', 'Sandun']
Values = ['Java', 'Python', 'C#']
dictionary = dict(zip(keys, Values))
print(dictionary)


print()
print("Add New Key:Value to dictionary")

dictionary['Sampath'] = "C"
print(dictionary)


print()
print("Delete from dictionary")

del dictionary['Sampath']
print(dictionary)