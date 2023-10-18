import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Loop for a maximum of 10 attempts (you can adjust this number)
for attempt in range(1, 11):
    # Ask the user to guess the number
    user_guess = int(input(f"Guess {attempt}: Guess the secret number (between 1 and 100): "))
    
    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempt} attempts.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
# If the loop completes without the correct guess, inform the user
else:
    print(f"Sorry, you've used all 10 attempts. The secret number was {secret_number}.")