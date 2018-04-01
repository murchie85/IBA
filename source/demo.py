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


# iterate through avaialble account files

# ======================== populate array
#initialize iterators
# PARSE FILES TO ARRAY

a = 0
b = 0
currentRow = 0


for a in range(0, len(availableAccounts)):
	with open(str(directory) + str(availableAccounts[a]) + ".csv", 'rU') as f:

		currentRow = [] 
		for line in f:  # iterate through stored 
			print(line)
