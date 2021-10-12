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
box = b * x
total_boxes = box/b
print("{} is the total number of eggs in {} boxes".format(box, total_boxes))

# Omelette: o can be varied
o = 4
omelette = o * x
total_omelette = omelette/o
print("{} is the total number of eggs in {} omelette".format(omelette, total_omelette))

# final
omelette_box = box/o
print("You can make {} omelettes with {} boxes of eggs".format(omelette_box,total_boxes))


