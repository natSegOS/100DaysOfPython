import random


separator = "." * 30

win_message = r'''
      ___           ___           ___                    ___                       ___     
     |\__\         /\  \         /\__\                  /\__\          ___        /\__\    
     |:|  |       /::\  \       /:/  /                 /:/ _/_        /\  \      /::|  |   
     |:|  |      /:/\:\  \     /:/  /                 /:/ /\__\       \:\  \    /:|:|  |   
     |:|__|__   /:/  \:\  \   /:/  /  ___            /:/ /:/ _/_      /::\__\  /:/|:|  |__ 
     /::::\__\ /:/__/ \:\__\ /:/__/  /\__\          /:/_/:/ /\__\  __/:/\/__/ /:/ |:| /\__\
    /:/~~/~    \:\  \ /:/  / \:\  \ /:/  /          \:\/:/ /:/  / /\/:/  /    \/__|:|/:/  /
   /:/  /       \:\  /:/  /   \:\  /:/  /            \::/_/:/  /  \::/__/         |:/:/  / 
   \/__/         \:\/:/  /     \:\/:/  /              \:\/:/  /    \:\__\         |::/  /  
                  \::/  /       \::/  /                \::/  /      \/__/         /:/  /   
                   \/__/         \/__/                  \/__/                     \/__/
'''

lose_message = r'''
                                                                     .-')      ('-.   
                                                                    ( OO ).  _(  OO)  
  ,--.   ,--..-'),-----.  ,--. ,--.          ,--.      .-'),-----. (_)---\_)(,------. 
   \  `.'  /( OO'  .-.  ' |  | |  |          |  |.-') ( OO'  .-.  '/    _ |  |  .---' 
 .-')     / /   |  | |  | |  | | .-')        |  | OO )/   |  | |  |\  :` `.  |  |     
(OO  \   /  \_) |  |\|  | |  |_|( OO )       |  |`-' |\_) |  |\|  | '..`''.)(|  '--.  
 |   /  /\_   \ |  | |  | |  | | `-' /      (|  '---.'  \ |  | |  |.-._)   \ |  .--'  
 `-./  /.__)   `'  '-'  '('  '-'(_.-'        |      |    `'  '-'  '\       / |  `---. 
   `--'          `-----'   `-----'           `------'      `-----'  `-----'  `------'
'''

stage_0 = r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

stage_1 = r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

stage_2 = r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''

stage_3 = r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''

stage_4 = r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''

stage_5 = r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

stage_6 = r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]
num_stages = len(stages)


def display_progress(progress):
    print(stages[num_stages - progress[1] - 1], "\n")
    print("".join(progress[0]), "\n")


def indices(character, string):
    return [index for index, letter in enumerate(string) if letter == character]


def get_guess(progress):
    display_progress(progress)
    guess = input("Guess a letter:\n").lower()

    if len(guess) != 1:
        print("\nYou can only guess a single letter at a time! Try again.")
        print(separator)
        return get_guess()

    return guess


def update_progress(progress, word, guess):
    if guess in word:
        print("\nGreat guess!")

        occurrences = indices(guess, word)

        for index in occurrences:
            progress[0][index] = guess
    else:
        print(f"\nOops! Looks like '{guess}' isn't in the word.")
        progress[1] -= 1

    print(separator)
    return progress


def main():
    word_list = ["aardvark", "baboon", "camel"]

    word = random.choice(word_list)
    num_letters = len(word)

    progress = [["_"] * num_letters, num_stages - 1]
    
    is_game_over = False
    did_win = False
    
    while not is_game_over:
        guess = get_guess(progress)
        progress = update_progress(progress, word, guess)

        if not "_" in progress[0]:
            is_game_over = True
            did_win = True
        elif progress[1] < 1:
            is_game_over = True

    if did_win:
        print(win_message)
    else:
        print(lose_message)

    display_progress(progress)


if __name__ == "__main__":
    main()

