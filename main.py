import random as random

reRoll = True

input('Welcome to Dicer! When you are ready to roll the dice, press enter!')
while reRoll:
  invalidInput = True
  diceRoll = random.randint(1, 6)
  print("The dice landed at " + str(diceRoll) + ".")
  while invalidInput:
    print('Reroll?')
    print('1. Yes!')
    print('2. No...')
    reRollInput = input()
    if reRollInput == '1' or reRollInput == '2':
      invalidInput = False
      if reRollInput == '2':
        reRoll = False
    else: 
      invalidInput = True

print('Thanks for playing!')
