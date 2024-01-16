COUNTY_TAX = 0.025
STATE_TAX = 0.05
item = float(input('Enter the price of the item: '))
instalments = int(input("how many instalments would you like: "))
print(f'The total amount of the purchase is {(1 + COUNTY_TAX + STATE_TAX)*item:.2f}')
print(f'For each instalment you have to pay {((1 + COUNTY_TAX + STATE_TAX)*item)/instalments:.2f}')