time, min = map(int, input().split())


if min - 45 < 0:
    min = 60 + (min - 45)
    time = time - 1
    if time < 0:
        time = 23
else:
    min = min - 45

print(time, min)       
