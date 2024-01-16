import random
numbers = []
for i in range(10):
    numbers.append(random.randint(0, 1000))


print(numbers)

names = ["humza", "mike", 'sally',"bob", 'eric', 'yumcha', 'joe', 'thomas', 'jake', 'ryan' ]
jobs = ["repariman", "teacher", 'cashier',"doctor", 'dog walker', 'plumber', \
        'pediatrist', 'pedeatrition', 'cook', 'veteran' ]


print(f"=====================================\n  NAMES   |  JOBS | NUMBERS\n==================")
for i in range(10):
    print(f'|{names[i]:>10} | {jobs[i]:>15} | {numbers[i]:5}|')