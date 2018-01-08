import random

MIN = 1
MAX = 6
roll = True
while roll:
    input_from_keys = input("Do you want to roll a dice? Y or N ")
    if input_from_keys == 'Y':
        print(random.randint(MIN, MAX))
    else:
        print("Fine, go on then")
        break




