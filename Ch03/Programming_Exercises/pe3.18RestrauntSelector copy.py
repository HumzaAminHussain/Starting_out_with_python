prob1 = input('Is anyone in your party a vegetarian?(Enter all lowercase): ')
prob2 = input('Is anyone in your party a vegan?(Enter all lowercase): ')
prob3 = input('Is anyone in your party gluten-free?(Enter all lowercase): ')
"""
 joe =                      Vegetarian: No,  Vegan: No,  Gluten-Free: N0
 Main Street Pizza Company— Vegetarian: Yes, Vegan: No,  Gluten-Free: Yes
 Corner Café—               Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
 Mama’s Fine Italian—       Vegetarian: Yes, Vegan: No,  Gluten-Free: No
 The Chef’s Kitchen—        Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
"""
if prob1 == "yes":
    print("Here are your restaurant choices:")
    if prob2 == "yes":
        if prob3 == "yes":
            print("Here are your restaurant choices:")
    else:
        if prob3 =="yes":
            print("Here are your restaurant choices:")
            print("Main Street Pizza Company")
else:
    if prob2 == "yes":
        if prob3 == "yes":
            print("Here are your restaurant choices:")
    else:
        if prob3 =="yes":
            print("Here are your restaurant choices:")
            print("Main Street Pizza Company")
print('Corner Café')
print("The Chef’s Kitchen")   