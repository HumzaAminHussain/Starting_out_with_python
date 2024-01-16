r = float(input('How long is the row in feet: '))
e = int(input('How many feet does an end-post assembly take: '))
s = int(input('How may feet do you want each vine to be apart from each other: '))
both_e = e*2
print(f"You can have {(r-(both_e))/s} vines in the row.")   