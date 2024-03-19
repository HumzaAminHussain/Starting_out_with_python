package = float(input('How many packages did you purchase: '))
totalpackage = package*99
if package >= 10 and package <= 19:
    discount = 10
    print(f'The discount is {discount}%.')
    print(f'The total is {(totalpackage-(totalpackage*.1)):.2f}.')
elif package >= 20 and package <= 49:
    discount = 20
    print(f'The discount is {discount}%.')
    print(f'The total is {(totalpackage-(totalpackage*.2)):.2f}.')
elif package >= 50 and package <= 99:
    discount = 30
    print(f'The discount is {discount}%.')
    print(f'The total is {(totalpackage-(totalpackage*.3)):.2f}.')
elif package >= 100:
    discount = 40
    print(f'The discount is {discount}%.')
    print(f'The total is {(totalpackage-(totalpackage*.4)):.2f}.')
else:
    print('There is no discount.')
    print(f'the total is {totalpackage:.2f}.')