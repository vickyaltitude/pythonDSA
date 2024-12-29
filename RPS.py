import sys
import random

def RPS():
    items = ['Rock', 'Paper', 'Scissors']  
    play = True
    
    while play:
       
        comChoice = random.choice(items)
        
        playerChoice = input('''Choose your choice:
        1. Rock
        2. Paper
        3. Scissors
        Enter your choice (1, 2, or 3): ''')
        
     
        if playerChoice not in ['1', '2', '3']:
            print("Invalid input! Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")
            continue

        playerChoice = items[int(playerChoice) - 1]  
        print(f"You chose: {playerChoice}")
        print(f"Computer chose: {comChoice}")


        if playerChoice == comChoice:
            print("Match Tie!!!")
        elif (playerChoice == 'Rock' and comChoice == 'Scissors') or \
             (playerChoice == 'Paper' and comChoice == 'Rock') or \
             (playerChoice == 'Scissors' and comChoice == 'Paper'):
            print("Yay, you won!!!")
        else:
            print("Oops... Computer won!!!")
        
      
        playAgain = input("Wanna play again? (yes/no): ").lower()
        if playAgain not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break  

    sys.exit()

RPS()
