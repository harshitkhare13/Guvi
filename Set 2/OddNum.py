interval = list(map(int, input('Enter two numbers as interval: ').split()))
for i in range(interval[0]+1, interval[1]):
    if i % 2 == 1:
        print(i, end = ' ')
        
               
