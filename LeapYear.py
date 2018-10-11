def isleap(year):
    leap = False
    if(year%4==0):
      if(year%100==0 and year%400==0):
        leap = True
      elif(year%100!=0):
        leap = True
      else:
        leap = False
    return leap

year = int(input('Enter a year: '))
if isleap(year):
    print('yes')
else:
    print('no')
