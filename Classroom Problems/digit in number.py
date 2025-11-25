num = int(input("Enter a number: "))

count = 0
temp = num

if num == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
