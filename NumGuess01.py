import random

userInput = ''
userGuess = 0

randNum = random.randrange(1, 101)

print('Guess what the number is selected between 1 and 100')

while randNum != userGuess:
    userInput = input('Expected Number: ').strip()

    if not userInput.isnumeric():
        print(userInput, 'This is not a number')
    else:
        userGuess = int(userInput)

        if userGuess < randNum:
            print("It's small. Please guess again with a larger number")
        elif userGuess > randNum:
            print("It's large. Please guess again with a smaller number")
        else:
            print('You got the number!')
