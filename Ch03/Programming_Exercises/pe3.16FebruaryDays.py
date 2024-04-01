year = int(input('What is the year: '))
if year%100 == 0:
    if year % 400 == 0 :
        print(f'In {year}, February has 29 days.')
    elif year % 400 > 0 or year % 400:
        print(f'In {year}, February has 28 days.') 
elif year%100<0 or year%100>0:
    if year%4 == 0:
       print(f'In {year}, February has 29 days.')   
    elif year%4<0 or year%4>0:
        print(f'In {year}, February has 28 days.')   
# talk to michael about the problem