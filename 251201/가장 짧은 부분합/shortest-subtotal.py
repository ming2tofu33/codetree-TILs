n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')
min_len = INF

i = 0
j = 0
curr_sum = 0 

while True:
    if curr_sum >= s:
        min_len = min(min_len, j - i)
        curr_sum -= arr[i]
        i += 1 
    elif j < n:
        curr_sum += arr[j]
        j += 1
    else:
        break

print(0 if min_len == INF else min_len)