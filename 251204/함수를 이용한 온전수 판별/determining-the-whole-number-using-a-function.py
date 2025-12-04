a, b = map(int, input().split())

# Please write your code here.

def condition1(n):
    if n % 2 == 0:
        return False
    return True

def condition2(n):
    if str(n)[-1] == '5':
        return False
    return True

def condition3(n):
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

cnt = 0

for i in range(a, b + 1):
    if condition1(i) and condition2(i) and condition3(i):
        cnt += 1

print(cnt)