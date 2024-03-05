color1 = input('Enter a color that is either red, yellow, or blue (all lowercase): ')
color2 = input('Enter a different color that is either red, yellow, or blue (all lowercase): ')
if color1 == "red" and color2 == "yellow":
    print('Orange.')
elif color1 == "red" and color2 == "blue":
    print('Purple.')
elif color1 == "blue" and color2 == "red":
    print('Purple.')
elif color1 == "blue" and color2 == "yellow":
    print("Green.")
elif color1 == "yellow" and color2 == "blue":
    print("Green.")
elif color1 == "yellow" and color2 == "red":
    print("Orange.")
elif color1 == "yellow" and color2 == "yellow":
    print("Yellow.")
elif color1 == "red" and color2 == "red":
    print("Red.")
elif color1 == "blue" and color2 == "blue":
    print("Blue.")
else:
    print("ERROR: you entered somthing other than the primary colors.")