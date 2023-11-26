import random

guesses = 0
numMin = 1
numMax = 100
userInput = ''
userGuess = 0

randNum = random.randrange(numMin, numMax + 1)

print('Guess a number between', numMin, 'and', numMax)

while randNum != userGuess:
    userInput = input('Expected Number: ').strip()

    if not userInput.isnumeric():
        print(userInput, 'This is not a number')
    else:
        guesses = guesses + 1
        userGuess = int(userInput)

        if userGuess < numMin or userGuess > numMax:
            print(userGuess, 'is not a number between', numMin, 'and', numMax)
        elif userGuess < randNum:
            print("It's small. Please guess again with a larger number")
        elif userGuess > randNum:
            print("It's large. Please guess again with a smaller number")
        else:
            print('Yeah! You got the number! Total Trying Count', guesses)  
    