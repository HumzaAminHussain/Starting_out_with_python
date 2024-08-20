prob1 = input('Is anyone in your party a vegetarian?(Enter all lowercase): ')
prob2 = input('Is anyone in your party a vegan?(Enter all lowercase): ')
prob3 = input('Is anyone in your party gluten-free?(Enter all lowercase): ')
if prob1 == "no" and prob2 == "no" and prob3 == "no":
    print("Here are your restaurant choices:")
    print('Joe’s Gourmet Burgers')
    print("Main Street Pizza Company")
    print('Corner Café')
    print('Mama’s Fine Italian')
    print("The Chef’s Kitchen")
elif prob1 == "no" and prob2 == "yes" and prob3 == 'yes':
    print("Here are your restaurant choices:")
    print('Corner Café')
    print("The Chef’s Kitchen")
elif prob1 == 'no' and prob2 == "yes" and prob3 == 'no':
    print("Here are your restaurant choices:")
    print('Corner Café')
    print("The Chef’s Kitchen")
elif prob1 == 'no' and prob2 == "no" and prob3 == 'yes':
    print("Here are your restaurant choices:")
    print("Main Street Pizza Company")
    print('Corner Café')
    print("The Chef’s Kitchen")
elif prob1 == 'yes' and prob2 == 'yes' and prob3 == "yes":
    print("Here are your restaurant choices:")
    print('Corner Café')
    print("The Chef’s Kitchen")
    
