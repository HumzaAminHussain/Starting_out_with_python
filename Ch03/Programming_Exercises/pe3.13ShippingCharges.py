weight = float(input('How much does the package weigh in pounds: '))
if weight <= 2:
    print(f'To ship this item you need ${1.50*weight} .')
elif weight >= 3 and weight <= 6:
    print(f'To ship this item you need ${3.00*weight} .')
elif weight >= 7 and weight <= 10:
    print(f'To ship this item you need ${4.00*weight} .')
elif weight >= 11:
    print(f'To ship this item you need ${4.75*weight} .')