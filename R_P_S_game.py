import random

moves = ['rock', 'paper', 'scissors']

user = input("Enter your move (rock, paper, or scissors): ").lower()
computer = random.choice(moves)

print(f"You played {user}, computer played {computer}.")

if user == computer:
    print("It's a tie!")
elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer == 'rock' or user == 'scissors' and computer == 'paper':
    print("You win!")
else:
    print("Computer wins!")

