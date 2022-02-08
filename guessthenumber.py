# This is a guess the number game
import random

secretNumber = random.randint(1,20)

# The player guesses 6 times
print('I am thinking of a number between 1 and 20')

guesses = 0
while guesses < 6:
    print('Take a guess.')
    try:
        guess = int(input())
        guesses += 1

    except:
        print('Type in an integer.....')

    if guesses == 6:
        print(f'Nope, you did not get the secret number. The secret number is {secretNumber}')
        break
    elif guess == secretNumber:
        print(f'Good job! You guessed my number in {guesses} guesses!')
        break
    elif guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
