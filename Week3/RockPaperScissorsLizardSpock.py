import random
while True:
    options = ["r", "p", "s", "l", "x"]
    names = {"r": "Rock", "p": "Paper", "s": "Scissors", "l": "Lizard", "x": "Spock"} ## i totally stole this from Alex!
    reasons = { 
        ### the key is a combination of the user selection and the computer selection.
        ### the first letter is the users's choice, the second letter is the computer's choice
        ### note: reverse the two letters of the key for when the computer beats the user's choice
        ### the value is the reason for the win
        "sp": "Scissors cuts Paper",
        "pr": "Paper covers Rock", 
        "rl": "Rock crushes Lizard", 
        "lx": "Lizard poisons Spock", 
        "xs": "Spock smashes Scissors", 
        "sl": "Scissors decapitates Lizard",
        "lp": "Lizard eats Paper", 
        "px": "Paper disproves Spock",
        "xr": "Spock vaporizes Rock",
        "rs": "As it always has, Rock crushes Scissors."
    }
    user_choice = input(names)
    computer_choice = random.choice(options);
    if user_choice not in options:
        print("bad choice")
        continue ### go to top of the while loop
    else:
        print(f"You picked {names[user_choice]}, I picked {names[computer_choice]}")

    combo = user_choice + computer_choice ### use this as an index into the 'reasons' dictionary
    obmoc = computer_choice + user_choice ### 'obmoc' is 'combo' reversed (for when the computer wins)
    if user_choice == computer_choice: ### check for a tie first...
        print(f"it's a draw: we both picked {names[user_choice]}\n")
    elif combo in reasons: ### if 
        print(f"You won! {reasons[combo]}\n") ### print the reason for the user's win from the 'reasons' dictionary
    else:
        print(f"You lost! {reasons[obmoc]}\n") ### note: using 'obmoc' because we need the key for when the computer wins
