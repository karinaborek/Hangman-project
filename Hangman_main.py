import random
from display_hangman import display_hangman
from functions_hangman import *
from player import *

player_one = Player()
player_two = Player()
player_one.password = get_word()
player_two.password = get_word()
player_one.name = player_one.request_for_name()
player_one.tries = player_one.request_for_difficulty()
player_two.name = player_two.request_for_name()
player_two.tries = player_two.request_for_difficulty()


while True:

