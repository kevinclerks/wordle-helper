import requests
import json
from colorama import Fore, Style

def send_query(query_string):
    max_res = '500'
    url = "https://api.datamuse.com/words?&max=" + max_res + "&sp=" + query_string
    print(url)
    response = requests.get(url)
    dlist = json.loads(response.text)
    dlist.reverse()
    return dlist

def print_results(words_list):
    print('----Results-----')
    for entry in words_list:
        print('{} : {}'.format(entry['word'], entry['score']))
    print('----------------')
    print(str(len(words_list)) + ' possible words')

def yellow_func(words_list, letter, position):
    words_list[:] = [d for d in words_list if 
              letter in d.get('word') and letter != d.get('word')[position]]
    return words_list

def yellow_func2(words_list, letter, position):
    result = []
    for entry in words_list:
        word = entry['word']
        # if letter not in word or letter == word[position]:
        #     pass
        if letter not in word:
            print('\tIgngored: {} not in {}'.format(letter, word))
        elif letter == word[position]:
            print('\tIgnored: {} in position {} of {}'.format(letter, position, word))
        else:
            # print('\t{} is in {} and not in position {}'.format(letter, word, position))
            result.append(entry)
    return result

def remove_greys(greys, candidate_list):
    for letter in greys:
        candidate_list[:] = [d for d in candidate_list if letter not in d.get('word')]

    return candidate_list

# GREEN LETTERS
lookup = input(Fore.GREEN + "Green letters, question marks: " + Style.RESET_ALL)
poss_words = send_query(lookup)
print_results(poss_words)

while True:
    # YELLOW LETTERS
    while True:
        letter = input(Fore.YELLOW + 'Enter the yellow letter: '+ Style.RESET_ALL)
        if not letter:
            break
        else:
            position = int(input('Which position? (0 - 4): '))
            poss_words = (yellow_func(poss_words, letter, position))
            print_results(poss_words)

    # GREY LETTERS
    while True:
        greys = input(Style.DIM + 'Enter the grey letters: '+ Style.RESET_ALL)
        if not greys:
            break
        else:
            poss_words = remove_greys(greys, poss_words)
            print_results(poss_words)
    
    game_on = input('Continue? (y/n): ')
    if game_on.lower()[0] == 'y':
        game_on = True
        continue
    else:
        game_on = False
        break