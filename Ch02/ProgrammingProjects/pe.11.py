males = int(input('How many males are in this class: '))
females = int(input('How many females are in this class: '))
people = males+females
malepercent = (males/people)*100
femalepercent = (females/people)*100
print(f'This class is {malepercent:.2f}% males and {femalepercent:.2f}% females. ')
