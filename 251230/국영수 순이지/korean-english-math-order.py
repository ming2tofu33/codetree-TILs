class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def __str__(self):
        return f'{self.name} {self.kor} {self.eng} {self.math}'


n = int(input())
tests = []

for _ in range(n):
    student_info = input().split()
    name = student_info[0]
    kor = int(student_info[1])
    eng = int(student_info[2])
    math = int(student_info[3])
    tests.append(Student(name, kor, eng, math))

tests.sort(key=lambda x: (x.kor, x.eng, x.math), reverse=True)

for t in tests:
    print(t)