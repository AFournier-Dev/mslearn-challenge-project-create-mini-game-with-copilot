import random

# write 'hello world' to the console
# print('hello world')



"""
What you should consider in the game interactions
Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
By the end of each round, the player can choose whether to play again.
Display the player's score at the end of the game.
The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
In your GitHub Codespaces, use the provided specifications to create prompts that can be utilized by GitHub Copilot to assist you in developing the minigame. Remember, GitHub Copilot uses comments to understand context and provide accurate suggestions during development.
"""
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock (r), paper (p), or scissors (s)): ").lower()
        if user_choice in ['rock', 'r', 'paper', 'p', 'scissors', 's']:
            return user_choice[0] if len(user_choice) > 1 else user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes (y)/no (n)): ").lower()
        if play_again in ['yes', 'y', 'no', 'n']:
            return play_again.startswith('y')
        else:
            print("Invalid choice. Please try again.")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        if not play_again():
            break

    print("Game over!")

play_game()
