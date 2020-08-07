# 'Mad Libs' Generator

# A program that will ask users to choose a story template,
# enter a series of inputs to fill the template
# and then print a completed story

import random

def get_template(prompt):
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("\n     You must enter a number. \n")
            continue
        if 0 < choice < len(stories):
            print("\n     You have selected " + stories[choice-1] + ".\n")
            break
        elif choice == 0:
            choice = random.randint(1, len(stories))
            break
        else:
            print("\n     That story does not exist. \n")
    return choice


def get_propernouns():
    print("Type three proper nouns:")
    _i = 0
    while True:
        _i += 1
        _item = input("Proper noun #%d : " %_i)
        propernouns.append(_item)
        if _i == 3:
            print("\n")
            break
    return


def get_pronouns():
    print("Type three pronouns:")
    _i = 0
    while True:
        _i += 1
        _item = input("Pronoun noun #%d : " %_i)
        pronouns.append(_item)
        if _i == 3:
            print("\n")
            break
    return

def get_nouns():
    print("Type three nouns:")
    _i = 0
    while True:
        _i += 1
        _item = input("Noun #%d : " %_i)
        nouns.append(_item)
        if _i == 3:
            print("\n")
            break
    return

def get_adjs():
    print("Type five descriptive adj:")
    _i = 0
    while True:
        _i += 1
        _item = input("Descriptive adj #%d : " %_i)
        adjs.append(_item)
        if _i == 5:
            print("\n")
            break
    return

def get_objs():
    print("Type three objects:")
    _i = 0
    while True:
        _i += 1
        _item = input("Obj #%d : " %_i)
        objs.append(_item)
        if _i == 3:
            print("\n")
            break
    return

# TODO: Possible to optimize but combining multiple functions into 1
#   single function? Future story templates share # of inputs or different?

welcome = """

Welcome to NTimothy's Madlibs!

# |        Title        

0 | Random
1 | Adventure
2 | Story 2 
3 | Story 3

"""
# TODO Possible optimization with welcome text and storage of template titles?
stories = ["'Adventure'", "'Story2'", "'Story3'"]

print(welcome)
template = get_template("Please choose a new story template number:")

# Create empty lists to store input 
propernouns = []
pronouns = []
nouns = []
adjs = []
objs = []

# Call functions to fill empty lists
get_propernouns()
get_pronouns()
get_nouns()
get_adjs()
get_objs()


# Story templates
if template == 1:
    print(
        f"\n There was once a {adjs[0]} {nouns[0]} named {propernouns[0]}."
        f"\n {propernouns[0]} was feeling adventurous one day and so {pronouns[0]} decided"
        f"\n to go on a quest to find some {objs[0]}. But not just any {objs[0]}, "
        f"\n the most {adjs[1]} {objs[0]} ever. {pronouns[0]} had heard"
        f"\n {propernouns[1]} knew just where to find one, so {pronouns[0]}"
        f"\n asked them the next day."
        f"\n"
        f"\n {pronouns[1]} said,"
        f"\n 'I will tell you where you can find one, "
        f"\n but only if you give me a {adjs[2]} {objs[1]} in return."
        f"\n I cannot get it myself, because you will need to enter the forest {nouns[1]}s"
        f"\n 'A very {adjs[3]} demand, but I will get you what you request' replied {propernouns[0]}'."
        f"\n"
        f"\n Suddenly, a {adjs[4]} {objs[2]} flew past their heads. They both looked at the direction from"
        f"\n which it came and saw {propernouns[2]} the {adjs[4]}, a mysterious {nouns[2]} who lived nearby."
          )

elif template ==2:
    print("\n"
          "Story 2 | In development")

elif template ==3:
    print("\n"
          "Story 3 | In development")
