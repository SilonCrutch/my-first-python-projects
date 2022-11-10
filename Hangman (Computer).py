# The goal of this game is to get the computer to guess your word
import random
from Words import words
import string

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def string(x):
    random.shuffle(x)
    string1 = ""
    for ele in x:
        string1 += ele
    return string1

def com_lives():
    x = int(input("How many lives do you want me to have? "))
    if x >= 1 and x <= 3:
        print("I like a challenge! Bring it on!")
        return x
    elif x >= 4 and x <= 6:
        print("A little tough but I think I can manage.")
        return x
    elif x == 0:
        print("I can't do anything with no lives! Play fair! Let's try this again.")
        return com_lives()
    else:
        print("This won't even be a challenge!")
        return

def alpha_list(a):
    list = []
    list[:0] = a
    return list


def hangman_com():
    alphabet = alpha_list(letters)
    choice = random.choice(alphabet)
    wrong_letters = []
    correct_letters = []
    lives = com_lives()
    player = input("What is your secret word? (Don't worry, I won't look.) ").upper()

    while lives >= 1 and len(player) > 0:
        print(f"I currently have these many lives: {lives}")
        wordlist = [letter if letter in correct_letters else "_" for letter in player]
        print("My guess so far: ", " ".join(wordlist))
        computer = input(f"Is {choice} in your word? ")
        
        if (computer == 'y') or (computer == 'yes') or (computer == 'Y') or (computer == 'Yes') or (computer == 'YES'):
            remove = alphabet.remove(choice)
            right = correct_letters.append(choice)
            choice = random.choice(alphabet)
        elif (computer == 'n') or (computer == 'no') or (computer == 'No') or (computer == 'NO'):
            lives = lives - 1 
            remove = alphabet.remove(choice)
            wrong = wrong_letters.append(choice)
            choice = random.choice(alphabet)
        else:
            print("Invalid response. Please try again.")

        
        
        if len(correct_letters) == len(player):
            guess = string(correct_letters)
            win = input(f"The computer is unbeatable! Was {guess} your word? ")
            if (win == 'y') or (win == 'yes') or (win == 'Y') or (win == 'Yes') or (win == 'YES'):
                new_game3 = input("Wanna play again? ")
                if (new_game3 == 'y') or (new_game3 == 'yes') or (new_game3 == 'Y') or (new_game3 == 'Yes') or (new_game3 == 'YES'):
                    print("A glutton for punishment I see. Let's go!")
                    return hangman_com()
                elif (new_game3 == 'n') or (new_game3 == 'no') or (new_game3 == 'No') or (new_game3 == 'NO'):
                    print("What? Are you scared?")
                else:
                    print("I don't understand what that means so I'll just assume you don't want to play again.")
            elif (win == 'n') or (win == 'no') or (win == 'N') or (win == 'NO') or (win == 'No'):
                check = input("Oh really? What was it? ")
                if check == guess and check != player:
                    print("You're cheating! Let's do that again and play fair this time!")
                    return hangman_com()
                elif player != guess and player != check:
                    print(f"Do you take me for a fool? I sa- I mean, I'm pretty sure your original word was {player}. Play fair human!")
                    return hangman_com()
                else:
                    print("It seems you outsmarted me. This time...")                        
            else:
                print("I don't understand but I assume that's human speak for 'deafeat'?")                    
        elif lives == 0: 
            lose = input("Oh no! I lost! What was your secret word? ").upper()
            if lose == player:
                print(f"It seems that {lose} was too hard for me to guess.")
            else:
                print(f"I peeked and saw that your word was {player}. I'll let it slide since I lost fair-and-square but you should learn to play fair.")





    


hangman_com()
#com_lives()