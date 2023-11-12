import random

# Roll one dice
num = random.randrange(1, 7)
print('Result of the face number:', num)

# Roll two dices
die1 = random.randrange(1, 7)
die2 = random.randrange(1, 7)
print('Result of the face number of die1:', die1)
print('Result of the face number of die2:', die2)
print('Total:', die1+die2)