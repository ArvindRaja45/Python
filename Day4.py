#ROCK PAPER SCISSORS
#You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = [rock, paper, scissors]
b = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
c = random.randint(0, 2)
if b == 0:
    print(a[b])
    print("Computer chose:")
    if c == 1:
        print(a[c])
        print("You lose")
    elif c == 2:
        print(a[c])
        print("You win")
    else:
        print(a[c])
        print("It's a draw")
elif b == 1:
    print(a[b])
    print("Computer chose:")
    if c == 2:
        print(a[c])
        print("You lose")
    elif c == 0:
        print(a[c])
        print("You win")
    else:
        print(a[c])
        print("It's a draw")
elif b ==2:
    print(a[b])
    print("Computer chose:")
    if c == 0:
        print(a[c])
        print("You lose")
    elif c == 1:
        print(a[c])
        print("You win")
    else:
        print(a[c])
        print("It's a draw")
else:
    print("You typed an invalid number. You lose!")
