import random

choices = ['rock', 'paper', 'scissors']

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    comp = random.choice(choices)
    print("Computer chose:", comp)

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != 'y':
        break