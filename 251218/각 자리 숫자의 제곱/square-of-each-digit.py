N = int(input())

# Please write your code here.

def sqr(n):
    if n < 10:
        return n * n

    digit = (n % 10)
    return sqr(n // 10) + digit * digit

print(sqr(N))