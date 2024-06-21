import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Please select a range by entering two integers, X and Y.")

    while True:
        try:
            x = int(input("Enter the lower bound (X): "))
            y = int(input("Enter the upper bound (Y): "))
            if x >= y:
                print("Invalid range! X should be less than Y. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter integers only.")

    print(f"Great! You've selected a range from {x} to {y}.")

    secret_number = random.randint(x, y)

    print("I've generated a random number in the range. Try to guess it!")

    num_guesses = 0
    max_guesses = int(input("Enter the maximum number of Guesses :"))
    while num_guesses != max_guesses:
        try:
            user_guess = int(input(f"Enter your guess ({x} to {y}): "))
            if user_guess < x or user_guess > y:
                print("Invalid guess! Please enter a number within the range.")
            else:
                num_guesses += 1
                if user_guess == secret_number:
                    print(f" Congratulations! You've guessed the number in {num_guesses} attempts.")
                    break
                elif user_guess < secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter an integer only.")
    
if __name__ == "__main__":
    number_guessing_game()