import random

def start_game():
    min_range = 0
    max_range = 100
    rand = random.randint(min_range, max_range)
    while True:
        answer = input("Guess a number between " + str(min_range) + " and " + str(max_range) + ". ")
        if answer.isdigit():
            answer = int(answer)
            if answer == rand:
                print("Wooo, what a pro")
                break
            if answer > rand:
                print("Ooops, that's a bit too much!")
            if answer < rand:
                print("Might wanna add a bit more than that")
        else:
            print("Only numbers!!!!")


running = True

while running:
    input_from_keys = input("Are you ready to play? Y or N ")

    if input_from_keys == 'Y':
        start_game()
    else:
        break

