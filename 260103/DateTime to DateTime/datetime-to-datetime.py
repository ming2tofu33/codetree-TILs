a, b, c = map(int, input().split())

# Please write your code here.

d, h, m  = 11, 11, 11
    elapsed_days += 1
    day += 1

    if day > months[month]:
        month += 1
        day = 1

print(elapsed_days + 1)

while True:
    if d == a and h == b and m == c: