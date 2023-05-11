
import random


def play_game(filename):
    print("Guess The Mystery Word")
    print("Mission: Protect the city from a scary dragon by correctly guessing each letter in the mystery word")
    print("Rules:")
    print('1. You have 8 lives \u2665')

    with open(filename) as file:
        word_list = file.read().split()
        word_random = random.choice(word_list)
    print(word_random)

    display = ''
    for letter in word_random:
        display += ' _'
    print("The mystery word is: " + display)

    display_nested_list = []
    display_nested_list.append([*display])  # list looks like [[]]
    display_letter_list = sum(display_nested_list, [])
    del display_letter_list[::2]
    print(display_letter_list)

    nested_letter_list = []
    nested_letter_list.append([*word_random])
    letter_list_key = sum(nested_letter_list, [])

    letter_list_value = letter_list_key.copy()
    letters_dictionary = dict(zip(letter_list_key, letter_list_value))
    print(letters_dictionary)

    display_dictionary

    lives = 3
    while lives > 0:
        letter = input("guess a letter: ")
        if letter in word_random:
            print('Correct')
            print(display)
            print(letters_dictionary[letter])

        else:
            lives -= 1
            print("Incorrect. You have " +
                  str(lives) + ' ' + "lives " + "\u2665 "  "left.")

    print("Game Over. The scary dragon wins")


if __name__ == "__main__":
    play_game("words.txt")
