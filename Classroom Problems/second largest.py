numbers = []

for i in range(10):
    num = float(input(f"Enter number: "))
    numbers.append(num)

numbers.sort()

print("Second largest number is:", numbers[-2])
