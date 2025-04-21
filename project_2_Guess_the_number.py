import random

print("🎯 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Generate random number
secret_number = random.randint(1, 100)
guesses = 0

while True:
    guess = input("Take a guess: ")

    # Make sure it's a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {guesses} tries!")
        break
