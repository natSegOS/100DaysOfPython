import art
import random
import words


num_stages = len(art.stages)


def display_progress(progress):
    print(art.stages[num_stages - progress[1] - 1], "\n")
    print("".join(progress[0]), "\n")


def indices(character, string):
    return [index for index, letter in enumerate(string) if letter == character]


def get_guess(progress):
    display_progress(progress)
    guess = input("Guess a letter:\n").lower()

    if len(guess) != 1:
        print("\nYou can only guess a single letter at a time! Try again.")
        print(art.separator)
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

    print(art.separator)
    return progress


def main():
    word = random.choice(words.word_list)
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
        print(art.win_message)
    else:
        print(art.lose_message)

    display_progress(progress)


if __name__ == "__main__":
    main()

