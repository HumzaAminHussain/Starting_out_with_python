number = int(input("Enter a number 1-10: "))
one = ('I')
two = ('II')
three = ('III')
five = ('V')
ten = ('X')
#print('I'*3)
#print((7%5)*"I")
if number == 1:
    print(one)
elif number == 2:
    print(two)
elif number == 3:
    print(three)
elif number == 4:
    print(f"{one}{five}")
elif number == 5:
    print(F'{five}')
elif number == 6:
    print(F'{five}{one}')
elif number == 7:
    print(F'{five}{two}')
elif number == 8:
    print(F'{five}{three}')
elif number == 9:
    print(f'{one}{ten}')
elif number == 10:
    print(f'{ten}')
else:
    print('ERROR: You entered a number outside the range 1-10.')
