print("enter two values")

num1 = int(input("Enter Num 01 : "))
num2 = int(input("Enter Num 02 : "))


def add_mul(x,y):
    added = x + y
    multiplied = x*y
    return added, multiplied


result1,result2 = add_mul(num1, num2)

print(result1)
print(result2)


# variable length argument passing ....
print("#######################################################")


def sum(*all_num):
    final_sum = 0
    for i in all_num:
        final_sum += i
    print(final_sum)


sum(2,3,4,5)


# keyword variable length argument passing ....
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")


def info(age, **data):
    print("age",age) 
    for i,j in data.items():
        print(i,j)
        

info(28, name="sachith", uni= "mora", index= 194)



