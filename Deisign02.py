guessLetters = []
for i in range(0, 5):
    currGuess = input('Guessed Character: ').strip().lower()
    guessLetters.apppend(currGuess)

guessedLetters.sort()

print(guessLetters)
