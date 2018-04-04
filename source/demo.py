# ======================== Python dependencies
import json
import pandas
import datetime
import os
import statistics
import numpy as np



print("Pulling data from storage......")




# ======================== collate to array
directory = "../../IBA-DATA/data/"
availableAccounts = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print(os.path.join(directory, filename))
        AccountFile = filename[:-4]
        availableAccounts.append(AccountFile)
        continue
    else:
        continue


print('The available files are ' + str(availableAccounts))



# ======================== Iterate through files and populate array
#initialize iterators
# PARSE FILES TO ARRAY

a = 0

currentRow = 0
accountArray = []


for a in range(0, len(availableAccounts)):
    print("The current Account Being processed is " + str(availableAccounts[a]))
    with open(str(directory) + str(availableAccounts[a]) + ".csv", 'rU') as f:
        currentRow = []
        for line in f:
            words = line.split(",")
            print(line)
            myarray = np.asarray(words)
            currentRow.append(myarray)
        accountArray.append(np.asarray(currentRow))


# ======================== main process



fileNumber = 0

for fileNumber in range(0, len(accountArray)):
    print(accountArray[fileNumber][3:])
