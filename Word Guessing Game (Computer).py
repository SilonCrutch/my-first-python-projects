import random

def guess_my_word(x):
    word = random.choice(x)
    choice = ", ".join(x)
    guess = input(f"These are your options: \"{choice}\". I bet I can guess what word you're thinking of. Does it start with \"{word[0]}\"? Yes or No ").lower()
    if guess == 'n' or guess == 'no':
        wrong = x.remove(word)
        guess = input(f'Then what was it? {choice} ').lower()
        if guess in x:
            print("Guess I am not as good as I thought! :\ ")
        elif guess == word:
            print(f"You tried to trick me! You said it was not {word} but it was!")
        else:
            print("That was not an option! You're cheating!")
    elif guess == 'y' or guess == 'yes':
        guess = input(f'Is it {word}? Yes or No ')
        if guess == 'n' or guess == 'no':
            print(f'Oops, I thought it was {word} haha. Better luck next time.')
        else: 
            print(f'I knew it was {word}! Didn\'t I tell you I could guess your word?')
    else:
        print("I do not understand what you mean so I assume that means I win!")

guess_my_word(["fish", "butter", "run", "bear", "dog", "baby", "water"])