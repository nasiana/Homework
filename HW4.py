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

There are two types of files which are able to be added to a staging stage; modified or untracked states. When a file 
is in a staging state, it is either not present in the most recent commit or it is a ‘modified’ file that the user 
instructs git to incorporate in the next commit.


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
'''