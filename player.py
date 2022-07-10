from urllib import request
from display_hangman import display_hangman
from functions_hangman import get_word

class Player:

    def __init__(self):
        pass
    def request_for_name(self):
        while True:
            name = input('What is your name?: ')
            confirm = input(f'type "yes" to confirm the name ({name}): ')
            if confirm == 'yes':
                return name
            else:
                print('enter a new name')


    def request_for_difficulty(self):
        while True:
            difficulty = input('select the difficulty level(easy, medium or hard): ')
            confirm = input(f'type "yes" to confirm your choice({difficulty}): ')
            if confirm == 'yes':
                if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
                    if difficulty == 'easy':
                        return 6
                    elif difficulty == 'medium':
                        return 5
                    elif difficulty == 'hard':
                        return 4
                else:
                    print('enter the correct difficulty')
    pass