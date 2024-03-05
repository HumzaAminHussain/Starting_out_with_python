color1 = input('Enter a color that is either red, yellow, or blue (all lowercase): ')
color2 = input('Enter a different color that is either red, yellow, or blue (all lowercase): ')
if color1 == "red" and color2 == "yellow":
    print('Orange.')
if color1 == "red" and color2 == "blue":
    print('Purple.')
if color1 == "blue" and color2 == "red":
    print('Purple.')
if color1 == "blue" and color2 == "yellow":
    print("Green.")
if color1 == "yellow" and color2 == "blue":
    print("Green.")
if color1 == "yellow" and color2 == "red":
    print("Orange.")
if color1 == "yellow" and color2 == "yellow":
    print("Yellow.")
if color1 == "red" and color2 == "red":
    print("Red.")
if color1 == "blue" and color2 == "blue":
    print("blue.")
else:
    print("ERROR: you entered somthing other than the primary colors.")