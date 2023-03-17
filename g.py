import random

# Generate all possible PIN codes
all_codes = [f"{i:04}" for i in range(10000)]

# Initialize variables for previous guesses and hints
prev_guesses = []
prev_hints = []

# Initialize variables for current guess and hint
curr_guess = ""
curr_hint = ""

# Set the number of attempts allowed
attempts = 15

# Loop until the code is guessed or attempts run out
while attempts > 0:
    # Generate a new guess
    if curr_hint == "":
        curr_guess = random.choice(all_codes)
    else:
        possible_codes = []
        for code in all_codes:
            if all(code[i] == curr_guess[i] for i in range(4) if curr_hint[i] == "X") and \
                    all(code[i] != curr_guess[i] for i in range(4) if curr_hint[i] == "0"):
                possible_codes.append(code)
        curr_guess = random.choice(possible_codes)

    # Print the current guess and prompt for a hint
    print(f"Guess: {curr_guess}")
    hint = input("Hint (XXXX): ")

    # Check if the code has been guessed
    if hint == "XXXX":
        print(f"Code cracked in {16 - attempts} attempts!")
        break

    # Update the previous guesses and hints
    prev_guesses.append(curr_guess)
    prev_hints.append(hint)

    # Filter the possible codes based on the previous guesses and hints
    possible_codes = []
    for code in all_codes:
        if all(code[i] == curr_guess[i] for i in range(4) if hint[i] == "X") and \
                all(code[i] != curr_guess[i] for i in range(4) if hint[i] == "0") and \
                all(all(code[i] != prev_guess[i][i] for i in range(4) if prev_hint[i] == "X") or
                    all(code[i] == prev_guess[i][i] for i in range(4) if prev_hint[i] == "X") and
                    all(code[i] != prev_guess[i][i] for i in range(4) if prev_hint[i] == "0")
                    for prev_guess, prev_hint in zip(prev_guesses, prev_hints)):
            possible_codes.append(code)

    # Update the all_codes list and decrement the attempts
    all_codes = possible_codes
    attempts -= 1

    # Print the remaining attempts
    print(f"Attempts left: {attempts}")

# Print the code if it was not guessed
if attempts == 0:
    print("Code not cracked :(")
