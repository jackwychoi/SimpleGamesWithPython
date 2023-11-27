currGuess = input('Guess a character: ').strip().lower()

if len(currGuess) > 1:
    currGuess = currGuess[0]

print(currGuess)