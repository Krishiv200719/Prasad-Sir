dict1 = {"A": 10, "B": 20, "C": 30, "D": 40}
dict2 = {"X": 20, "Y": 40, "Z": 50, "W": 30}

common_values = []

for v1 in dict1.values():
    for v2 in dict2.values():
        if v1 == v2 and v1 not in common_values:
            common_values.append(v1)

print("Common values:", common_values)
