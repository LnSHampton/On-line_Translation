# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:35:04 2021

@author: LnSHa

Project: Multilingual Online Translator

Stage 7/7: Unexpected

DESCRIPTION

Okay, it seems like your program translates as expected. However, there’s a 
problem you should always keep in mind: something can break your program.

Up to this stage, you were thinking about things that should be in your code. 
But what if things go wrong? For example, you gave your program to someone 
who’s not familiar with the concept behind it. What if they try to translate 
to or from languages different from those you have in your code, or even 
start typing jabberwocky? That can break your program.

All these situations are called exceptions because you didn’t expect them to 
happen, and now you have to handle them.

Examples

The greater-than symbol followed by a space (> ) represents the user input. 
Note that it's not part of the input.

Example 1

Notify users that they cannot translate to or from some languages.

> python translator.py english korean hello
Sorry, the program doesn't support korean

Example 2

Check and notify if there’s a problem with the user’s internet connection.

> python translator.py english all hello
Something wrong with your internet connection

Example 3

Tell the user that you can’t translate jabberwocky.

> python translator.py english all brrrrrrrrrrr
Sorry, unable to find brrrrrrrrrrr



"""
# Posted to Hyperlink
from bs4 import BeautifulSoup
import requests
import sys


lang = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
        'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
url = 'https://context.reverso.net/translation/'
from_language, to_language = sys.argv[1:3]
try:
    from_lang = lang.index(from_language.capitalize())
except ValueError:
    print(f"Sorry, the program doesn't support {from_language}")
    sys.exit()
try:
    to_lang = -1 if to_language.upper() == 'ALL' else lang.index(to_language.capitalize())
except ValueError:
    print(f"Sorry, the program doesn't support {to_language}")
    sys.exit()
word = sys.argv[3]
file_path_name = word + '.txt'
beg = end = to_lang
if to_lang < 0:
    beg, end = 0, len(lang)-1
for n in range(beg, end+1):
    if n == from_lang:
        continue
    target_url = url + lang[from_lang].lower() + '-' + lang[n].lower() + '/' + word.lower()
    r = requests.get(target_url, headers={'user-agent': 'my-app/0.0.1'})
    status_code = r.status_code
    if 400 <= status_code <= 499:
        print(f'Sorry, unable to find {word}')
        sys.exit()
    if status_code >= 500:
        print('Something wrong with your internet connection')
        sys.exit()
    my_soup = BeautifulSoup(r.content, 'html.parser')
    word_translations = my_soup.find_all('a', {'class': 'dict'})
    phrases = my_soup.find_all('div', {'class': ['src', 'trg']})
    words = [t.text.strip('\n').strip() for t in word_translations]
    phrases2 = [e.text.strip('\n ') for e in phrases if e.text.strip()]
    print(f'{lang[n]} Translations')
    print(*(words[i] for i in range(0, min(len(words), 5))), sep='\n')
    print(f'\n{lang[n]} Examples:')
    for i in range(0, min(len(phrases2), 10), 2):
        print(*(phrases2[i] for i in range(i, i+2)), sep='\n')
        print()
    with open(file_path_name, 'a+', encoding='utf-8') as f:
        f.write(f'{lang[n]} Translations\n')
        for i in range(0, min(len(words), 5)):
            f.write(words[i] + '\n')
        f.write(f'\n{lang[n]} Examples:\n')
        for i in range(0, min(len(phrases2), 10), 2):
            for j in range(i, i+2):
                f.write(phrases2[j] + '\n')
            f.write('\n')

#%%
# Working copy
from bs4 import BeautifulSoup
import requests
import sys


lang = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
        'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
url = 'https://context.reverso.net/translation/'

# from_language = input('from language> ')
# to_language = input('to langauge> ')
from_language, to_language = sys.argv[1:3]
try:
    # from_lang = lang.index(sys.argv[1].capitalize())
    from_lang = lang.index(from_language.capitalize())
except ValueError:
    print(f"Sorry, the program doesn't support {from_language}")
    sys.exit()

# if to_language.upper() == 'ALL':
#     to_lang = -1
# else:
try:
       # to_lang = lang.index(sys.argv[2].capitalize())
       # to_lang = lang.index(to_language.capitalize())
    to_lang = -1 if to_language.upper() == 'ALL' else lang.index(to_language.capitalize())
except ValueError:
    print(f"Sorry, the program doesn't support {to_language}")
    sys.exit()

# print(f'From language: {from_lang}')
# print(f'To language: {to_lang}')
# sys.exit()

# from_lang = lang.index(sys.argv[1].capitalize())
# to_lang = -1 if sys.argv[2] == 'all' else lang.index(sys.argv[2].capitalize())
word = sys.argv[3]
file_path_name = word + '.txt'
beg = end = to_lang
if to_lang < 0:
    beg, end = 0, len(lang)-1
for n in range(beg, end+1):
    if n == from_lang:
        continue
    target_url = url + lang[from_lang].lower() + '-' + lang[n].lower() + '/' + word.lower()
    r = requests.get(target_url, headers={'user-agent': 'my-app/0.0.1'})
    status_code = r.status_code
    # print('status code', status_code, type(status_code))
    if 400 <= status_code <= 499:
        print(f'Sorry, unable to find {word}')
        sys.exit()
    if status_code >= 500:
        print('Something wrong with your internet connection')
        sys.exit()
    my_soup = BeautifulSoup(r.content, 'html.parser')
    word_translations = my_soup.find_all('a', {'class': 'dict'})
    phrases = my_soup.find_all('div', {'class': ['src', 'trg']})
    words = [t.text.strip('\n').strip() for t in word_translations]
    phrases2 = [e.text.strip('\n ') for e in phrases if e.text.strip()]
    print(f'{lang[n]} Translations')
    print(*(words[i] for i in range(0, min(len(words), 5))), sep='\n')
    print(f'\n{lang[n]} Examples:')
    for i in range(0, min(len(phrases2), 10), 2):
        print(*(phrases2[i] for i in range(i, i+2)), sep='\n')
        print()
    with open(file_path_name, 'a+', encoding='utf-8') as f:
        f.write(f'{lang[n]} Translations\n')
        for i in range(0, min(len(words), 5)):
            f.write(words[i] + '\n')
        f.write(f'\n{lang[n]} Examples:\n')
        for i in range(0, min(len(phrases2), 10), 2):
            for j in range(i, i+2):
                f.write(phrases2[j] + '\n')
            f.write('\n')

#%%


