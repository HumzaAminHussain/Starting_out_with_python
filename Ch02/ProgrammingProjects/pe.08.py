TIP = 0.18
TAX = 0.07
meal = float(input('How much was your meal: '))
print(f'The amount of an 18 percent tip is {meal*TIP:.2f}')
print(f'The sales tax is {meal*TAX:.2f}')
print(f'The total is {(1+TAX+TIP)*meal:,.2f}')