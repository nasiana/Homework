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

from math import floor

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
    number2decade = {'1': "Oneties", '2': "Twenties", '3': "Thirties", '4': "Forties", '5': "Fifties", '6': "Sixties",
            '7': "Seventies", '8': "Eighties", '9': "Nineties", '0': "Noughties"}
    return " ".join(map(lambda i: number2decade[i], str(decade_2)))

year_century = year_century()
number_decade = number_decade()
print(("The year book was from {}. The century and decade: {}, {}.").format(user_year, year_century, number_decade))




