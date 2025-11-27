students_marks = {
    "a": 85,
    "b": 92,
    "c": 78,
    "d": 95,
    "e": 88
}

topper = max(students_marks, key=students_marks.get)

print("Topper:", topper, "with", students_marks[topper], "marks")
