time, min = map(int, input().split())
wating = int(input())

all =  time * 60 + min + wating

if all - 24*60 >= 0:
    all = all - 24*60

time =  all // 60
min = all % 60
print(time, min)