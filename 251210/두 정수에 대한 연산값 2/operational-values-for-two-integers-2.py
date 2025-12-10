a, b = map(int, input().split())

# Please write your code here.

def calculate(a, b):
    a, b = min(a, b) + 10, max(a, b) * 2
    return a, b

a, b = calculate(a, b)
print(a, b)