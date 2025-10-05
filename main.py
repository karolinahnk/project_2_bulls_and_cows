import random
import time

def opening_text() -> None:
    print("Hi There")
    print("--------------------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("--------------------------------------------------------")
    print("Enter a number:")
    print("--------------------------------------------------------")

def unique_number():
    """Loading 4 unique numbers without zero at first position"""

    numbers = [str(num) for num in range(10)]
    first = random.choice(numbers[1:])
    others = random.sample([num for num in numbers if num != first], 3)
    return first + " ".join(others)

def valid_tip(tip: str) -> tuple[bool, str]:
    """Check if the players tip is valid and returns the message"""

    if len(tip) != 4:
        return False, "Unique number must be exactly 4 digits long."
    if not tip.isdigit():
        return False, "Unique number must have only digits."
    if tip[0] == "0":
        return False, "Unique number can`t start with zero."
    if len(set(tip)) != 4:
        return False, "Unique number can`t be repeat."
    return True, ""

def count_bulls_cows(tip: str, secret: str) -> tuple[int, int]:
    """
    Counting how many bulls and cows we have. Cows are not include bulls
    and bulls not include cows
    """

    bulls = sum(tip1 == tip2 for tip1, tip2 in zip(tip, secret))
    cows = sum(cows in secret for cows in tip) - bulls
    return bulls, cows

def result(bulls: int, cows: int) -> None:
    """Prints the result of the guess with singular or plural form."""

    bull_text = "bull" if bull == 1 else "bulls"
    cow_text = "cow" if cow == 1 else "cows"
    print(f"{bulls} {bull_text}, {cows} {cow_text}\n")

def game() -> None:
    """
    Launch and the entire course of the game principle.
    Counts how long the game lasts.
    """

    opening_text()
    secret = unique_number()
    attempts = 0
    start_time = time.time()

    while True:
        print("--------------------------------------------------------")
        tip = input("Enter a number: ").strip()
        print("--------------------------------------------------------")

        valid, error = valid_tip(tip)
        if not valid:
            print("Wrong tip:", error, "\n")
            continue

        attempts += 1
        bulls, cows = count_bulls_cows(tip, secret)
        result(bulls, cows)

        if bulls == 4:
            end_time = time.time()
            elapsed = int(end_time - start_time) 
            minutes, seconds = divmod(elapsed, 60)

            print(f"Correct, you've guessed the right number!")
            quess_word = "guess" if attempts == 1 else "guesses"
            print(f"in {attempts} {guess_word}!")
            print(f"Time taken: {minutes} min {seconds} sec")
            print("--------------------------------------------------------")
            print("That is amazing!")
            break
        
if __name__ == "__main__":
    game()