import pandas as pd
import numpy as np
import os
import re

# It needs to ask the users to have the files ready in their desktop folders
print("please save the gradebook files from wileyplus and canvas in your desktop folder (it is not working for mac's)")

# We need to get the file names for both gradebooks
wiley_file = input("Enter the file name of wileyplus gradebook:")
canvas_file = input("Enter the file name of the uky canvas gradebook:")

# If the user did not write the file names with .csv, then we do it
if wiley_file[-4] != ".csv":
    wiley_file = wiley_file + ".csv"
if canvas_file[-4] != ".csv":
    canvas_file = canvas_file + ".csv"


# We automatically setup the wokring directory to the desktop
os.chdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

# Create pandas dataframe for wileyplus gradebook
wiley = pd.read_csv(wiley_file, encoding = "UTF-8")
# if the third and fourth persons have their grades, we do not drop them
# otherwise, empty columns will be dropped out
row3 = wiley.iloc[4,:].notnull()
row4 = wiley.iloc[5,:].notnull()
available = list(row3 & row4)

#Here, we save the wileyplus ID coulumns, because we need to use them later
id = wiley["ID"]

# deleting the columns empty columns
wiley = wiley.iloc[:,available]

# We also drop columns with column names not containing parenthesis

# It is because, only the columns with parenthesis are for the grades for individual assignments

wiley = wiley.iloc[:,wiley.columns.str.contains(r"\(")]

# During the deleting process, we lost the id column, so we should restore it.

wiley['id'] = id


# Now, import the canvas gradebook
canvas = pd.read_csv(canvas_file, encoding = "UTF-8")

# names is the student names
names = canvas['Student']

# We are only interested in the wiley plus id numbers in the canvas gradebook
canvas = canvas.loc[:,canvas.columns[canvas.columns.str.contains(r"Wiley", flags = re.I)]]
canvas = canvas.loc[:,canvas.columns[canvas.columns.str.contains(r"id", flags = re.I)]]

# set-up the column name as 'id'
canvas.columns = ['id']

# now merge the two datasets by id existing in the canvas
combined = pd.merge(left = canvas, right = wiley, how = "left", on = 'id')

# index for the combined dataframe is the student names
combined.index = names

# we are going to convert the grades into percentage * 100
for r in range(1, (len(combined.columns)-1)):
    cmax = np.max(wiley[combined.iloc[:,r].name])
    combined.iloc[:,r] = np.round(100*combined.iloc[:,r]/cmax,2)






# write it into csv
combined.to_csv("result.csv")







