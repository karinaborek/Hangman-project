import random
with open('countries-and-capitals.txt','r') as f:
    countries = f.readlines()
def get_word():
    new_list = []
    for country in countries:
        split_country = country.split(' | ')
        new_list.append(split_country[0])
        new_list.append(split_country[1])
    word = (random.choice(new_list))
    return word.upper()

def word_hiding(word):
    password = ''
    for letter in word:
        if letter != ' ':
            letter = '_'
            password += letter
        elif letter == ' ':
            password += letter
    return list(password)

def discovering_letters(discover_password):
    discover_password_list = list(discover_password)
    choice = input('')
    hidden_word_list = word_hiding(discover_password)
    for index,element in enumerate(discover_password_list):
        if discover_password_list[index] == choice:
            hidden_word_list[index] = choice
    hidden_word = ''.join(hidden_word_list)
    print(hidden_word)