class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'
    
people = []
n = int(input())

for _ in range(n):
    n, h, w = input().split()
    h, w = int(h), int(w)
    people.append(Person(n, h, w))

people.sort(key=lambda x: x.height)

for p in people:
    print(p)