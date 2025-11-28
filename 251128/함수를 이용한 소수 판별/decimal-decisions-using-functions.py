a, b = map(int, input().split())

# Please write your code here.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

add = 0
for j in range(a, b + 1):
    if is_prime(j):
        add += j

print(add)