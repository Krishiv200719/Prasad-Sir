numbers = (10, 20, 30, 40, 50)

value = int(input("Enter a value to search: "))

if value in numbers:
    print("Index of value:", numbers.index(value))
else:
    print("Value not found in the tuple.")
