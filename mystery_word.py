import sys
import random


def play_game(filename):
    print("Guess The Mystery Word")
    print("Mission: Protect the city from a scary dragon by correctly guessing each letter in the mystery word")
    print("Rules:")
    print('1. You have 8 lives \u2665')
    print('2. You only lose a life if you guess a letter incorrectly')
    start_answer = input(
        "Do you want to accept your mission? Type Y or N: ")
    if start_answer == "Y":
        print("**Great! The city needs you. lets play.**")
    elif start_answer == "N":
        print("**You must not be the hero the city needs. Come back when you have enough courage.**")
        sys.exit()

    with open(filename) as file:
        word_list = file.read().split()
        word_random = random.choice(word_list)
    print(word_random)

    display = ''
    for letter in word_random:
        display += ' _'
    print("The mystery word is: " + display)

    blank_list = []
    for letter in word_random:
        blank_list.append('_')

    guesses = 3
    while guesses > 0:
        letter = input("guess a letter: ")
        if letter in word_random:
            print("correct")
            for index in range(len(word_random)):
                if word_random[index] == letter:
                    blank_list[index] = letter
            print(' '.join(blank_list))

        else:
            guesses -= 1
            print("Incorrect. You have " + str(guesses) +
                  ' ' + "lives " + "\u2665 "  "left.")
    # if guesses == 0:
    #     print('you lose')

    print("Game Over. The scary dragon wins")

    play_game(filename)


if __name__ == "__main__":
    play_game("words.txt")
