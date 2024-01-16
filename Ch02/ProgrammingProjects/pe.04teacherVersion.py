first_item=float(input('Enter the first items price: '))
second_item=float(input('Enter the second items price: '))
third_item=float(input('Enter the third items price: '))
fourth_item=float(input('Enter the fourth items price: '))
fifth_item=float(input('Enter the fifth items price: '))
sub_total = first_item+second_item+third_item+fourth_item+fifth_item
print(f'Your subtotal is {sub_total:,.2f}')
print(f'Your sales tax is {sub_total*0.07:,.2f}')
print(f'Your total is {sub_total*1.07:,.2f}')
