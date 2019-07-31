# beg30.py
hour1,minute1 = map(int,input().split())
hour2,minute2 = map(int,input().split())
print(tsp(hour1-hour2),tsp(minute1-minute2))
