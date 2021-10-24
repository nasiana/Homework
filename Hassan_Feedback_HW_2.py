'''
Variables (unless you define them as global) are scoped, so using i twice like you have is fine - they are in
different functions.
Some comments about your code:

# You're not actually using the return value of cashier_receipt_loop function - you've just declared some global
variables that you are accessing both functions. You should try and avoid globals where you can - they can lead to
hard to debug code. So instead of globals, could you return what you need from the function and use that?

# What you're doing with zip obviously works, but is there a better data structure you could such that you wouldn't
have to join two lists? Remember you have a list of labels (keys) and a value - is there a data structure you can use
instead of item_name_list and item_price_list

# Given you can, is there a way you can simplify the for loop in cashier_receipt function so you don't have to check
the length of lists, etc?
'''