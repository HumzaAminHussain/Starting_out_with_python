mass = float(input('Enter the mass of the object: '))
weight = mass*9.8
print(f'{weight}')
if weight > 500:
    print('This item is to heavy.')
elif weight < 100:
    print('This item is to light.')