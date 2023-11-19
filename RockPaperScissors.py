import random

cChoice = random.choice('RPS')

# uChoice = input('Select one of the items(R: Rock, P: Paper, S:Scissors): ')

# print('You:', uChoice)
# print('Com:', cChoice)

uChoice = input('Select one of the items(R: Rock, P: Paper, S:Scissors): ').upper().strip()

print('You:', uChoice)
print('Com:', cChoice)

if cChoice == uChoice:
    print('Draw !!!')
elif uChoice == 'R' and cChoice =='P':
    print('You Lose !!!')
elif uChoice == 'P' and cChoice =='R':
    print('You Win !!!')
elif uChoice == 'R' and cChoice =='S':
    print('You Win !!!')
elif uChoice == 'S' and cChoice =='R':
    print('You Lose !!!')
elif uChoice == 'P' and cChoice =='S':
    print('You Lose !!!')
elif uChoice == 'S' and cChoice =='P':
    print('You Win !!!')
else:
    print('Something Wrong !')