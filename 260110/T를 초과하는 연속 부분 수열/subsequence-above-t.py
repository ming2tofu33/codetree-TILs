n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_cnt = 1

for i in range(n):
    if i >= 1 and arr[i] > arr[i - 1] and arr[i] > t:
        cnt += 1
        max_cnt = max(cnt, max_cnt)
    else:
	    cnt = 0

print(max_cnt)