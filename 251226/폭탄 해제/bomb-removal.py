unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Unlock:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
    def __str__(self):
        return f'code : {self.code} \ncolor : {self.color} \nsecond : {self.second} '

bomb1 = Unlock(unlock_code, wire_color, seconds)
print(bomb1)