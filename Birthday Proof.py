import random
from collections import Counter

def random_birthday():
    month = random.randint(1, 12)
    days_in_month = {2: 28, 4: 30, 6: 30, 9: 30, 11: 30}
    day = random.randint(1, days_in_month.get(month, 31))
    year = random.randint(1990, 2015)
    return (day, month, year)

def generate_birthdays(n):
    birthdays = []
    for _ in range(n):
        birthdays.append(random_birthday())
    return birthdays

def birthday_probability(n, simulations=10_000):
    same_birthday_cases = 0 

    for _ in range(simulations):
        birthdays = generate_birthdays(n)
        only_day_month = [(d, m) for d, m, _ in birthdays]
        counts = Counter(only_day_month)

        if any(count > 1 for count in counts.values()):
            same_birthday_cases += 1

    probability = same_birthday_cases / simulations
    return probability

num_students = 10
birthdays = generate_birthdays(num_students)

print("Janamdin (day/month/year) of students:")
for i, (d, m, y) in enumerate(birthdays, start=1):
    print(f"Student {i}: {d}/{m}/{y}")

counts = Counter((d, m) for d, m, _ in birthdays)
duplicates = [f"{d}/{m}" for (d, m), c in counts.items() if c > 1]

if duplicates:
    print("\nSame janamdin (day & month) found:")
    for d in duplicates:
        print(d)
else:
    print("\nNo same janamdin found in this group.")
prob = birthday_probability(num_students)
print(f"\nProbability that at least two share a janamdin (for {num_students} students): {prob:.2%}")