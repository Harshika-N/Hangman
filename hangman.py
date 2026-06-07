import random

def hangman():
    # List of words for the game
    words = ['python', 'java', 'javascript', 'ruby', 'swift', 'kotlin', 'hangman', 'programming', 'developer', 'computer']
    word = random.choice(words).lower()
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()  # What the user has guessed

    lives = 6

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        # Display current state
        print(f'You have {lives} lives left. You have used these letters: {' '.join(guessed_letters)}')
        # What the current word is (e.g., W - R D)
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1  # Take away a life if wrong
                print(f'\nYour letter, {user_letter}, is not in the word.')

        elif user_letter in guessed_letters:
            print('\nYou have already used that letter. Please try again.')
        else:
            print('\nInvalid character. Please try again.')

    # Game over
    if lives == 0:
        print(f'\nYou died, sorry. The word was {word}')
    else:
        print(f'\nYou guessed the word {word}!!')

if __name__ == '__main__':
    hangman()