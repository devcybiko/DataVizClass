import random
while True:
    options = ["r", "p", "s"]
    winning_combinations = ["rs", "sp", "pr"]

    ### for rock, paper, scissors, lizard, spock...
    # options = ["r", "p", "s", "l", "x"]
    # winning_combinations = ["sp", "pr", "rl", "lx", "xs", "sl", "lp", "px", "xr", "rs"]
    user_choice = input(options)
    computer_choice = random.choice(options);

    if user_choice not in options:
        print("bad choice")
        continue ### go to top of the while loop

    combo = user_choice + computer_choice
    if user_choice == computer_choice:
        print(f"it's a draw: you both picked {user_choice}\n")
    elif combo in winning_combinations:
        print(f"You won! {user_choice} beats {computer_choice}\n")
    else:
        print(f"You lost! {user_choice} loses to {computer_choice}\n")
