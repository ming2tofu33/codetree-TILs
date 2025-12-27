class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def __str__(self):
        return f'{self.date} {self.day} {self.weather}'

n = int(input())
weather = []

for _ in range(n):
    d, dy, w = input().split()
    weather.append(Forecast(d, dy, w))

weather.sort(key=lambda x: x.date)
rainydays = list(filter(lambda x: x.weather == 'Rain', weather))

print(rainydays[0])