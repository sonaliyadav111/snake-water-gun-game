'''
1 for snake 
-1 for water 
0 for gun
'''
import random

def get_computer_choice():
    options = ['Snake', 'Water', 'Gun']
    return random.choice(options)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Snake' and computer == 'Water') or \
         (player == 'Water' and computer == 'Gun') or \
         (player == 'Gun' and computer == 'Snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Snake, Water, Gun Game!")
    
    while True:
        player_choice = input("Enter your choice (Snake, Water, Gun) or 'quit' to exit: ").capitalize()
        
        if player_choice == 'Quit':
            print("Thanks for playing!")
            break
        
        if player_choice not in ['Snake', 'Water', 'Gun']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
