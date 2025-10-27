from hangman.game import render_display, render_guessed

def prompt_guess():
    """asks the user to choose a letter"""

    while True:

        choice = input("Please enter a valid alphabetic letter: ")
        if choice.isalpha() and len(choice) < 2:
           return choice
        else:
            print("invalid input try again")


def print_status(game_data):

    render_display(game_data)
    #
    # print("letters Guessed: " + " ".join(game_data["guessed"]))
    # print("Wrong guesses: " + str(game_data["wrong_guesses"]))
    

def print_result(game_data):

    if game_data["wrong_guess"] >= game_data["max_tries"]:
        print("You lost!")
    else:
        print("You won!")

