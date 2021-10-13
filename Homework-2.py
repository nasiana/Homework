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

# BOX: b can be varied
b = 6
o = 4
box = b * x
number_boxes = box/b
print("{} is the total number of eggs in {} boxes".format(box, number_boxes))
# total_b_varied is the variable to be varied by user
total_b_varied = 10
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
total_o_b = ((total_o_varied) * omelette)/b
print("You can make {} omelettes with {} boxes of eggs.".format(total_o_varied, total_o_b))

# general statement/sanity check
omelette_box = box/o
print("You can make {} omelettes with {} boxes of eggs".format(omelette_box,number_boxes))

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