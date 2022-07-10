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