# Hangman Game

A web-based Hangman game built with **Flask** and **Vanilla JavaScript**. Guess the hidden word one letter at a time before you run out of lives.

## Features

- Interactive Hangman gameplay
- Built with Flask backend
- Vanilla JavaScript frontend
- Letter selection interface
- Hint system to reveal random letters
- Life counter with 6 attempts
- Start a new game anytime

## Project Structure

```
hangman-game/
│
├── app.py
├── requirements.txt
├--hangman.py
├── templates/
│   └── index.html
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Open in Browser

Navigate to:

```text
http://localhost:5000
```

## How to Play

1. A hidden word is selected randomly.
2. Click on letters to guess the word.
3. Correct guesses reveal the letter's position.
4. Incorrect guesses reduce your remaining lives.
5. You start with **6 lives**.
6. Click **Get Hint** to reveal a random unrevealed letter.
7. Guess the entire word before your lives reach zero.
8. Click **New Game** to start a fresh round.

## Game Rules

- Each incorrect guess costs one life.
- Repeated guesses are ignored.
- The game ends when:
  - All letters are guessed (**You Win!**)
  - Lives reach zero (**Game Over**)

## Technologies Used

- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **Vanilla JavaScript**

## Future Improvements

- Difficulty levels
- Score tracking
- Category-based word selection
- Leaderboard
- Responsive mobile design
- Sound effects and animations

## License

This project is open source and available under the MIT License.

## Author
Harshika N
