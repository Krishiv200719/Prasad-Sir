items = []

for i in range(10):
    value = input(f"Enter item: ")
    items.append(value)

count_dict = {}

for i in items:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print("item frequencies:")
for i, count in count_dict.items():
    print(i, ":", count)
