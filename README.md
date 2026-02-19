Overview

This is a Command Line Interface number guessing game written in Python. The computer randomly selects a number between 1 and 1000. The player chooses a difficulty level and attempts to guess the correct number within a limited number of chances.

If the player guesses correctly within the allowed attempts, they win. If they run out of chances, the game reveals the correct number.

Features

* Random number generation between 1 and 1000
* Three difficulty levels
  * Easy: 10 chances
  * Medium: 5 chances
  * Hard: 3 chances
* Input validation for non numeric and out of range guesses
* Higher or lower feedback after each guess
* Distance based hint system
* Final chance parity hint
* Divisibility hint when far from target
* Timer to track how long it takes to win
* High score tracking per difficulty level during session
* Multiple rounds support

How the Game Works

1. The game displays a welcome message and difficulty options.
2. The player selects a difficulty level.
3. The system generates a random number.
4. The player enters guesses.
5. The game provides feedback after each guess.
6. The round ends when the player guesses correctly or runs out of chances.
7. The player can choose to play another round.

Requirements

* Python 3.13.1

No external libraries are required. The game uses only built in modules:

* random
* time

How to Run

1. Clone the repository:

git clone https://github.com/abduladama001/number-guessing-cli

2. Navigate into the project directory:

cd number-guessing-cli

3. Run the program:

python number_guessing_game.py

Game Rules

* The number is always between 1 and 1000.
* Invalid inputs do not reduce attempts.
* Out of range guesses are rejected.
* Hints are provided based on how close the guess is.
* High scores track the fewest attempts per difficulty level during a single session.

Project Structure

number_guessing_game.py
README.md

Learning Objectives

This project demonstrates:

* Function based program structure
* Input validation
* Loop control and condition handling
* Random number generation
* Basic timing logic
* State management with dictionaries

Author

Abdulrahman Suleiman Adama

License

This project is open source and free to use for learning purposes.
