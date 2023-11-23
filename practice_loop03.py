animals = []

userInput = ' '

print("Let's make a list for animals")
print('Please type one animal at once')
print('Let it be blank to finish')

while userInput != '':
    userInput = input('Type the kind of animals. Let it be blank to finish: ')\
    .strip()

    if len(userInput) > 0:
        animals.append(userInput)

animals.sort()

print(animals)
