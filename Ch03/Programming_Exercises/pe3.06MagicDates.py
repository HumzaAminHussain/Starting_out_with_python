Month = int(input('Enter a month as a number (jan = 1, dec = 12): '))
day = int(input('Enter the day of the month: '))
year = int(input('Enter the last 2 digits of the year: '))
if Month*day == year:
    print("This date is a magic date.")
else:
    print('This date is not a magic date.')    