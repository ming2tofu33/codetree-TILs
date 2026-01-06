n = int(input())

OFFSET = 100
MAX_R = 200

line = [0] * (MAX_R + 1)
loc = OFFSET + 1

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(loc, loc-x, -1):
            line[i] += 1
    else:
        for i in range(loc-x, loc):
            line[i] += 1

f = list(filter(lambda a: a >= 2, line))
print(len(f))