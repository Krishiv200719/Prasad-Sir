student_marks = {
    "a": 85,
    "b": 92,
    "c": 78,
    "d": 92,
    "e": 85
}

unique_values = []

for value in student_marks.values():
    if value not in unique_values:
        unique_values.append(value)

print("Unique values:", unique_values)
print("Count of unique values:", len(unique_values))
