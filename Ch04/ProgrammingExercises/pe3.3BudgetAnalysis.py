budget = float(input('Enter your budget for the month: '))
keep_going = "yes"
total = 0
while keep_going == 'yes': 
    Expense = float(input('How much was the thing that you bought this month: '))
    total += Expense
    keep_going = input('Did you buy anything else this month(Enter yes or no): ')
if total>budget:
    print(f'You went ${total-budget:,.2f} over your budget.')
elif total<budget:
    print(f'You went ${budget-total:,.2f} under your budget.')
else:
    print(f'You did not exeed the budget of ${budget} nor did you spend less than it.')
