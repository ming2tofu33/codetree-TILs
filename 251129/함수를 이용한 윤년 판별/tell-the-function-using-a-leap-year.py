y = int(input())

# Please write your code here.

def is_leap_year(n):
    if n % 4 == 0 and not(n % 100 == 0 and n % 400 != 0):
        return 'true'
    else:
        return 'false'

print(is_leap_year(y))