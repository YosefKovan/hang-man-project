from hangman.words import choose_secret_word
from hangman.io import prompt_guess, print_status, print_result

#================================
#         validate guess
#================================
def validate_guess(letter, guessed_letters):
    """validates if the letter was already guessed"""
    if letter in guessed_letters:
        return False, "Letter was guessed in the past"

    return True, "Letter was not guessed in the past"

#================================
#         add to display
#================================
def add_to_display(game_data, letter):
    """this function will add the guessed letters to the display list at the correct index"""
    secret = game_data["secret"]
    display = game_data["display"]

    for i in range(0, len(secret)):
        if secret[i] == letter:
            display.insert(i, letter)

#================================
#          apply guess
#================================
def apply_guess(game_data, letter):
    """this will check if the letter is in the secret and update if needed"""

    #game data secret is the secret string
    if letter in game_data["secret"]:
        game_data["guessed"].add(letter)
        add_to_display(game_data, letter)
        return True

    return False

#================================
#            is won
#================================
def is_won(game_data):
    """check if player won"""
    if '_' in game_data["display"]:
        return False
    return True

#================================
#            is lost
#================================
def is_lost(game_data):
    if game_data["wrong_guesses"] >= game_data["max_tries"]:
        return True
    return False

#================================
#           init state
#================================
def init_state(secret, max_tries):
    """this function initializes the data for the game"""

    #add '_' to display as the length of the word
    display = ["_" for i in range(0, len(secret))]

    data = {
        "secret" : secret,
        "display" : display,
        "guessed" : set(),
        "wrong_guesses" : 0,
        "max_tries" : max_tries
    }

    return data

#================================
#          play round
#================================
def play_round(game_data):
    """this function handles the logic for each round"""

    guessed_letter = prompt_guess()

    # this will check and validate if the letter was previously guessed!
    validate_guess_result = validate_guess(guessed_letter, game_data["guessed"])
    if not validate_guess_result[0]:
        print(validate_guess_result[1])
        return

    # if the letter was not guessed it will add it to the guessed
    game_data["guessed"].add(guessed_letter)

    # this will check and handle if the guessed letter is in the secret word!
    if apply_guess(game_data, guessed_letter):
        print("Guess was correct!")
    else:
        print("letter guessed is not correct!")
        game_data["wrong_guesses"] += 1

    print_status(game_data)

#================================
#          play game
#================================
def play_game():
    """main game logic and loop"""

    game_data = init_state(choose_secret_word(), 6)

    print_status(game_data)
    while not is_won(game_data) and not is_lost(game_data):
        play_round(game_data)

    print_result(game_data)







