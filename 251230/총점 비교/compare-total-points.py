class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    
    def __str__(self):
        return f'{self.name} {self.score1} {self.score2} {self.score3}'

n = int(input())

students = []

for _ in range(n):
    name, score1, score2, score3 = input().split()
    students.append(Student(name, int(score1), int(score2), int(score3)))

students.sort(key=lambda x: x.score1 + x.score2 + x.score3)

for student in students:
    print(student)