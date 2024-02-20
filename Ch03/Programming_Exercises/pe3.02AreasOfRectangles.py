rec1with = float(input('Enter the width of rectangle 1: '))
rec1length = float(input('Enter the length of rectangle 1: '))
rec2with = float(input('Enter the width of rectangle 2: '))
rec2length = float(input('Enter the length of rectangle 2: '))
rec1 = rec1with*rec1length
rec2 = rec2length*rec1with
if rec1 > rec2:
    print('Rectangle 1\'s area is greater than rectangle 2\'s area')
elif rec2 > rec1:
    print('Rectangle 2\'s area is greater than rectangle 1\'s area')
else:
    print('The areas of both rectangles are the same.')