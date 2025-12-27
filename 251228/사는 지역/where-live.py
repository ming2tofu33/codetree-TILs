class Info:
    def __init__(self, name, street_num, region):
        self.name = name
        self.street_num = street_num
        self.region = region
    
    def __str__(self):
        return f'name {self.name} \naddr {self.street_num} \ncity {self.region}'

n = int(input())
info = []

for _ in range(n):
    name, street_num, region = input().split()
    info.append(Info(name, street_num, region))

info.sort(key=lambda x: x.name)

print(info[-1])