from collections import namedtuple

total = 0
noStudents, header = int(input()), input().split()
Student = namedtuple('Student', header)
for i in range(noStudents):
    f1, f2, f3, f4 = input().split()
    s = Student(f1, f2, f3, f4)
    total += int(s.MARKS)

print(f"{total/noStudents:.2f}")
