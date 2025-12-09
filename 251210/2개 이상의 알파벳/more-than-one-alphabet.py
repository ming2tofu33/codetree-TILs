A = input()

# Please write your code here.

def check_letter(s):
    letters = set(s)
    return 'Yes' if len(letters) >= 2 else 'No'

print(check_letter(A)) 
