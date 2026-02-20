import random
import time


def print_welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")
    print("Select a difficulty level to start.")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chance)")
    print("3. Hard (3 chances)")


def get_difficulty():
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("You have selected the Easy difficulty.")
        return 10, "Easy"
    elif choice == "2":
        print("You have selected the Medium difficulty.")
        return 5, "Medium"
    elif choice == "3":
        print("You have selected the Hard difficulty.")
        return 3, "Hard"
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        return 5, "Medium"


def update_high_score(high_scores, difficulty, attempts):
    if difficulty not in high_scores:
        high_scores[difficulty] = attempts
        print(f"New high score for {difficulty} difficulty: {attempts} attempts.")
    elif attempts < high_scores[difficulty]:
        high_scores[difficulty] = attempts
        print(f"New high score for {difficulty} difficulty: {attempts} attempts.")
    else:
        print(f"Current high score for {difficulty} difficulty: {high_scores[difficulty]} attempts.")


def play_round(high_scores):
    number = random.randint(1, 1000)
    chances, difficulty = get_difficulty()

    print(f"You have {chances} chances to guess the number.")
    print("Let's start the game!")

    attempts = 0
    start_time = time.time()

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 1000:
            print("Your guess must be between 1 and 1000.")
            continue

        attempts += 1

        if guess == number:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {total_time} seconds.")

            update_high_score(high_scores, difficulty, attempts)
            return

        elif guess < number:
            print("Incorrect! The number is greater than your guess.")
        else:
            print("Incorrect! The number is less than your guess.")

        remaining = chances - attempts
        print(f"You have {remaining} chances left.")

        distance = abs(number - guess)

        if distance <= 5:
            print("Hint: You are extremely close.")
        elif distance <= 10:
            print("Hint: You are within 10 numbers.")
        elif distance <= 20:
            print("Hint: You are within 20 numbers.")

        if remaining == 1:
            if number % 2 == 0:
                print("Final hint: The number is even.")
            else:
                print("Final hint: The number is odd.")

        if distance > 30 and number % 5 == 0:
            print("Hint: The number is divisible by 5.")

    print(f"You ran out of chances. The number was {number}.")


def main():
    high_scores = {}

    while True:
        print_welcome()
        play_round(high_scores)

        again = input("Do you want to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
