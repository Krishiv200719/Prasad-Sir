paragraph = """Python is a great programming language.
Python is easy to learn and Python is powerful."""

words = paragraph.lower().replace(".", "").split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
