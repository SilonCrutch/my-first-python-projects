import random

def rpc_game():
    user = input("Rock, Paper or Scissors? ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    if user == computer:
        print(f"It's a draw! You both threw {computer}.")
    elif user == "rock" and computer == computer[2]:
        print(f"You win! You threw {user} and the computer threw {computer}.")
    elif user == "scissors" and computer == computer[1]:
        print(f"You win! You threw {user} and the computer threw {computer}.")
    elif user == "paper" and computer == computer[0]:
        print(f"You win! You threw {user} and the computer threw {computer}.")
    else:
        print(f"You lose! :( You threw {user} and the computer threw {computer}.")

    
rpc_game()