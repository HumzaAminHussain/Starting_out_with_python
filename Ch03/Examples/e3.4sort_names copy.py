flag =  True
while flag:
    name1 = input('Enter a name (last name first): ')
    name2 = input('Enter another name (last name first): ')
    if name1 < name2:
        print('Here are the name, listed alphabetically.')
        print(name1)
        print(name2)
        flag = False
    if name2 < name1:
        print('Here are the name, listed alphabetically.')
        print(name2)
        print(name1)
        flag = False
    else:
        print('The names are the same, please put different names.')
print("end program")