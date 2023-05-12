import random

words = ["apple", "banana", "cat", "dog", "elephant"]

word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0

while incorrect_guesses < 6:
    print("The word is: ", "".join(["_" if letter not in guessed_letters else letter for letter in word]))

    guess = input("Guess a letter: ")

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        print("Incorrect!")
        incorrect_guesses += 1

    if len(guessed_letters) == len(word):
        print("You won!")
        break

    if incorrect_guesses == 6:
        print("You lost!")
        break
