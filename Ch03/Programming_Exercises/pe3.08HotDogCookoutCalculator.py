people = int(input('How many people are coming to the cook out: '))
peopleeat = int(input('How many Hot dogs is each person eating: '))
HOTDOG = 10
BUN = 8
hotdogpeople = people * peopleeat
if hotdogpeople%HOTDOG > 0:
    print(f"You need {hotdogpeople//HOTDOG+1} hotdog packages.")
else:
    print(f"You need {hotdogpeople//HOTDOG} hotdog packages.")
if hotdogpeople%BUN > 0:
    print(f"You need {hotdogpeople//BUN+1} hotdog bun packages.")
else:
    print(f"You need {hotdogpeople//BUN} hotdog bun packages.")
if hotdogpeople%HOTDOG > 0:
    print(f'You will have {HOTDOG*(hotdogpeople//HOTDOG+1)-(hotdogpeople%HOTDOG)} hotdogs left over.')
if hotdogpeople%BUN > 0:
    print(f'You will have {BUN*(hotdogpeople//BUN+1)-(hotdogpeople%BUN)} hotdog buns left over.')
