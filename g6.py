import random

def generate_guess(previous_guesses, previous_hints):
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)

    while True:
        guess = ''.join(digits[:6])
        if guess not in previous_guesses:
            break

    for i, digit in enumerate(guess):
        if digit == previous_hints[i]:
            continue
        elif digit in previous_hints:
            guess = guess.replace(digit, '', previous_hints.count(digit))
    return guess

previous_guesses = set()
previous_hints = []

while True:
    hint = input("Enter hint (X for correct digit and position, 0 for correct digit but wrong position, and _ for incorrect digit): ")
    previous_hints.append(hint)
    
    if 'X' * 6 in previous_hints:
        print("Congratulations, you guessed the PIN!")
        break

    guess = generate_guess(previous_guesses, previous_hints)
    print("Guess:", guess)

    previous_guesses.add(guess)
