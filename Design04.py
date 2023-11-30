gameWord = "apocalypse"
guessedLetters = ["a", "e"]
maskChar = "_"

displayWord = ""

for letter in gameWord:
    print(letter)
    if letter in guessedLetters:
        print("Yes. It's right.")
        displayWord += letter
    else:
        print("No. It's wrong.")
        displayWord += maskChar
    print("displayWord is", displayWord)

print("Original Word:", gameWord)
print("Customized Word:", displayWord)