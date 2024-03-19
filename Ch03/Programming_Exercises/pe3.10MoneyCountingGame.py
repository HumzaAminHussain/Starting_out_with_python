#numofcoin = int(input('Enter how many coins you need to make a dollar: '))
pennies = int(input('How many pennies do you have: '))
nickles = int(input('How many nickles do you have: '))
totalAmountNickels = nickles*5
dimes = int(input('How many dimes do you have: '))
totalAmountDimes = dimes*10
quarters = int(input('How many quarters do you have: '))
totalAmountQuarters = quarters*25
totalAmount = pennies + totalAmountNickels + totalAmountDimes + totalAmountQuarters
if totalAmount == 100:
    print('Congrats you have a dollar!')
elif totalAmount <100:
    print('Sorry you have less than a dollar.')
elif totalAmount > 100:
    print('Sorry you have more than a dollar.')
