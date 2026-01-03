a, b, c = map(int, input().split())

# Please write your code here.

day, hour, minute  = 11, 11, 11
elapsed_time = 0

while True:
    if (a, b, c) < (day, hour, minute):
        elapsed_time = -1
        break

    if day == a and hour == b and minute == c:
        break
    
    elapsed_time += 1
    minute += 1

    if minute == 60:
        hour += 1
        minute = 0
        if hour == 24:
            day += 1
            hour = 0

print(elapsed_time)


# a, b, c = tuple(map(int, input().split()))

# diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

# if diff < 0:
#     print(-1)
# else:
#     print(diff)