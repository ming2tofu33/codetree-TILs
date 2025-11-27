n = int(input())

# Please write your code here.

def special_num(num):
    return 'Yes' if num % 2 == 0 and (num // 10 + num % 10) % 5 == 0 else 'No'

print(special_num(n))