A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

score = float(input('Enter your test score: '))

if score >= A_SCORE:
    print('Your grade is A')
else:
    if score >= C_SCORE:
        print('Your grade is C.')
    else:
        if score >= D_SCORE:
            print('Your grade is D.')
        else:
            print('Your grade is F.') 