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


