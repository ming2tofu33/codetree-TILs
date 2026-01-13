n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def is_subarray(n1, n2, a, b):
    start, idx = 0, 0
    result = False

    while True:
        if start == n1 or idx == n2:
            break

        if result and a[start + idx] != b[idx]:
            result = False
            break

        if a[start + idx] == b[idx]:
            idx += 1
            result = True
        else:
            start += 1
    
    return result

ans = 'Yes' if is_subarray(n1, n2, a, b) else 'No'

print(ans)