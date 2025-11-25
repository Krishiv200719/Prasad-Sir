sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("The longest word is:", longest)
