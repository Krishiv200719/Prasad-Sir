numbers = [10,3,4,6,7,9,8,2,3,1,4,5,6,7,8,9,10]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
