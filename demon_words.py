import sys
import random


def choose_level(list1, list2, list3, list4):
    level = input("Type 1, 2, army, or evil: ")
    if level == "1":
        list_to_randomize = list1
    elif level == "2":
        list_to_randomize = list2
    elif level == "army":
        list_to_randomize = list3
    elif level == "evil":
        list_to_randomize = list4
    return list_to_randomize


file = open("read.txt")
read_file = file.read()

file = open("read2.txt")
read_file2 = file.read()


def open_game(filename):
    with open(filename) as file:
        word_list = file.read().split()

    one_dragon_list = []
    two_dragon_list = []
    army_dragons_list = []
    evil_list = []
    list_to_randomize = []
    blank_list = []
    zero_list = []
    one_list = []

    for word in word_list:
        evil_list.append(word)
        if len(word) <= 6:
            one_dragon_list.append(word)
        if len(word) > 7 and len(word) <= 8:
            two_dragon_list.append(word)
        if len(word) >= 9:
            army_dragons_list.append(word)

    print(read_file)
    file.close()

    start_answer = input(
        "Will you accept this mission? Type Y or N: ")
    if start_answer == "Y":
        print("\n")
        print("**Great! The city needs you. Lets play.**")
        print("\n")
    elif start_answer == "N" or start_answer != "Y":
        print("**You must not be the hero the city needs. Come back when you have enough courage.**")
        sys.exit()

    print(read_file2)
    file.close()

    list_to_randomize = choose_level(
        one_dragon_list, two_dragon_list, army_dragons_list, evil_list)

    if list_to_randomize is one_dragon_list or two_dragon_list or army_dragons_list:
        word_random = random.choice(list_to_randomize)
        print(word_random)
        for letter in word_random:
            blank_list.append('_')
            print("The mystery word is " + str(len(word_random)) +
                  " letters " + " ".join(blank_list))

    guesses = 3
    if list_to_randomize is evil_list:
        while guesses > 0:
            word_random = random.choice(evil_list)
            print(word_random)
            for letter in word_random:
                blank_list.append('_')
                
            letter = input("guess a letter: ")
            if letter in word_random:
                print("Correct")
                for letter in word_random:
                    blank_list.append('_')
                for index in range(len(word_random)):
                    if word_random[index] == letter:
                        blank_list[index] = letter
                        print(' '.join(blank_list))

                for word_random in range(len(evil_list)):
                    word_random = ''
                    blank_list = []

    else:
        while guesses > 0:

            letter = input("guess another letter: ")
            if letter in word_random:
                print("Correct")
                for index in range(len(word_random)):
                    if word_random[index] == letter:
                        blank_list[index] = letter
                        print(' '.join(blank_list))

            if '_' not in blank_list:
                print("You saved the city!")
                break

            elif (len(letter) > 1):
                print("only guess 1 letter at a time")

            elif letter not in word_random:
                guesses -= 1
                if guesses == 1:
                    print("Incorrect. You have " + str(guesses) +
                          ' ' + "life " + "\u2665 "  "left.")
                if guesses > 1:
                    print("Incorrect. You have " + str(guesses) +
                          ' ' + "lives " + "\u2665 "  "left.")

                if guesses == 0:
                    print("Incorrect. You have no lives " + "\u2665 "  "left.")
                    if list_to_randomize is one_dragon_list:
                        print("\n")
                        print(
                            "*** GAME OVER. The word was " + word_random.upper() + ". The scary dragon wins ***")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "*** GAME OVER. The word was " + word_random.upper() + ". The scary dragons win ***")
                    print("\n")

    open_game("test_words.txt")


if __name__ == "__main__":
    open_game("test_words.txt")
