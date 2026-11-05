students = [
    ("Адель", 18, 4.5),
    ("Сергей", 67, 3.5),
    ("Айгиз", 23, 5.0),
]

# Самый старший
oldest = max(students, key = lambda student: student[1])
print(f"Самый старший студент: {oldest[0]}, ему {oldest[1]} лет.")

# Самый высокий балл
highest = max(students, key = lambda student: student[2])
print(f"Самый умный судент: {highest[0]}, у него {highest[2]} баллов.")

# Средний возраст
avg_age = sum(s[1] for s in students) / len(students)
print(f"Средний возраст: {avg_age:.2f}")
