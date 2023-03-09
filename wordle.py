import requests
import json
import sys

def send_query(query_string):
    max_res = '500'
    url = "https://api.datamuse.com/words?&max=" + max_res + "&sp=" + query_string
    print(url)
    response = requests.get(url)
    dlist = json.loads(response.text)
    dtuple = [tuple(d.values()) for d in dlist]
    dtuple.reverse()
    return dtuple

def print_results(words):
    print('----Results-----')
    for word in words:
        print('{} : {}'.format(word[0], word[1]))
    print('----------------')
    print(str(len(words)) + ' possible words')

def yellow_func(words, letter, position):
    result = []
    # yellow = input('Yellow letters')
    for tuple in words:
        word = tuple[0]
        if letter not in word or letter == word[position]:
            pass
        # if letter not in word:
        #     print('\tIgnored: {} not in {}'.format(letter, word))
        # elif letter == word[position]:
        #     print('\tIgnored: {} in position {} of {}'.format(letter, position, word))
        else:
            # print('\t{} is in {} and not in position {}'.format(letter, word, position))
            result.append(tuple)
    return result

def remove_greys(greys, words):
    for letter in greys:
        for tuple in words:
            word = tuple[0]
            # print('Checking for {} in {}'.format(letter,word))
            if letter in word:
                words.remove(tuple)
                # print('\tRemoved {}. It has a {}'.format(word, letter))
    return words

# GREEN LETTERS
lookup = input("Green letters, question marks: ")

# if len(sys.argv) == 2:
#     lookup = sys.argv[1]
# else:
#     lookup = input("Green letters, question marks: ")

poss_words = send_query(lookup)
print_results(poss_words)

while True:
    # YELLOW LETTERS
    while True:
        letter = input('Enter the yellow letter: ')
        if not letter:
            break
        else:
            position = int(input('Which position? (0 - 4): '))
            poss_words = (yellow_func(poss_words, letter, position))
            print_results(poss_words)

    # GREY LETTERS
    while True:
        greys = set(input('Enter the grey letters: '))
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