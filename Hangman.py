import random

maxLives = 7        
maskChar = "_"      
livesUsed = 0       
guessedLetters = [] 

gameWords = ["anvil", "boutique", "cookie", "fluff",
            "jazz", "pneumonia", "sleigh", "society",
            "topaz", "tsunami", "yummy", "zombie"]

gameWord = random.choice(gameWords)

displayWord = maskChar * len(gameWord)

while gameWord != displayWord and livesUsed < maxLives:

    print(displayWord)

    if len(guessedLetters) > 0:
        youTried = ""
        for letter in guessedLetters:
            youTried += letter
        print("Tried Letters:", youTried)

    print(maxLives - livesUsed, "Count left")
    
    print()

    currGuess = input("Guessed Letters:").strip().lower()
    if len(currGuess) > 1:
        currGuess = currGuess[0]
    if currGuess in guessedLetters:
        print("It's the letter you already guessed", currGuess)
    else:
        guessedLetters.append(currGuess)
        guessedLetters.sort()
        displayWord = ""
        for letter in gameWord:
            if letter in guessedLetters:
                displayWord += letter
            else:
                displayWord += maskChar

        if currGuess in gameWord:
            print ("Right Guess!")
        else:
            print ("Wrong!")
            livesUsed += 1
    
    print()

if displayWord == gameWord:
    print ("Win! The word is", gameWord+'!')
else: 
    print ("Lose! The word is", gameWord+'!')