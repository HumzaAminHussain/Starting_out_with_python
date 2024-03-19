weight = float(input('How much do you weigh in pounds: '))
height = float(input('How tall are you in inches: '))
bmi = weight*(703/height**2)
if bmi < 18.5:
    print('You are underweight for your height.')
elif bmi > 25:
    print('You are overweight for your height.')
else:
    print('You are the optimal weight for your height.')