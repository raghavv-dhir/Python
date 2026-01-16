# Given data
students = ["Aman", "Riya", "Karan", "Riya", "Aman", "Neha", "Karan", "Aman"]
subjects = ["Math", "Science", "Math", "English", "English", "Math", "Science", "Science"]
marks = [85, 90, 78, 88, 92, 60, 55, 95]

print("1) zip() and enumerate()")
for i, (n, sub, m) in enumerate(zip(students, subjects, marks), start=1):
    print(i, n, sub, m)

print("\n2) defaultdict(list)")
from collections import defaultdict

student_marks = defaultdict(list)
for name, mark in zip(students, marks):
    student_marks[name].append(mark)

print(dict(student_marks))

print("\n3) Counter")
from collections import Counter

student_count = Counter(students)
print(student_count)

print("\n4) List comprehension >=90")
high_scorers = [students[i] for i in range(len(marks)) if marks[i] >= 90]
print(high_scorers)

print("\n5) Set comprehension")
unique_subjects = {subject for subject in subjects}
print(unique_subjects)

print("\n6) Dict comprehension- avg")
average_marks = {name: sum(marks_list) / len(marks_list)
                 for name, marks_list in student_marks.items()}
print(average_marks)

print("\n7) map() + filter()- squared+pass")
passing_squared = list(map(lambda x: x*x, filter(lambda x: x >= 60, marks)))
print(passing_squared)

print("\n8) reduce()- total")
from functools import reduce

total_marks = reduce(lambda a, b: a + b, marks)
print(total_marks)

print("\n9) any() and all()")
print("Any mark below 60:", any(mark < 60 for mark in marks))
print("All marks above 40:", all(mark > 40 for mark in marks))

print("\n10) for-else")
for mark in marks:
    if mark == 100:
        print("Perfect scorer found")
        break
else:
    print("No perfect scorer")

print("\n11) break and continue")
for mark in marks:
    if mark < 60:
        continue
    if mark > 95:
        break
    print(mark)

print("\n12) Using deque")
from collections import deque

student_queue = deque(students)

# Add 2 students from right
student_queue.append("Pradeep")
student_queue.append("Nihar")

# Remove 1 from left
student_queue.popleft()

# Add 1 from left
student_queue.appendleft("Ankit")

# Remove 1 from right
student_queue.pop()

print(student_queue)

print("\n13) Nested list comprehension")
pairs = [(student, subject) for student in students for subject in subjects]
print(pairs)
