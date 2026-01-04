binary = list(map(int, list(input())))

num = 0

for i in binary:
    num = num * 2 + i

num *= 17

digits = []

while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit, end='')