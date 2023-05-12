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


if __name__ == "__main__":
    play_game("words.txt")
