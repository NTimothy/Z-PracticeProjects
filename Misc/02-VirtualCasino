# Arcade

# A program which allows a player to play various mini-gambling type games

import random


# function for cleanliness
def clear():
    cl = "\n"*20
    print(cl)


# default invalid option print
def invalid():
    print("That is not a valid option.\n")


menu1_options = ["Fish Prawn Crabs", "Blind Man's Bluff", "to cash out"]


def game_menu():
    _i = 0
    while True:
        try:
            print("\n" + welcome)
            print(f"You currently have {p_credits} credits to play with.\n")
            _i = int(input("Select your option:"))
            if -1 < _i < len(menu1_options):
                clear()
                print("\n\n     You have selected " + menu1_options[_i] + ".\n")
                break
            else:
                clear()
                print(f"\n\n Error. {_i} is not a valid option.")
                continue
        except ValueError:
            clear()
            print("\n Error. You must enter a single number.")
            continue
    return _i


def menu_fpc():
    global p_credits
    while True:
        if p_credits <= 0:
            break
        menu0 = {
            "1": "Play",
            "2": "Explain Rules",
            "3": "..Return to front desk"
        }
        fpc_options = menu0.keys()
        try:
            print("You are at the Fish Prawn Crabs table.")
            for _i in fpc_options:
                print(_i, menu0[_i])
            print("\n")
            selection = input("Please select an option:")
        except ValueError:
            clear()
            print("You must enter a valid number")
            continue
        if selection == '1':
            clear()
            play_fpc()
            continue
        elif selection == '2':
            clear()
            print(fpc_rules)
            continue
        elif selection == "3":
            clear()
            break
        else:
            clear()
            print("\n\nError. That is not a valid option\n\n")
            continue


def play_fpc():
    dice = ["fish", "prawn", "crab", "rooster", "stag", "tiger"]
    clear()
    net = 0
    while True:
        c_check(net)
        if p_credits <= 0:
            break
        bet_map["fish"] = 0
        bet_map["prawn"] = 0
        bet_map["crab"] = 0
        bet_map["rooster"] = 0
        bet_map["stag"] = 0
        bet_map["tiger"] = 0
        _betlist = []
        _winnings = []
        _spent = []
        _a = random.choice(dice)
        _b = random.choice(dice)
        _c = random.choice(dice)
        _winlist = [_a, _b, _c]
        net = 0
        print("\n The dice have been rolled!\n")
        _ans = y_n()
        if _ans == "y":
            _current_bet = fpc_bet(p_credits, net)
            clear()
            print("You have bet(s) on:")
            count = 0
            for key, value in bet_map.items():
                if value > 0:
                    _spent.append(value)
                    if key in _winlist:
                        count += 1
                        _winnings.append(value * _winlist.count(key))

                    _betlist.append(key)
                    print(key.upper())

            print("""\nTime for dice reveal!""")
            print("     Dice #1 shows", _a.upper())
            print("     Dice #2 shows", _b.upper())
            print("     Dice #3 shows", _c.upper(), "\n")

            profit = sum(_winnings)*count
            net = profit - sum(_spent)
            print("You started with", p_credits, "credits.")
            print("Your winnings gained you", profit, "credits.")
            print("You bet a total of", sum(_spent), "credits.")
            match = compare(_betlist, _winlist)
            if len(match) > 0 and net > 0:
                print(f"You've won {net} credits!")
            elif net == 0:
                print(f"You broke even!")
            else:
                print(f"You netted a lost of {net} credits.")

        elif _ans == "n":
            clear()
            break
        else:
            clear()
            invalid()
        continue


def fpc_bet(x, y):
    _money = x + y
    global p_credits
    p_credits = _money
    _num_bets = 0
    _bet_total = 0
    _bet = 0
    while True:
        try:
            print(f"\n\nYou currently have {_money} credits to play with.")
            if _money <= 0:
                print("You ran out of money.")
                return _bet_total
            print(f"\n\nYou have made {_num_bets} bet(s) worth {_bet_total} credits.")

            if _num_bets == 3:                          # if maximum number of bets are made
                clear()
                return _bet_total

            _bet = int(input("Enter a bet amount.\n"))

            if _bet == 0:                               # if no more bets want to be made
                clear()
                break

            elif 0 < _bet <= p_credits:                         # if a valid bet is placed, complete calculations
                clear()
                _num_bets += 1
                _bet_total += _bet
                _money -= _bet
                fpc_animal(_bet)                        # function to determine bet placement
                continue
            else:
                clear()
                invalid()
                continue
        except ValueError:
            _bet = -1
            continue


def fpc_animal(amt):
    while True:
        print("\n")
        animals = ["fish", "prawn", "crab", "rooster", "stag", "tiger"]
        _animals = [animal.capitalize() for animal in animals]
        print(_animals)
        choice = input("\n What are you betting on? ").lower()
        if choice in animals:
            bet_map[choice] += amt
            break
        else:
            clear()
            invalid()
            continue


def c_check(a):
    global p_credits
    p_credits = p_credits + a
    print(f"\nYou currently have {p_credits} credits remaining.")


def y_n():
    while True:
        ans = input("Would you like to place a bet (Y/N): ")
        ans = ans.lower()
        if ans == "y" or "n":
            return ans
        else:
            print("Please respond with 'Y' for Yes or 'N' for No.")
            continue


def compare(bet, win):
    winners = [value for value in bet if value in win]
    return winners


welcome = ("""Welcome to the casino!
    0 | Fish Prawn Crab
    1 | Blind Man's Bluff
    2 | ..Cash out.
    """)
fpc_rules = ("""
F I S H    P R A W N    C R A B    R U L E S
========================================================================
Fish Prawn Crab is game involving dice and luck.

It is also known by other names and variations:
    Chuck-a-luck or Birdcage [American]
    Crown & Anchor [British]
    Hoo Hey How [Chinese]
    Bầu cua tôm cá [Vietnamese]

There are 3 dice with depictions of animals on each side of the dice:
    Fish
    Prawn
    Crab
    Rooster
    Stag
    Tiger
------------------------------------------------------------------------

3 dice are rolled at the beginning of a round and hidden from view
while players can make bets. At the end of a round, the dice are 
revealed and payouts given based on the bets made.

 - You may make up to 3 separate bets each round
 - Minimum bet is 1
 - No maximum bet

Payout rates are as follows:

    1 match        1:1
    2 matches      2:1
    3 matches      3:1
    3 of a kind    30:1 [not yet implemented]
    
========================================================================
""")
bet_map = {
    "fish": 0,
    "prawn": 0,
    "crab": 0,
    "rooster": 0,
    "stag": 0,
    "tiger": 0,
}
p_credits = 100


while p_credits > 0:
    try:
        option = game_menu()
        if option == 0:
            menu_fpc()
            continue
        elif option == 1:
            print("Game 1 here\n")     # TODO Game/functions not yet implemented
            continue            
        elif option == 2:
            print(f"\nYou have left the casino with {p_credits} credits!")
            break
        else:
            clear()
            invalid()
        continue
    finally:
        if p_credits <= 0:
            print("You ran out of credits! Better luck next time.")
            exit()
