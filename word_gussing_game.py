import random
import time

name = input("Enter your name: ")
print("Good luck!", name)

words = ['fortnite', 'clashofclan', 'pubg', 'subwaysurfer',
         'mobilelegend', 'hillclimb', 'minecraft']

correct_word = random.choice(words)

print("Guess a word")
guesses = ''

count = 10

while count > 0:

    failed = 0

    for char in correct_word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print("You win!")
        print("You correctly guess the word", correct_word)
        break

    guess = input("Start guessing: ")
    guesses += guess

    if guess not in correct_word:
        count -= 1
        print("Incorrect")
        print("You have", +count, "more guess chance")

        if count == 0:
            print("You lose! the correct word is", correct_word)




