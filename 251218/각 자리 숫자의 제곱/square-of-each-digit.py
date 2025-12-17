N = int(input())

# Please write your code here.

def sqr(n):
    if n < 10:
        return n ** 2
    
    return sqr(n // 10) + ((n % 10) ** 2)

print(sqr(N))