# incorrect version TASK 3 (PYTHON Q1)
chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# corrected version TASK 3 (PYTHON Q1)
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('{}'.format(message))

# corrected version 1 TASK 3 (PYTHON Q2)
Penelope = "Penelope"
my_name = Penelope
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# corrected version 2 TASK 3 (PYTHON Q2)

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# TASK 3: Q3

# x must always be set to 1
eggs = x = 1

# # #
# METHOD 1: user to vary total_o_varied and total_b_varied
# # #

# BOX: b can be varied
b = 6
o = 4
box = b * x
# set the value for number_boxes in case you want to vary x
number_boxes = box/b
print("{} is the total number of eggs in {} boxes".format(box, number_boxes))
# total_b_varied is the variable to be varied by user
total_b_varied = 10
# total_b_o calculates the omellettes that can be made from total_b_varied boxes of eggs. It does this by multiplying \
# the total_b_varied variable to be varied by the user by the box variable to calculate the total number of eggs \
# then by divided the total number of eggs by parameter o
total_b_o = ((total_b_varied) * box)/o
print("With {} boxes of eggs, you can make {} omelettes.".format(total_b_varied,total_b_o))

# Omelette: o can be varied
o = 4
b = 6
omelette = o * x
number_omelette = omelette/o
print("{} is the total number of eggs in {} omelette".format(omelette, number_omelette))
# total_o_varied is the variable to be varied by user
total_o_varied = 15
# total_o_b calculates the number of boxes used from making total_o_varied of omelettes. It does this by multiplying \
# the total_o_varied variable to be varied by the user by the omelette variable to calculate the total number of eggs \
# then by divides the total number of eggs by parameter b
total_o_b = ((total_o_varied) * omelette)/b
print("You can make {} omelettes with {} boxes of eggs.".format(total_o_varied, total_o_b))

# general statement/sanity check
omelette_box = box/o
print("You can make {} omelettes with {} boxes of eggs".format(omelette_box,number_boxes))

# # #
# METHOD 2: user to vary total_o_varied and total_b_varied
# # #

# mathematical relationships
o = 4
b = 6
relation_o = o/b
# o/b = 4/6
print("{} boxes of eggs is required to make {} omelettes.".format(relation_o, 1))
relation_b = b/o
# b/o = 6/4
print("{} omelettes can be made from {} boxes of eggs".format(relation_b, 1))

# method 2 of doing the question, user must vary total_o_varied and total_b_varied
user_boxes = relation_o * total_o_varied
print("With {} boxes of eggs, you can make {} omelettes.".format(user_boxes,total_o_varied))
user_omellettes = relation_b * total_b_varied
print("You can make {} omelettes with {} boxes of eggs.".format(user_omellettes, total_b_varied))

# TASK 3: Q4

# TASK 3: Q4: TASK 1
my_str = "I love coding."
print(my_str)

###
# METHOD 1
###

# In Python, strings are immutable therefore had to create a new copy of my_str as result
# results is a copy of my_str with the relevant substitions
result = ''
to_replace = '.'
replaced = '!'

for i in my_str:
    if i == to_replace:
        result += replaced
    else:
        result = result + i

print(result)

###
# METHOD 2
###

my_str = "I love coding."
print(my_str)
print(my_str.replace(".", "!", 1))

# TASK 3: Q4: TASK 2

my_str_1="EVERY Exercise Brings Me Closer to Completing my GOALS."
print(my_str_1)
print(my_str_1.lower())

# TASK 3: Q4: TASK 3

my_str_2 = "We enjoy travelling"

###
# METHOD 1: If statement
###

if my_str_2[0] == 'A':
        print("The string does start with A")
else:
        print("The string does not start with A")

###
# METHOD 2
###
my_str_2 = "We enjoy travelling"
print("Does the string start with A: {}".format(my_str_2.startswith('A')))

