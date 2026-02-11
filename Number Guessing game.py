import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = input("Enter your guess (or 'q' to quit): ").strip()

            # Allow the player to quit
            if guess.lower() == 'q':
                print(f"Game over! The number was {secret_number}.")
                break

            guess = int(guess)

            # Validate range
            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Check guess
            if guess < secret_number:
                print("Too low! 📉 Try again.")
            elif guess > secret_number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("⚠ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
