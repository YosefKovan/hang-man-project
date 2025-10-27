
def prompt_guess():
    """asks the user to choose a letter"""

    while True:

        choice = input("Please enter a valid alphabetic letter: ")
        if choice.isalpha() and len(choice) < 2:
           return choice
        else:
            print("invalid input try again")

def render_guessed(game_data):
    """this function will print the letters that were guessed"""
    print("Letters Guessed: " + ', '.join(game_data["guessed"]))

def render_display(game_data):
    """this will print the letters that were guessed"""
    print("Letters left to guess: " + " ".join(game_data["display"]))

def render_summary(game_data):
    print("Secret word: " + game_data["secret"])
    render_guessed(game_data)

def print_status(game_data):

    render_display(game_data)
    render_guessed(game_data)
    print("Wrong guesses: " + str(game_data["wrong_guesses"]))

def print_result(game_data):

    if game_data["wrong_guess"] >= game_data["max_tries"]:
        print("You lost!")
    else:
        print("You won!")

