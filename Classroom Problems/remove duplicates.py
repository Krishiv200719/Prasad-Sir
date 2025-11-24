numbers = []

for i in range(10):
    num = int(input(f"Enter number: "))
    numbers.append(num)

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
