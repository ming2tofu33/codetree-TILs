arr = list(map(int, input().split()))
l = []

for i in arr:
    if i >= 250:
        break
    else:
        l.append(i)

print(sum(l), round(sum(l)/len(l), 1))