n, m = map(int, input().split())

# Please write your code here.
def get_gcd(x, y):
    nd = set()
    md = set()

    for i in range(1, n +1):
        if n % i == 0:
            nd.add(i)

    for j in range(1, m +1):
        if m % j == 0:
            md.add(j)

    gcd = max(nd & md)

    print(int(n * m / gcd))

get_gcd(n, m)