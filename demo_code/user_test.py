
# coding: utf-8

# In[1]:


# Imports

from passwordGen import genPassword
from IPython.display import clear_output
import random, string
import datetime
from random import shuffle
import time


# In[2]:


# Get a new user id
# Return - a user id

def getUID():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))


# In[28]:


# Globals
thisUser = getUID()


# In[4]:


def checkInput(realPassword, serviceName):
    while (True):
        print "Please enter the " + serviceName + " password now."
        password = raw_input()
        if (password == realPassword):
            logData("Passed Check Password: " + realPassword)
            logData
            break
        logData("Failed Check Password: " + realPassword)


# In[5]:


def logData(data):
    f = open("log.txt", "a+")
    f.write(str(datetime.datetime.now()) + "|" + str(thisUser) + "|" + data + "\n")
    f.close()


# In[11]:


def runQuestions():
    questions = [genPassword(), genPassword(), genPassword()]
    thisUser = getUID()

    print "This tool will generate new passwords for 3 sites.\nFor each password, you will be asked to enter each\none to verify that it is "
    print "\n"

    print "This is your password for Hooli: " + str(questions[0])
    print ""

    time.sleep(0.5)
    checkInput(questions[0], "Hooli")

    print "\n\nThis is your password for Pied Piper: " + str(questions[1])
    print ""
    checkInput(questions[1], "Pied Piper")

    print "\n\nThis is your password for Myspace: " + str(questions[2])
    print ""
    checkInput(questions[2], "Myspace")

    print "\n\nNow you will be tested on each password. Be aware\nthat the passwords may not be in the same order.\nPress enter to continue"
    wait = raw_input()

    clear_output()

    checkMemory = [
        ["Hooli", questions[0]],
        ["Pied Piper", questions[1]],
        ["Myspace", questions[2]]]

    shuffle(checkMemory)

    for question in range(3):
        for attempt in range(3):
            print "What was the password for " + checkMemory[question][0] + "? You have " + str(3 - attempt) + " attempts remaining."
            logData("Start Memory Password: " + checkMemory[question][1])
            passwordAttempt = raw_input()
            if (passwordAttempt == checkMemory[question][1]):
                print "\nThat was the correct password."
                logData("Passed Memory Password: T'" + checkMemory[question][1] + "' == F'" + passwordAttempt + "'")
                break
            logData("Failed Memory Password: T'" + checkMemory[question][1] + "' == F'" + passwordAttempt + "'")
            print "\nThat password was not correct. Try again."
            print "Press enter to continue"
            wait = raw_input()
            clear_output()
        print "Press enter to continue"
        wait = raw_input()
        clear_output()
    logData("Completed Test")
    print "You have completed the test. Thank you for your participation."


# In[ ]:


runQuestions()

