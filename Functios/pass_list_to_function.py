
lst = [12, 4, 9]

print(lst)

def count(list_of_nums):
    even = 0
    odd = 0
    for i in list_of_nums:
        if (i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

even_num, odd_num = count(lst)

print("even",even_num)
print("odd",odd_num)


