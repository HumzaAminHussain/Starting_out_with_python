seconds = int(input('Enter a number of seconds: '))
MINUTE = 60
HOUR = 3600
DAY = 86400
if seconds > DAY:
    day = seconds//DAY
    seconds = seconds%DAY
    hour = seconds//HOUR
    seconds = seconds%HOUR
    minute = seconds//MINUTE
    seconds = seconds%MINUTE
    print(f'That is {day} day\'s, {hour} hour\'s, {minute} minutes, and {seconds} seconds.')
elif seconds == DAY:
    print(f'That is {1} day.')
elif seconds > HOUR:
    hour = seconds//HOUR
    seconds = seconds%HOUR
    minute = seconds//MINUTE
    seconds = seconds%MINUTE
    print(f'That is {hour} hour\'s, {minute} minutes, and {seconds} seconds.')
elif seconds == HOUR:
    print(f'That is {1} hour.')
elif seconds == MINUTE:
    print(f'That is {1} minute.')
elif seconds > MINUTE:
    second = seconds%MINUTE
    minute = seconds//MINUTE
    print(f'That is {0} hour\'s, {minute} minute and {second} seconds.')