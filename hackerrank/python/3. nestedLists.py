if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second_lowest = sorted(list(set(x[1] for x in students)))[1]
    students = sorted(students)
    for student in students:
        if student[1] == second_lowest:
            print(student[0])
