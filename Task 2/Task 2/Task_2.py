import random   # Import the random module to generate random numbers

flag = 0   # A flag variable to check if the user guessed correctly (0 = not guessed, 1 = guessed)

# Generate a random integer between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

# Loop gives the user 10 attempts to guess
for i in range(10):
    # Show remaining attempts (starts from 10 down to 1)
    print(f"Your Attempts: {10-i}")
    
    # Take input from the user and convert it to an integer
    try:
        user_guess = int(input("Please guess the hidden number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter an integer from 1 to 100") # Handle non-integer input from the user
        continue 
    
    # Validate input: Check if the guess is within the valid range (1–100)
    if user_guess < 1 or user_guess > 100:
        print("Please enter number between 1 and 100: ")
        continue   # Skip the rest of the loop and ask again
    
    # If the guess is greater than the hidden number
    elif user_guess > random_number:
        print("too high")
    
    # If the guess is smaller than the hidden number
    elif user_guess < random_number:
        print("too low")
    
    # If the guess matches the hidden number
    elif user_guess == random_number:
        print("Congratulation You Guessed the Number Correctly 🥳🎉")
        flag = 1   # Mark flag as guessed correctly
        break      # Exit the loop since the number is guessed

# After the loop, check if the flag is still 0 (means the number was never guessed)
if flag == 0:
    print("We’re sorry, but you have reached the maximum number of attempts.")
