#Task4 - Control flow
grades = [85, 78, 92, 45, 33, 67, 88, 41]

print("Grade Categories:")
for grade in grades:
    if grade > 80:
        print(f"Score: {grade} - Grade: A")
    elif 60 <= grade <= 80:
        print(f"Score: {grade} - Grade: B")
    elif 40 <= grade < 60:
        print(f"Score: {grade} - Grade: C")
    else:
        print(f"Score: {grade} - Grade: F")

boosted_grades = list(map(lambda x: x * 1.05, grades))
print("Boosted Grades:", boosted_grades)

grades_above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("Boosted Grades Above 90:", grades_above_90)