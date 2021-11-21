"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self):

        while True:
            item_name = input('What item do you want to enter into the cash register? ')
            item_value = input('What is the cost of the item [please write in pounds]? ')
            key = (str(item_name)).lower()
            value = float(item_value)
            self.total_items[key] = value
            self.total_price += value
            user_q = (input("Do you want to enter more items? Enter Y/N ")).lower()
            if user_q == ('Y').lower():
                continue
            else:
                break
        return self.total_items, self.total_price


    def remove_item(self):
        # To remove a key from a dictionary in Python, use the pop() method or the “del” keyword.
        while True:
            delete = (input('Please enter the name of the item you wish to delete ')).lower()
            if delete in self.total_items:
                if self.discount != 0:
                    self.total_price -= (self.discount * self.total_items[delete])
                    del self.total_items[delete]
                else:
                    self.total_price -= self.total_items[delete]
                    del self.total_items[delete]
            else:
                print("This item is not in the cash register ")
            user_q = (input("Do you want to delete more items? Enter Y/N ")).lower()
            if user_q == ('Y').lower():
                continue
            else:
                break
        return self.total_items, self.total_price, self.discount


    def apply_discount(self):
        discount = float(input('What is the discount value [please write as a decimal value e.g. 10% = 0.1]? '))
        self.discount += discount
        return self.discount

    def get_total(self):
        if self.discount != 0:
            self.total_price *= (1 - self.discount)
        return self.total_price

    def show_items(self):
        print("The receipt is as follows: {}".format(self.total_items))
        if self.discount != 0:
            print("The total price applied with the discount is: {}".format(self.total_price))
        else:
            print("The total price applied without discount is: {}".format(self.total_price))

    def reset_register(self):
        # use the .clear() method to clear the dictionary
        self.total_items.clear()
        # use the del keyword to delete Python variables
        del self.total_price
        del self.discount
        print("The cash register has been cleared.")

# EXAMPLE code run:

# ADD
c1 = CashRegister()
c1.add_item()
c1.apply_discount()
c1.get_total()
c1.show_items()
c1.remove_item()
c1.show_items()
c1.reset_register()

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
