my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list2 = []
for number in my_list:
    if number not in my_list2:
        my_list2.append(number)
print("The list with unique elements only:")
print(my_list, my_list2)