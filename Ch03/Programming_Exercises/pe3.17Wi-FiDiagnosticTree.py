yes =  False
no = True
print('Reboot the computer and try to connect.')
problem = input('Did that fix the problem?(Enter yes or no, all lowercase): ')
if problem == "no":
    print('Reboot the router and try to connect.')
    problem = input('Did that fix the problem?(Enter yes or no, all lowercase): ')
    yes =  False
    no = True
    if problem == "no":
        print("Make sure the cables between the router and modem are plugged in firmly")
        problem = input('Did that fix the problem?(Enter yes or no, all lowercase): ')
        yes =  False
        no = True
        if problem == "no":
            print('Move the router to a new location.')
            problem = input('Did that fix the problem?(Enter yes or no, all lowercase): ')
            yes =  False
            no = True
            if problem:
                print('Get a new router.')
elif problem == "yes":
    print('')
# ask michael to help.