interval = list(map(int, input('Enter two numbers as interval: ').split()))
count = 0
for i in range(interval[0]+1, interval[1]):
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end = ' ')
