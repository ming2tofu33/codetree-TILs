N = int(input())

# Please write your code here.

def f(n):
    if n == 1:
        return 0
        
    if n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f(n // 3) + 1

print(f(N))

# cnt = 0

# def f(n):
#     global cnt
#     if n == 1:
#         return cnt
#     if n % 2:
#         cnt += 1
#         return f(n // 3)
#     else:
#         cnt += 1
#         return f(n // 2)

# print(f(N))