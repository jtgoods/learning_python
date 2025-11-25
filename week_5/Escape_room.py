# Pseudocode
"""
1. setup
    1.1 explain challenges
2. enter code
    2.1 prompt player for 4-digit code
    2.2 validate input (must be 4 digits)
        2.2.1 if invalid, prompt again
    2.3 check code correctness
        2.3.1 if correct, proceed
        2.3.2 if wrong, end game
3. choose path
    3.1 prompt player for L, C, or R
    3.2 validate input (must be L, C, or R)
        3.2.1 if invalid, prompt again
    3.3 check path correctness
        3.3.1 if correct, proceed
        3.3.2 if wrong, end game
4. balance weights
    4.1 prompt for left weight
    4.2 prompt for right weight
    4.3 validate both inputs (must be digits)
        4.3.1 if invalid, prompt again
    4.4 check if left + right == target sum
        4.4.1 if correct, proceed/win
        4.4.2 if wrong, end game
5. end message
    5.1 show win/lose message
"""

# Define main functions

def enter_code():
    """
    2. enter code
        2.1 prompt player
        2.2 check code
        2.3 branch on success/failure
    """
	# prompt for four digit code, reject wrong input, give feedback
    code_pass = "4507" # passing code to advance to next stage
    while True: # repeating loop
        code = input("Enter the four digit code to move on: ") #input code
        if not code.isdigit() or len(code) != 4: #validation check for 4-digit code
            print(f"'{code}' is not a valid 4-digit number. Try again.")
            continue
        if code == code_pass: # passing example 
            print("Correct code! The door unlocks.")
            return True
        else: #if code is incorrect
            print(f"Code '{code}' is incorrect. The temple rumbles!")
            return False

def choose_path():
    """
    3. choose path
        3.1 prompt player
        3.2 check path 
        3.3 branch on success/failure
    """
    path_pass = "L" # passing path to move on to the final stage
    while True:
        path = input("You meet a three-way path, choose L, R, or C") #three way path input
        path = path.upper() # convert to uppercase
        path = path.strip() # convert to solitary letter
        if path not in ("L", "R", "C"): # validation checking for L, R, or C
            print("You have entered an invalid response. Enter 'L', 'R', or 'C'")
            continue
        if path == path_pass: # correct path
            print("Congratulations, you have chosen the correct path. The door beyond opens") # pass message
            return True
        else:
            print(f"You have chosen '{path}', which is the wrong path. The temple floor swallows you whole!") # fail message
            return False


def balance_weights():
    """
    4. balance weights
        4.1 prompt for left weight
        4.2 prompt for right weight
        4.3 validate both inputs (must be digits)
            4.3.1 if invalid, prompt again
        4.4 check if left + right == target sum
            4.4.1 if correct, proceed/win
            4.4.2 if wrong, end game
    """
    target_sum = 10
    while True:
        left = input("Add stones: How many on the left side? ")
        right = input("Add stones: How many on the right side? ")
        if not left.isdigit() or not right.isdigit():
            print(f"Both must be numbers! Try again.")
            continue
        left = int(left)
        right = int(right)
        if left + right == target_sum:
            print(f"The scales balance perfectly at {target_sum}! You solved the final puzzle.")
            return True
        else:
            print(f"The scales tip unevenly... {left}+{right} does not balance. Try again.")

# Main program flow
def start_temple_escape():
    """Main game flow controlling the temple puzzles."""
    print("\n🏛️ Welcome to the Ancient Temple of Code!")
    print("Solve all three puzzles to escape.\n")

    if enter_code():
        if choose_path():
            balance_weights()

    print("\nEnd of attempt. Restart the temple to try again.")

# Start the adventure
start_temple_escape()
