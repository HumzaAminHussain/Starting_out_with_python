Books = int(input('How many books have you bought this month: '))

if Books == 0:
    print(f"You earned {Books} points this month.")
elif Books == 2:
    print('You earned 5 points this month.')
elif Books == 4:
    print('You earned 15 points this month.')
elif Books == 6:
    print(f'You earned {Books*5} points this month.')
elif Books >= 8:
    print('You earned 60 points this month.')