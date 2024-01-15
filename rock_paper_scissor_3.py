# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min
# rock == rock --> draw, paper == paper --> draw, scissor == scissor --> draw
import my_module

print("Welcome to rock, paper, scissors game")
print("There are 3 modes: human vs human (HH), human vs computer (HC), computer vs computer (CC)\n")

#gamemode = input("Please select your mode - human vs human (HH), human vs computer (HC), "                  
#"computer vs computer (CC) or quit (Q)\n").upper()

gamemode = "NOT_SET"


# game loop
while (gamemode != "Q"):

    if (gamemode == "HH"):
        human_1_input = input("Human one, please enter ROCK, PAPER, or SCISSOR\n").upper()   
        human_2_input = input("Human two, please enter ROCK, PAPER or SCISSOR\n").upper()
        my_module.game_logic(human_1_input, human_2_input, "Human one", "Human two")
    elif (gamemode == "HC"):
        human_1_input = input("Human, please enter ROCK, PAPER, or SCISSOR\n").upper()
        computer_input = my_module.rand_convert()
        my_module.game_logic(human_1_input, computer_input, "Human", "Computer")

    gamemode = input("Please select your mode - human vs human (HH), human vs computer (HC), "                  
    "computer vs computer (CC) or quit (Q)\n").upper()




