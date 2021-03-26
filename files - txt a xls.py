# importing the module
import pandas as pd
import os
path = os.path.dirname(os.path.abspath(__file__))

maxfileS = 48  # WE have to declare this to indicate the end of the final file to process
x = 1


columns = ['COL1', 'COL2', 'COL3', 'COL4'] #example

dfTmp = pd.DataFrame(columns=columns)  # VARIABLE CONTAINER

for x in range(maxfileS+1):
    print(x)
    file = path + '\\'+str(x)+'.txt'
    print('*******************'+file)
    # read specific columns of csv file using Pandas
    # the type of encoding
    # read_csv with encoding='latin1', encoding='iso-8859-1' or encoding='cp1252'
    # export data into excel file
    df = pd.read_csv(file, delimiter='|',
                     encoding='iso-8859-1', usecols=columns)
    print(df)
    if x < 1:
        df.to_csv(path+'\\result.csv', index=False,  header=True)
    else:
        df.to_csv(path+'\\result.csv', mode='a', index=False, header=None)
#dfTmp.to_excel(path+'\\result.xlsx', index=False)
