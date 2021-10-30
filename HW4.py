"""
CFG Homework 4: Nasian Ahmed
"""

'''
TASK 1 (Git and GitHub)
'''

# Question 1

'''
GIT WORKFLOW FUNDAMENTALS

·        Working Directory

The working directory, synonymously known as the workspace, generally refers to the user’s project folder. When the 
user initiates the creation of a project folder locally on their computer. Provided they haven’t used any Git commands, 
and have created the project folder as they usually would do - this is just a working directory in the form of a 
project folder. It hasn’t become a repository yet.

In the working directory, each respective file can either be in one of the two possible states of being ‘tracked’ or 
‘untracked’. A file in the ‘untracked’ state is not in the staging area and thus is not in the last snapshot - git does 
not know about these files. A file in the ‘tracked’ state is a file that git is aware of and was in the last snapshot.
 

·        Staging Area

The staging area is synonymously known as the index or the cache. To make git aware of untracked files so that they can 
begin to be version controlled, they need to be added to the staging area by employment of the ‘git add’ command. The 
file is  copied from the working directory into the staging by use of the ‘git add’ command. It is commonly 
inaccurately thought that the file is moved into the staging area, this is not accurate - the file is copied into the 
staging area. This file will now be tracked by Git.

There are two types of files which are able to be added to a staging stage; modified or untracked states. 


·        Local Repo (head)

After a user has created a project folder locally on their computer, the next step is to transform this project folder 
into a repository to form a local repository. This is achieved through the employment of the ‘git init’ command. This 
command will cause the creation of a hidden folder located in the project folder named ‘.git’ - this effectively being 
the repository.

Whilst files remain in the local repository and they haven’t been synced with the remote repositories, the files are 
localised to the users machine. Git permits users to execute commands so that the repositories are clones onto the 
local machine. The location of where these copies are stored are within the local machine and so are restricted to that 
location. Until they have been synced with remote machines, other users cannot access these local repositories when 
working from foreign machines.


·        Remote repo (master)

Git permits the user to synchronize local repositories with the remote repositories. This is so other users can access 
these files and synchronize their changes with the author. 

The synchronization is achieved through the deployment of two Git commands: push and pull.

The command for the push command is ‘git push’ plus relevant. The push command is employed so that all the commits can 
be pushed from the current repository to the tracked remote repository. It is also possible that this command be 
utilized for the purposes of pushing the user’s repository to several repositories immediately. 

WORKING DIRECTORY STATES:

·        Staged

There are two types of files which are able to be added to a staging stage; modified or untracked states. When a file 
is in a staging state, it is either not present in the most recent commit or it is a ‘modified’ file that the user 
instructs git to incorporate in the next commit.

‘git add’ is utilized to add files to the staging state. 

·        Modified

A file being in the ‘modified’ state has the definition that the changes which have been made to the file have not been 
committed yet. The changes could possibly be modifying, adding or deleting the contents of the file. 

These files will be incorporated into the next commit but will be incorporated in their corresponding new state.

·        Committed

When a file is in the committed state, this has the definition that the changes made to the file have been stored in 
the Git directory  within a snapshot. The ‘git commit’ command is employed to commit the file. The consequence of this 
command is to produce a new snapshot of the Git directory and demonstrates some stats in relation to the change made.

GIT COMMANDS:

·        Git add

This command is utilized to incorporate the changes of a file into the user’s next commit.

A user creating, deleting or modifying  a file will result in changes occurring locally and will not be incorporated in 
the next commit unless explicitly done so using Git commands such as ‘git add’.

The repository is not changed by the use of the ‘git add’ command. In addition, until the ‘git commit’ command is 
utilized the changes will not be saved from solely the use of the ‘git add’ command.


·        Git commit

The ‘git commit’ command is used when the user wants to save their changes. Git commit only locally saves changes made.

A commit in Git can be understood as a snapshot of your repository represented at a particular point in time.

·        Git push

Once the user has committed the changes; Git push is the next step so that the changes can be pushed (sent) to the 
remote server. The ‘git push’ command will upload the user’s commits to the remote repository.

If the branch the user wishes to upload is newly created, there are various ways to do this but one such way is with 
‘git push <remote> <branch-name>’.

Changes must be committed for them to be uploaded by using the Git push command.

·        Git fetch

The ‘git fetch’ command is used to instruct the local git to retrieve the most recent meta-data from the original i.e. 
from a remote repository into a local repository. It is mistakenly thought that this command executes file-transferring,
however, it is actually more similar to the objective of a ‘check’ where it checks whether there are any changes 
available.

·        Git merge

The purpose of the Git merge branch is to merge the branch you have been working in with the parent branch. This 
command essentially merges the parent branch with the user’s feature branch including all of its commits. It is of 
utmost importance to remember that the user must first be on the specific branch that they wish to merge with 
their feature branch. 

The Git fetch command is executed before the Git merge command.

It’s very important that before the branches are merged that the dev branch has the latest version, or else there is a 
possibility of conflicts with data and other such undesirable issues.

The main objective of Git merge is to merge (combine) two branches. 

Merging integrates the content, retrieved from a source branch, with a target branch. The source branch history does 
not change and stays the same; it is solely the target branch which will be changed.


·        Git pull

The ‘git pull’ command instructs the local git to retrieve the most recent meta-data from the original and copy them 
into the local repository. It is different to Git fetch in that it does the same thing but additionally copies the data 
into the local repository.
'''

"""
# TASK 2 (Exception Handling)
"""

# Question 1

'''
The following code is to be executed for the purposes of the user entering the pin
'''

set_pin_code = 1998

def user_pin_string():
    user_pin = (input("Please enter you PIN code: "))
    try:
        user_pin = int(user_pin)
    except (ValueError):
        print("Your number is not an integer please try again.")
    return user_pin

first_stage = False

def pin_loop():
    i = 0
    first_stage = False
    while i < 3:
        user_pin = user_pin_string()
        i += 1
        if user_pin != set_pin_code:
            continue
        else:
            print("You have entered the correct pin!")
            first_stage = True
            break
    else:
        print("You have entered the incorrect pin more than 3 times. You are now exited from the program. However "\
              "you will be re-entered into the program to make sure you complete this and proceed to withdrawal.")
    return user_pin, first_stage


while first_stage == False:
    user_pin, first_stage = pin_loop()
else:
    print("We are proceeding on to the next step now")

    '''
    Simulation of cash withdrawal
    '''

    def withdrawal_amount_string():
        withdrawal_amount = (input("Please enter your withdrawal amount: "))
        try:
            withdrawal_amount = float(withdrawal_amount)
        # i added both ValueError and TypeError due to code later on and errors which may come as it is possible/
        # now either that either of these types may occur
        except (ValueError, TypeError):
            print("Your input is not valid please try again.")
        else:
            print("Your withdrawal amount is {}".format(withdrawal_amount))
            # I added this for myself but this is not in the CFG guidelines so don't include it, but work on this some more and manipulate in reading week
            # assert withdrawal_amount >= 0
            # try:
            #     pass
            # except AssertionError:
            #     print("The withdrawal amount has to be a value greater than or equal to 0.")
        return withdrawal_amount


    '''
    Note to Rehana/Andreea/Hassan: LOL please ignore these comments they pertain to programming i commented out, but I want to have these comments
    so my brain can understand what I did when I come back later to this code to improve it.
    
    For my code, I programmed it to perform  steps
    7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error 
    an exit the program.

    Before 

    6.       Subtract the amount from the account balance and display the remaining
    balance (NOTE! The balance cannot be negative!)

    We were told on this course to think like Software Engineers and think about the end product, well it does not really
    make much sense to perform (6) before (7). It does not make sense based on the average mathematical logic a the average
    person possesses and it just does not make sense according to the average person. 
    
    It especially does not make sense with my code as I have programmed it so that the withdrawal amount can not be less
    than 0, therefore the restrictions to put in place are 7 then 6. 

    My withdrawal amount = x, account balance = y

    Where constriction 6 can be represented as: y >= 0
    Constriction 7 is represented as: x < y

    If x is always >= 0 (due to earlier programming) , and y is already set at the positive integer value of 100.

    Therefore I should program it first so that x < y, and if y is initially set so
    y = 100 and x is initially set to be x >= 0, when you perform y - x it would follow then the condition of y >= 0 would 
    be automatically fullfilled. Regardless I programmed it anyways.
    '''

    def subtraction_account():
        account_balance = 100
        withdrawal_amount = withdrawal_amount_string()
        try:
            account_balance -= withdrawal_amount
            assert withdrawal_amount < account_balance
            assert account_balance >= 0
        except AssertionError:
            print("Assertion error: Either the withdrawal amount can not be more money then you have in your bank "\
             "account or the balance cannot be less than 0")
        else:
            print("Remaining balance: {}".format(account_balance))

    subtraction_account()

"""
TASK 3: (Testing)

Question 1:
Use the Simple ATM program to write unit tests for your functions.
You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
Try to write at least 5 unit tests in total covering various cases.

"""

# Q1

""""
I have accepted I'll get 0 marks on this question; I spent all day trouble shooting Github and I spent literally
hours (my entire day) figuring it out, so didn't have enough time to really do this.
C'est la vie
"""

def user_pin_string():
    user_pin = (input("Please enter you PIN code: "))
    try:
        user_pin = int(user_pin)
    except (ValueError):
        print("Your number is not an integer please try again.")
    return user_pin

from unittest import mock
from unittest import TestCase

class Test_user_pin_string(TestCase):
    @mock.patch(user_pin)
    def user_pin_string(self, mock_user_pin):
        user_pin = "abc"
        mock_user_pin.return_value = "abc"
        expected = AssertionError
        result = mock_user_pin
        self.assertEqual(expected, result)







