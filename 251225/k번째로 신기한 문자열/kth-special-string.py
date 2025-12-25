n, k, t = input().split()
n, k = int(n), int(k)
words = []

for _ in range(n):
    word = input()
    if word.startswith(t):
        words.append(word)

words.sort()

print(words[k-1])