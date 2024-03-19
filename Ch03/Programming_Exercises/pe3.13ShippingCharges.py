Weight = float(input('How much does the package weigh in pounds: '))
if Weight <= 2:
    print('The shipping charge is $1.50 .')
elif Weight >= 3 and Weight <= 5:
    print('The shipping charge is $3.00 .')
elif Weight >= 7 and Weight <= 10:
    print('The shipping charge is $4.00 .')
elif Weight >= 11:
    print('The shipping charge is $4.75 .')