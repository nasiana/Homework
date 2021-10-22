
'''
HOMEWORK 3: Nasian Ahmed
'''

'''
TASK 1 (Conditional flow)
'''

# Q1: Create a program that tells you whether or not you need an umbrella when you leave the house.

def umbrella_need():
    user_q = (input("Is it currently raining? Please reply with y/n ")).lower()
    if user_q == 'y':
        print('In the famous words of Queen RiRi (Rihanna)...Please take an umbrella!')
    elif user_q == 'n':
        print('Fortunately for you buddy, today you do not need an umbrella!')
    else:
        print('You have entered input which is not valid. The program will run again, please reply with input\
        that is either "y/n"')
        umbrella_need()

umbrella_need()

#Q2:

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money >= boat_cost:
	print('You can afford the boat hire')
else:
	print('You cannot afford the board hire')

# Q3

# constraint: that sells books between 1800 and 1950

user_year = int(input("What was the year the book was sold in? "))
if user_year < 1800 or user_year > 1950:
    print("Books in this shop are sold between 1800 and 1950, please check the year and enter again")

def year_century():
    # // is the floor method
    century = (user_year//100) + 1
    # as we are only dealing with the time period 1800 - 1950 the names are set otherwise this would get more complex
    if century == 19:
        num_2_string = 'Nineteenth'
        return ("{} Century").format(num_2_string)
    if century == 20:
        num_2_string = 'Twentieth'
        return ("{} Century").format(num_2_string)

def number_decade():
    decade_1 = int(str(user_year)[2:])
    decade_2 = decade_1 // 10
    # I really like this following method, do more research in reading week into the following code to see how I can\
    # manipulate further using map and test it more to become more comfortable with it
    number2decade = {'1': "Oneties", '2': "Twenties", '3': "Thirties", '4': "Forties", '5': "Fifties", '6': "Sixties",
            '7': "Seventies", '8': "Eighties", '9': "Nineties", '0': "Noughties"}
    return " ".join(map(lambda i: number2decade[i], str(decade_2)))

year_century = year_century()
number_decade = number_decade()
print(("The year the book was from {}. The century and decade: {}, {}.").format(user_year, year_century, number_decade))

'''
TASK 2 (Lists and Dictionaries)
'''

# Q1

shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])

# Q2

def user_choc_match():
    user_choc = (input("What type of chocolate do you want? ")).lower()
    chocolates = {
        'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2.00
    }
    return chocolates.get(user_choc, "Please choose from: white, milk, dark and vegan. I do not sell other types of chocolate.")

price_choc = user_choc_match()
print(price_choc)

# Q3

import random

def lottery_number():
    lottery_empty = set()
    while (len(lottery_empty)) < 7:
        num_rand = random.randint(1, 100)
        lottery_empty.add(num_rand)
    return lottery_empty

ticket_1 = tuple(lottery_number())
lottery = tuple(lottery_number())

print("The numbers for your lottery ticket are: {}".format(ticket_1))
print("The numbers for the lottery are: {}".format(lottery))

ticket_1_list = list(ticket_1)
lottery_list = list(lottery)

def ticket_lottery_compare(ticket_1_list, lottery_list):
    # practise some more with list comprehension in reading week, also go over the following code a bit more/
    # in reading week
    comparison = [i for i in ticket_1_list + lottery_list if i in ticket_1_list and i in lottery_list]
    if comparison == None:
        return 0
    frequency = int(len(comparison)/2)
    return frequency

Number_matches = ticket_lottery_compare(ticket_1_list, lottery_list)
print("The number of matches between your ticket and lottery is {}".format(Number_matches))

def lottery_prizes(Number_matches):
    if Number_matches == 3:
        return "You have won £20 for three matching numbers"
    elif Number_matches == 4:
        return "You have won £40 for four matching numbers"
    elif Number_matches == 5:
        return "You have won £100 for five matching numbers"
    elif Number_matches == 6:
        return "You have won  £10000 for six matching numbers"
    elif Number_matches == 7:
        return "You have won £1000000 for seven matching numbers"
    else:
        return "You haven't won anything, sorry! "

lottery_prizes = (lottery_prizes(Number_matches))
print(lottery_prizes)

'''
TASK 3  (Read and Write files)
'''

# Q2

# Example solution

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)

# Q3

# Q3: TASK 1

# ask Hassan if there was a way I could have automated this rather than doing this by hand

elton_lyrics = [
"\nYou could never know what it's like",
"\nYour blood like winter freezes just like ice",
"\nAnd there's a cold lonely light that shines from you",
"\nYou'll wind up like the wreck you hide behind that mask you \
use",
"\n"
"\nAnd did you think this fool could never win?",
"\nWell look at me, I'm coming back again",
"\nI got a taste of love in a simple way",
"\nAnd  if  you  need  to   know   while  I'm   still   standing,  you  just \
fade away",
"\n"
"\nDon't you know I'm still standing better than I ever did",
"\nLooking like a true survivor, feeling like a little kid",
"\nI'm still standing after all this time",
"\nPicking up the pieces of my life without you on my mind",
"\n"
"\nI'm still standing (Yeah, yeah, yeah)",
"\nI'm still standing (Yeah, yeah, yeah)",
]

with open('song.txt', 'w') as elton:
    elton.writelines(elton_lyrics)

# Q3: TASK 2

# If the file does not exist, then the 'r' and 'r+' modes will throw an error hence\
# the file has not been created successfully.
# If the file has been created successfully, i.e. the file exists, then the 'r' and 'r+'\
# modes will not throw an error and the code will run fine

file = open('song.txt', 'r')
file.close()

# Q3: TASK 3

with open('song.txt', 'r') as read_file:
# x will store the contents of read_file in a readable format
    x = read_file.read()
# z splits the file line by line into a list
    z = x.split('\n')
    empty_lyrics = []
    for line in z:
        y = line.split()
        [empty_lyrics.append(line) for word in y if word == 'still']

for i in empty_lyrics:
    print(i)

'''
TASK 4 (API)
'''

import requests
import json

pokemon_list = [1, 2, 3, 4, 5, 6]
pokemon_name = []
pokemon_moves = []

def pokemon():
    for id in pokemon_list:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id)
        response = requests.get(url)
        pokemon = response.json()
        pokemon_name.append(pokemon['name'])
        pokemon_moves.append(pokemon['moves'])
    return pokemon_name, pokemon_moves

def pokemon_dict():
    pokemon()
    pokemon_list_to_dict = {pokemon_name[i]: pokemon_moves[i] for i in range(len(pokemon_name))}
    return pokemon_list_to_dict

pokemon_dict = pokemon_dict()

with open('pokemon.txt', 'w') as pokemon_file:
    pokemon_file.write(json.dumps(pokemon_dict))


'''
Considering how large these files, it is useful to run sanity checks as my brain cannot decipher these huge files by
eye

Sanity check:
import requests
import json

pokemon_list = [1, 2, 3, 4, 5, 6]
pokemon_name = []

def pokemon_test():
    for id in pokemon_list:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id)
        response = requests.get(url)
        pokemon = response.json()
        pokemon_name.append(pokemon['name'])
    return pokemon_name

print(pokemon_test())
'''
