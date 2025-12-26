MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Test:
    def __init__(self, code, score):
        self.code = code
        self.score = score
    
    def __str__(self):
        return f'{self.code} {self.score}'

test_scores = []
for i in range(MAX_N):
    test_scores.append(Test(codenames[i], scores[i]))

test_scores.sort(key=lambda x: x.score)

print(test_scores[0])