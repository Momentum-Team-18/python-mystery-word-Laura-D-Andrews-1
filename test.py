
import random


def play_game(filename):
    print("Guess The Mystery Word")
    print("Mission: Protect the city from a scary dragon by correctly guessing each letter in the mystery word")
    print("Rules:")
    print('1. You have 8 lives \u2665')
    print('2. You only lose a life if you guess a letter incorrectly')

    with open(filename) as file:
        word_list = file.read().split()
        word_random = random.choice(word_list)
    print(word_random)

    display = ''
    for letter in word_random:
        display += ' _'
    print("The mystery word is: " + display)

    letter_list = []
    blank_list = []
    for letter in word_random:
        letter_list.append(letter)
        blank_list.append('_')

    guesses = 3
    while guesses > 0:
        guess = input("guess a letter: ")
        if letter in word_random:
            print('Correct')
            for index in range(len(word_random)):
                if letter_list[index] == guess:
                    blank_list[index] = guess
                    fill_in_list = ' '.join(blank_list)
            print(fill_in_list)

            count = fill_in_list.count('_')
            print(count)
            for count in fill_in_list:
                if count == 0:
                    print('you won!')

        else:
            guesses -= 1
            print("Incorrect. You have " + str(guesses) +
                  ' ' + "lives " + "\u2665 "  "left.")

    print("Game Over. The scary dragon wins")


if __name__ == "__main__":
    play_game("words.txt")
