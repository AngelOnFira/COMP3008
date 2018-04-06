
# coding: utf-8

# In[16]:


# Imports

import csv
from dateutil import parser


# In[17]:


# Load a CSV, return a list
# In - file to open
# Return - the CSV in list format

def openCSV(filename):
    
    # Open the file
    with open(filename, 'rb') as f:
        
        # Parse the CSV
        reader = csv.reader(f)
        return list(reader)


# In[26]:


# Load log file, return a list
# Return - the log in list format

def openLog():
    
    # Open the log file
    with open('../server/log.txt', 'rb') as f:
        
        # Read the lines to a list
        lines = f.read().splitlines()
    
    # Iterate through each line
    for i, line in enumerate(lines):
        
        # Separate by pipes
        lines[i] = line.split("|")
        # Remove milliseconds from the time
        lines[i][0] = lines[i][0].split(".")[0]
    return lines


# In[20]:


# Write CSV from list
# in - the CSV file to write to
# in - the data to write

def writeCSV(filename, thisList):
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(thisList)


# In[19]:


# Make a list that will hold info about a user
# in - user id
# in - password scheme
# return - a list for a new user

def userInfo(uid, scheme):
    list = {
        "uid": uid,
        "scheme": scheme,
        "password": {
            "loginSuccess": 0,
            "loginFailure": 0,
            "loginSuccessTimes": [],
            "loginFailureTimes": []
        }
    }
    return list


# In[22]:


# Convert datetime to seconds

def dateToSeconds(date):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], str(date).split(":"))) 


# In[21]:


# Dict to list for exporting
# in - the dictionary to be converted
# return - a list of the converted dict

def dictToList(thisDict):
    returnList = []
    for key, value in thisDict.iteritems():
        successTimesAvg = 0
        failureTimesAvg = 0
        
        # Calculate the average times for success
        if (not len(value['password']['loginSuccessTimes']) == 0):
            for success in value['password']['loginSuccessTimes']:
                successTimesAvg += success
            successTimesAvg /= len(value['password']['loginSuccessTimes'])
        
        # Calculate the average times for failure
        if (not len(value['password']['loginFailureTimes']) == 0):
            for failure in value['password']['loginFailureTimes']:
                failureTimesAvg += failure
            failureTimesAvg /= len(value['password']['loginFailureTimes'])
        
        # Transform to list
        thisRow = [
            value['uid'],
            value['scheme'],
            value['password']['loginSuccess'] + value['password']['loginFailure'],
            value['password']['loginSuccess'],
            value['password']['loginFailure'],
            successTimesAvg,
            failureTimesAvg            
        ]
        
        # Append this row to the lists
        returnList.append(thisRow)
    return returnList


# In[35]:


# Parse a CSV

def parseCSV(filename):
    # Open the log
    thisCSV = openCSV('../analysis/data/' + str(filename) + '.csv')
    
    # The dictionary to hold the info
    infoDict = {}

    # Go through each line in the log
    for i, row in enumerate(thisCSV):
        
        # There is a case here at line 2197 of the input CSV.
        # There is no start for that attempt, and so we skip it.
        if row[5] == "login" and not i == 2196:
            # Create a new user if it is not already one
            if row[1] not in infoDict:
                infoDict[row[1]] = userInfo(row[1], row[3])
            
            # Find the last place that start was found.
            # This is the start of the password attempt.
            startRow = i - 1
            while (True):
                if (thisCSV[startRow][6] == "start"):
                    break
                startRow -= 1

            # Calulate the time the user took to put in the password
            timeDiff = dateToSeconds(parser.parse(row[0]) - parser.parse(thisCSV[startRow][0]))

            # Count success or failure and add time
            if row[6] == "success":
                infoDict[row[1]]['password']["loginSuccess"] += 1
                infoDict[row[1]]['password']["loginSuccessTimes"].append(timeDiff)
            elif row[6] == "failure":
                infoDict[row[1]]['password']["loginFailure"] += 1
                infoDict[row[1]]['password']["loginFailureTimes"].append(timeDiff)

    # Save the info to a CSV file
    out = sorted(dictToList(infoDict))
    writeCSV("../analysis/data/" + str(filename) + "-out.csv", out)
    
    # Print out the results
    for i in out:
        print i
    print "\n\n"


# In[32]:


# Parse a Log file

def parseLog():
    # Open the log
    thisLog = openLog()
    
    # The dictionary to hold the info
    infoDict = {}

    # Go through each line in the log
    for i, row in enumerate(thisLog):
        
        # Get the type of log message
        typeData = row[2].split(":")[0]
        
        # We only care if it is a success or failed password entry
        if typeData == "Passed Memory Password" or typeData == "Failed Memory Password":
            # Create a new user if it is not already one
            if row[1] not in infoDict:
                infoDict[row[1]] = userInfo(row[1], "2word")

            # Calulate the time the user took to put in the password
            timeDiff = dateToSeconds(parser.parse(row[0]) - parser.parse(thisLog[i - 1][0]))

            # Count success or failure and add time
            if typeData == "Passed Memory Password":
                infoDict[row[1]]['password']["loginSuccess"] += 1
                infoDict[row[1]]['password']["loginSuccessTimes"].append(timeDiff)
            elif typeData == "Failed Memory Password":
                infoDict[row[1]]['password']["loginFailure"] += 1
                infoDict[row[1]]['password']["loginFailureTimes"].append(timeDiff)

    # Save the info to a CSV file
    out = sorted(dictToList(infoDict))
    writeCSV("../analysis/data/Log-out.csv", out)
    
    # Print out the results
    for i in out:
        print i
    print "\n\n"


# In[34]:


# The main section. This will call the rest
# of the parsers, and show the output

parseCSV("Text21")
parseCSV("Imagept21")
parseLog()

