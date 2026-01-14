n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

found = False
for s in range(n1 - n2 + 1):
    if a[s:s+n2] == b:
        found = True
        break

print("Yes" if found else "No")