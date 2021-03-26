from art import *
import os
import pandas as pd
cwd = os.path.dirname(os.path.abspath(__file__)) + "\\"
files = os.listdir(cwd)

# show title ascii
titlex = text2art("xcodered")
print(titlex)

print("********Listing all excel files in the folder***********************")
print("********Only the first sheet*********************** \n")
print("Checking---------->path: " + cwd)

# check all files xls
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(cwd + file), ignore_index=True)
        print("-Combining Data XLSX " + file + "***")
    elif file.endswith('.xls'):
        df = df.append(pd.read_html(cwd + file), ignore_index=True)
        print("-Combining Data HTML " + file + "***")
df.head()
print(" \nWriting new file......")
df.to_excel(cwd + 'result.xlsx')
print(" \nDone!")
