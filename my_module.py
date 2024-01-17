
# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min 

import random

def rand_convert():

    roll = random.randint(1,3)
    if (roll == 1):
        return "ROCK"
    elif (roll == 2):
        return "PAPER"
    else:
        return "SCISSOR"

def rand_convert_v2():
    _roll = random.choice(["ROCK","PAPER","SCISSOR"])
    return _roll

def game_logic(inPlayer1_input, inPlayer2_input, inPlayer1_name, inPlayer2_name):

    _rock = "ROCK"
    _paper = "PAPER"
    _scissor = "SCISSOR" 

    _values = []
    _values.append("ROCK")
    _values.append("PAPER")
    _values.append("SCISSOR")

    # hh first
    if (inPlayer1_input == inPlayer2_input):
        print("Game is a DRAW")
    elif (inPlayer1_input != inPlayer2_input):
        if (inPlayer1_input == _rock and inPlayer2_input == _paper):
            print(inPlayer2_name + " wins with " + inPlayer2_input + 
            " over " + inPlayer1_input)
        elif (inPlayer1_input == _paper and inPlayer2_input == _rock):
            print(inPlayer1_name + " wins with " + inPlayer1_input + " over "
            + inPlayer2_input)
        elif (inPlayer1_input == _rock and inPlayer2_input == _scissor):
            print(inPlayer1_name + " wins with " + inPlayer1_input + " over " 
            + inPlayer2_input)
        elif (inPlayer1_input == _scissor and inPlayer2_input == _rock):
            print(inPlayer2_name + " wins with " + inPlayer2_input + " over " 
            + inPlayer1_input)
        elif (inPlayer1_input == _scissor and inPlayer2_input == _paper):
            print(inPlayer1_name + " wins with " + inPlayer1_input + " over " 
            + inPlayer2_input)
        elif (inPlayer1_input == _paper and inPlayer2_input == _scissor):
            print(inPlayer2_name + " wins with " + inPlayer2_input + " over " 
            + inPlayer1_input)

