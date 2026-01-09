n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cnt, max_cnt, cur_num = 0, 0, 0

for i in range(n):
    cur_num = i
    if i == 0 or arr[i] != arr[i - 1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        if cur_num != i:
            cnt = 0

print(max_cnt)