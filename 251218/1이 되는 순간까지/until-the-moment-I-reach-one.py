N = int(input())

# Please write your code here.

cnt = 0

def f(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2:
        cnt += 1
        return f(n // 3)
    else:
        cnt += 1
        return f(n // 2)

print(f(N))