items = [10,3,4,6,7,9,8,2,3,1,4,5,6,7,8,9,10]

count_dict = {}

for i in items:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print("item frequencies:")
for i, count in count_dict.items():
    print(i, ":", count)
