set1 = set(input("Enter elements of first set (space separated): ").split())
set2 = set(input("Enter elements of second set (space separated): ").split())

print("Union:", set1.union(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Intersection:", set1.intersection(set2))