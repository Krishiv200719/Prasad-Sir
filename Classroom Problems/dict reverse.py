student = {
    "a": 85,
    "b": 92,
    "c": 78
}

reversed_dict = {}
for key, value in student.items():
    reversed_dict[value] = key

print(reversed_dict)
