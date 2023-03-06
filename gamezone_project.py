import random

credit_points = 500
menu = {"tea": 10, "coffee": 20,"cold drink": 40,"sandwich": 50,"pie": 60}

def snake_and_ladder():
    global credit_points
    position = 0
    c= 0
    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {3: 38, 24: 33, 42: 93, 72: 84}
    
    while position < 100:
        input("Press enter to roll the dice...")
        dice = random.randint(1, 6)
        c = c +1
        if c > 20:
            credit_points -= 50
            break
        print("You rolled a", dice)
        if position + dice > 100:
            print("Oops, you rolled too high! You need to roll a", 100 - position, "or less to win.")
        else:
            position += dice
            if position in snakes:
                print("snake", snakes[position])
                position = snakes[position]
            elif position in ladders:
                print(" ladder! ", ladders[position])
                position = ladders[position]
            print("You are now on position", position)
    if position == 100:
        credit_points += 100        
        print("You won the game")


def tic_tac_toe():
    import numpy as np
    global credit_points

    board = np.zeros((3, 3)).astype(int)
    
    def check_win():
        if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
            return True
        if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
            return True
        return False
    
    def play_turn():
        x = int(input(f"What is player {turn}'s x position?"))
        y = int(input(f"What is player {turn}'s y position?"))
        try:
            if board[y, x]==0:
                board[y, x]=turn
            else:
                play_turn()
        except IndexError:
            play_turn()
    
    turn = 1
    move = 9
    while move >0:
        print (board)
        play_turn()
        if check_win():
            print (f"Player {turn} has won!")
            print (board)
            if turn ==1:
               credit_points += 100
            else:
               credit_points -= 50 
            break
        turn = turn*-1
        move = move -1

def r_p_s():
    global credit_points
    moves = ['rock', 'paper', 'scissors']

    user = input("Enter your move (rock, paper, or scissors): ").lower()
    computer = random.choice(moves)

    print(f"You played {user}, computer played {computer}.")

    if user == computer:
        print("It's a tie!")
    elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer == 'rock' or user == 'scissors' and computer == 'paper':
        print("You win!")
        credit_points += 100
    else:
        print("Computer wins!")
        credit_points -= 50
   

def guess_game():
    global credit_points
    
    number = random.randint(1, 10)
    guess = -1
    attempts = 0
    
    print("Guess a number between 1 and 10. You have 2 attempts.")
    
    while guess != number and attempts < 2:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
            
    if guess == number:
        print("Congratulations! You guessed the number in", attempts, "attempts.")
        credit_points += 100
    else:
        print("Sorry, you ran out of attempts. The number was", number)
        credit_points -= 50


def order(d):
        name=input("Enter the order name: ") 
        quantity=int(input("Number of Quantity: ") )
        d[name]=quantity

     
def remove(d):
    r = input("Enter item to remove")
    if r in d:
        d.pop(r)
    print(d)   
        
    
def modify(d):
    m = input("Modify Quanty of items:")
    n = int(input("New quantity"))
    if m in d:
        d[m]=d.get(m) + n
    print(d)    


def bill(d):
    global credit_points
    total = []
    for i in d.keys():
        if i in menu.keys():
             s = d[i] * menu[i]
             total.append(s)
             
    print("Total bill:" , sum(total))  
    credit_points -= sum(total)


def food():
    
    menu = {"tea": 10, "coffee": 20,"cold drink": 40,"sandwich": 50,"pie": 60}
    print(menu)
    d = {}
    name=input("Enter the order name: ") 
    quantity=int(input("Number of Quantity: ") )
    d[name]=quantity 

    print(d)  
    
    for i in menu:
        ask = int(input("1.add, 2. remove, 3.modify the quantity, 4. confirm/bill"))
        if ask == 1:
            order(d)
        if ask ==2:
            remove(d)   
        if ask ==3:
            modify(d) 
        print(d)   
        p = input("Done y or n:")
        if p == "y":
            bill(d)
            break 



def main():
    global credit_points
    
    print("Welcome to the Game Zone! You have", credit_points, "credit points.")
    
    while credit_points <=500:
        print("Which game would you like to play?")
        print("1. Snake and Ladder")
        print("2. Tic Tac Toe")
        print("3. Guessing Game")
        print("4. Rock Paper scissors Game")
        print("5. Order food")
        print("6. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            snake_and_ladder()
        elif choice == 2:
            tic_tac_toe()
        elif choice == 3:
            guess_game()
        elif choice == 4:
            r_p_s() 
        elif choice == 5:
            food()     
        elif choice == 6:
            print("Thanks for playing! Your final credit points are", credit_points)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    
