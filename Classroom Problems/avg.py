class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Krishiv", 101, [85, 90, 78, 92, 88])

print("Name:", s1.name)
print("Roll Number:", s1.roll)
print("Marks:", s1.marks)
print("Average:", s1.average())
