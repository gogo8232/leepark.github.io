import pandas as pd
import numpy as np
import os
import re




os.chdir(r"C:\Users\Lee Sak Park\Desktop")
wiley = pd.read_csv("2019-10-06T1327_Grades-Lock,_2e.csv", encoding = "UTF-8")
row3 = wiley.iloc[4,:].notnull()
row4 = wiley.iloc[5,:].notnull()
available = list(row3 & row4)
id = wiley["ID"]

wiley = wiley.iloc[:,available]

wiley = wiley.iloc[:,wiley.columns.str.contains(r"\(")]
wiley['id'] = id

canvas = pd.read_csv("2019-12-08T1708_Grades-STA296-004.csv", encoding = "UTF-8")
names = canvas['Student']
canvas = canvas.loc[:,canvas.columns[canvas.columns.str.contains(r"Wiley", flags = re.I)]]
canvas = canvas.loc[:,canvas.columns[canvas.columns.str.contains(r"id", flags = re.I)]]

canvas.columns = ['id']

combined = pd.merge(left = canvas, right = wiley, how = "left", on = 'id')
combined.index = names
for r in range(1, (len(combined)-1)):
    cmax = combined.iloc[:,r].max()
    combined.iloc[:,r] = np.round(100*combined.iloc[:,r]/cmax,2)

combined.to_csv("result.csv")







