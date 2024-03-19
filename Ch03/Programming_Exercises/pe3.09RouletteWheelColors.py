
p0 = "Green"
p1 = "Red"
p2 = "Black"
num = int(input('Enter a number 0-36: '))
if num <0 or num >36:
    print(f'ERROR: You entered {num}, a number outside the range 0-36.')
elif num == 0:
    print(p0)
elif (num >= 1 and num <= 10) or (num >= 19 and num <= 29):
    if num%2 == 0:
        print(p2)
    else:
        print(p1)    
else:
    if num%2 == 0:
        print(p1)
    else:
        print(p2)    
