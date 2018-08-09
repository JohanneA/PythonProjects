import random

def create_word_array(word):
    word_array= []
    for c in word:
        word_array.append(c)
    return word_array


def print_gallow(wrong_guesses_left):
    if wrong_guesses_left == 6:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#")
        print("\t#")
        print("\t#")
        print("\t#")
    if wrong_guesses_left == 5:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#")
        print("\t#")
        print("\t#")
    if wrong_guesses_left == 4:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#   |")
        print("\t#")
        print("\t#")
    if wrong_guesses_left == 3:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#  /|")
        print("\t#")
        print("\t#")
    if wrong_guesses_left == 2:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#  /|\\")
        print("\t#")
        print("\t#")
    if wrong_guesses_left == 1:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#  /|\\")
        print("\t#    \\")
        print("\t#")
    if wrong_guesses_left == 0:
        print("=============================")
        print("")
        print("\t######")
        print("\t#   |")
        print("\t#   O")
        print("\t#  /|\\")
        print("\t#  / \\")
        print("\t#")


def print_current_word(current_word):
    print("Current word ", end="")
    for c in current_word:
        if c == 0:
            print("_ ", end="")
        else:
            print(c + " ", end="")

def add_to_word(char, word, correct_word):
    new_word = word
    index = 0
    for c in correct_word:
        if c == ans:
            new_word[index]=c
        else:
            new_word[index]=word[index]
        index += 1
    return new_word


words = ["jazz", "outpouring", "world", "money", "horse", "kissing", "python", "pikachu", "rainbow", "fancy"]

while True:
    random_index = random.randint(0,len(words)-1)
    max_number_of_wrong_quesses =  6
    current_guesses = []
    current_word_chars = create_word_array(words[random_index])
    word = []
    for i in current_word_chars:
        word.append(0)

    print("DUN DUN DUN HANGMAN COMMENCES")
    print_gallow(max_number_of_wrong_quesses - len(current_guesses))
    print_current_word(word)
    print("   You already guessed these letters" + str(current_guesses))

    while True:
        if max_number_of_wrong_quesses == 0:
            print(" ")
            print("Nope, wrong, rip in pasta")
            break;
        ans = input("Guess a letter")
        if ans in current_word_chars:
            print("Correct!")
            word = add_to_word(ans,word,current_word_chars)
        else:
            current_guesses.append(ans)
            print("Wrong answer")
            max_number_of_wrong_quesses -= 1
        print(" ")
        print_gallow(max_number_of_wrong_quesses)
        print_current_word(word)
        print("   You already guessed these letters" + str(current_guesses))

        if 0 not in word:
            print(" ")
            print("Congratulations")
            break
    break


