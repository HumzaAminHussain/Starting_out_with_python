p= float(input("What is the principal amount that you put in the bank: "))
r= float(input('What is the annual interest rate: '))
n=int(input('How many times is the interest compounded: '))
t= float(input('How many years will the account be left to earn interest: '))
r_2 = r/100
print(f'After {t} years you will have {p*(1+(r_2/n))**(n*t):.2f} dollars in the bank.')