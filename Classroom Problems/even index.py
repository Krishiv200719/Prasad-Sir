text = input("Enter a string: ")

print("Characters at even index positions:")
for i in range(0, len(text), 2):
    print(text[i])
