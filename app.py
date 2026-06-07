import random
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

WORDS = ['python', 'java', 'javascript', 'ruby', 'swift', 'kotlin', 'hangman', 'programming', 'developer', 'computer']
MAX_LIVES = 6
ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

def init_game():
    word = random.choice(WORDS).lower()
    word_letters = set(word)
    guessed_letters = set()
    lives = MAX_LIVES
    return word, word_letters, guessed_letters, lives

def get_display_word(word, guessed_letters):
    return [letter if letter in guessed_letters else '_' for letter in word]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/new-game', methods=['POST'])
def new_game():
    word, word_letters, guessed_letters, lives = init_game()
    display_word = get_display_word(word, guessed_letters)
    return jsonify({
        'word': word,
        'display_word': ' '.join(display_word),
        'guessed_letters': [],
        'lives': lives,
        'game_over': False,
        'won': False,
        'message': 'New game started! Guess a letter.'
    })

@app.route('/api/guess', methods=['POST'])
def guess():
    data = request.get_json()
    word = data.get('word', '')
    guessed_letters = set(data.get('guessed_letters', []))
    lives = data.get('lives', MAX_LIVES)

    letter = data.get('letter', '').lower()

    if not letter or len(letter) != 1 or letter not in ALPHABET:
        display_word = get_display_word(word, guessed_letters)
        return jsonify({
            'display_word': ' '.join(display_word),
            'guessed_letters': sorted(list(guessed_letters)),
            'lives': lives,
            'game_over': False,
            'won': False,
            'message': 'Invalid character. Please try again.'
        })

    if letter in guessed_letters:
        display_word = get_display_word(word, guessed_letters)
        return jsonify({
            'display_word': ' '.join(display_word),
            'guessed_letters': sorted(list(guessed_letters)),
            'lives': lives,
            'game_over': False,
            'won': False,
            'message': f'You have already used that letter.'
        })

    guessed_letters.add(letter)
    message = ''

    if letter in set(word):
        message = f'Good job! {letter} is in the word.'
    else:
        lives -= 1
        message = f'Your letter, {letter}, is not in the word.'

    display_word = get_display_word(word, guessed_letters)
    game_over = lives == 0 or '_' not in display_word
    won = lives > 0 and '_' not in display_word

    if game_over:
        if won:
            message = f'You guessed the word {word}!!'
        else:
            message = f'You died, sorry. The word was {word}'

    return jsonify({
        'display_word': ' '.join(display_word),
        'guessed_letters': sorted(list(guessed_letters)),
        'lives': lives,
        'game_over': game_over,
        'won': won,
        'message': message
    })

@app.route('/api/hint', methods=['POST'])
def hint():
    data = request.get_json()
    word = data.get('word', '')
    guessed_letters = set(data.get('guessed_letters', []))
    lives = data.get('lives', MAX_LIVES)

    word_letters = set(word) - guessed_letters
    if word_letters:
        hint_letter = random.choice(list(word_letters))
        guessed_letters.add(hint_letter)

    display_word = get_display_word(word, guessed_letters)
    game_over = lives == 0 or '_' not in display_word
    won = lives > 0 and '_' not in display_word

    message = f'Hint: a letter was revealed!'
    if game_over:
        if won:
            message = f'You guessed the word {word}!!'
        else:
            message = f'You died, sorry. The word was {word}'

    return jsonify({
        'display_word': ' '.join(display_word),
        'guessed_letters': sorted(list(guessed_letters)),
        'lives': lives,
        'game_over': game_over,
        'won': won,
        'message': message
    })

if __name__ == '__main__':
    app.run(debug=True)
