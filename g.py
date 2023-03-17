import random

# Generate a random six-digit PIN code
pin = ''.join(str(random.randint(0, 9)) for _ in range(6))

# Keep track of previous guesses and hints
guesses = set()
hints = {}

# Define a function to check a guess against the PIN code and update hints
def check_guess(guess):
    if guess == pin:
        return True
    
    # Check for correct digits in correct position
    hint = ['X' if guess[i] == pin[i] else '_' for i in range(6)]
    
    # Check for correct digits in incorrect position
    for i in range(6):
        if hint[i] == '_':
            for j in range(6):
                if j != i and guess[j] == pin[i] and hint[j] == '_':
                    hint[i] = '0'
                    hint[j] = '0'
                    break
                    
    hints[guess] = hint
    return False

# Guess the PIN code within 15 attempts
for i in range(15):
    # Get user input for the next guess
    guess = input(f"Guess #{i+1}: ")
    
    # Check if guess has already been made
    if guess in guesses:
        print("You've already guessed that!")
        continue
    
    # Check if guess is valid
    if not guess.isdigit() or len(guess) != 6:
        print("Invalid guess! Please enter a six-digit number.")
        continue
    
    # Update previous guesses
    guesses.add(guess)
    
    # Check the guess against the PIN code and update hints
    if check_guess(guess):
        print("Congratulations, you guessed the PIN code!")
        break
    else:
        hint = hints[guess]
        print(f"Hint: {''.join(hint)}")
else:
    print("Sorry, you have run out of guesses. The PIN code was:", pin)
