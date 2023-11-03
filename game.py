import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of attempts
max_attempts = 5
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

while attempts < max_attempts:
    try:
        guess = int(input(f"You have {max_attempts - attempts} attempts left. Enter your guess: "))
        
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts + 1} attempts.")
            break

        attempts += 1
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")