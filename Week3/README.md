# Week 3

## Rock, Paper, Scissors

My solution uses a `list` to store all the possible winning combinations. This is much simpler than creating the "if hydra". 


```python
    winning_combinations = ["rs", "sp", "pr"]
```

Then, I combine the `user_choice` and the `computer_choice` to make a unique string for the game. If the string is in the list, then the user has won. Otherwise they've lost. 

* NOTE: I simplified the logic by first checking for a tie
* NOTE: I also know that if it's not a tie or a win for the user, it must be a win for the computer (or a loss for the user).

```python
    combo = user_choice + computer_choice
    if user_choice == computer_choice:
        print(f"it's a draw: you both picked {user_choice}\n")
    elif combo in winning_combinations:
        print(f"You won! {user_choice} beats {computer_choice}\n")
    else:
       print(f"You lost! {user_choice} loses to {computer_choice}\n")
```

## Rock, Paper, Scissors, Lizard, Spock

The advantage of this solution is that it generalizes to [Rock, Paper, Scissors, Lizard, Spock (RPSLX)](https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock) just by updating the `list` of `options` and `winning_combinations`. No other changes are necessary.

```python
    options = ["r", "p", "s", "l", "x"]
    winning_combinations = ["sp", "pr", "rl", "lx", "xs", "sl", "lp", "px", "xr", "rs"]
```

## RPSLX: Redux

With a few embellishments, the game can also explain the reasons for the win/loss of RPSLX:

```python
    options = ["r", "p", "s", "l", "x"]
    names = {"r": "Rock", "p": "Paper", "s": "Scissors", "l": "Lizard", "x": "Spock"} ## i totally stole this from Alex!
    reasons = { 
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
```

Here, the `reasons` dictionary has a "key" that is all the winning combinations. And the "value" is the reason for the win.

As before, I combine the `user_choice` and the `computer_choice` as an index into the `reasons` dictionary. If  `combo in reasons` then I know the user has won. AND, I can print the exact reason (as explained by Sheldon) for the win.

Notice, that to print the reason for the `computer_choice` win, the `combo` has to be reversed. There is a programmatic way to do it, but it's [not a pretty sight](https://stackoverflow.com/questions/931092/reverse-a-string-in-python). In this case it was sufficient to create a separate variable `obmoc` with the concatenation reversed.

```python
    combo = user_choice + computer_choice 
    obmoc = computer_choice + user_choice 
    if user_choice == computer_choice: 
        print(f"it's a draw: we both picked {names[user_choice]}\n")
    elif combo in reasons:
        print(f"You won! {reasons[combo]}\n") 
    else:
        print(f"You lost! {reasons[obmoc]}\n")
```

## Game Play

```
{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}r
You picked Rock, I picked Spock
You lost! Spock vaporizes Rock

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}p
You picked Paper, I picked Scissors
You lost! Scissors cuts Paper

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}l
You picked Lizard, I picked Paper
You won! Lizard eats Paper

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}s
You picked Scissors, I picked Rock
You lost! As it always has, Rock crushes Scissors.

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}x
You picked Spock, I picked Paper
You lost! Paper disproves Spock

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}r
You picked Rock, I picked Spock
You lost! Spock vaporizes Rock

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}p
You picked Paper, I picked Paper
it's a draw: we both picked Paper

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}l
You picked Lizard, I picked Scissors
You lost! Scissors decapitates Lizard

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}s
You picked Scissors, I picked Paper
You won! Scissors cuts Paper

{'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'l': 'Lizard', 'x': 'Spock'}x
You picked Spock, I picked Rock
You won! Spock vaporizes Rock
```