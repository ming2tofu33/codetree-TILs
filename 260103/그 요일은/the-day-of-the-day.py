m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
date = [m1, d1]
total_days = 0

while True:
    if date[0] == m2 and date[1] == d2:
        break

    date[1] += 1
    total_days += 1

    if date[1] > months[date[0]]:
        date[0] += 1
        date[1] = 1

cnt = total_days // 7 + (day_of_week[A] <= total_days % 7)

print(cnt)