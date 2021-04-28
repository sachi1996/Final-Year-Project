#Break is use to skip loop
print()
print("Break :::::::::::::::::::::::::")
st = 5
  
x = int(input("How many watches you want? "))

i = 1
while i<=x:
    if i>st:
        print("Out of Stock")
        break
    print("watch") 
    i+=1
print("Bye Break")
print()

#Continue is use to continue the loop skip of if statement
print("Continue :::::::::::::::::::::")
x = range(1,10,1)
for i in x:
    if i%2==0:
        continue
    print(i)
print("Bye Continue")
print()

#Pass is use to continue the loop skip of if statement
print("Pass :::::::::::::::::::::")
x = range(1,10,1)
for i in x:
    if i%2==1:
        pass
    else:
        print(i)
print("Bye Pass")