guessedLetters = []

for i in range(0, 5):
    youTried = input('Guessed Character: ').strip().lower()
    guessedLetters.append(youTried)

    for letter in guessedLetters:
        print('Tried Letter: ', letter)

print(guessedLetters)