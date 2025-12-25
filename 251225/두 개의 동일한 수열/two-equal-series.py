n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

print('Yes' if sorted(A) == sorted(B) else 'No')