from random import randrange

def get_all_word():
    """this will read all the words from the text file"""
    with open("./data/words.txt", 'r') as f:
        file_content = f.read()
        return file_content.split('\n')


def choose_secret_word():
   """this function will return a random word"""
   words = get_all_word()
   random_index = randrange(0, len(words))
   return words[random_index]
