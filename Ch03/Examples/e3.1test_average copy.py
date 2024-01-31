HIGH_SCORE = 95

test1 = int(input('Enter the score for test 1: '))
if test1 > 100:
    print("Please input a realistic number")
    test1 = int(input('Enter the new score for test 1: '))

test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

avarage = (test1 + test2 + test3) / 3
print(f'the avarage test score is {avarage:.2f}.')

if test2 > 100:
    print("Please input a realistic number")

if test3 > 100:
    print("Please input a realistic number")

if avarage >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')

if test1 == test2:
    print("Test 1 and test 2 are the same")

if test3 != test2:
    print("Test 2 and test 3 are not the same")