import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of guesses
guess_count = 0

# Start the guessing loop
while True:
    # Ask the user to guess the number
    user_guess = int(input("Guess the secret number (between 1 and 100): "))
    
    # Increment the guess count
    guess_count += 1

    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {guess_count} guesses.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")