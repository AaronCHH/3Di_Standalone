
# coding: utf-8

# # Read Excel Write mdu

# <div id="toc"></div>

# ## List sheet names

# In[1]:

import pandas as pd
import sys, os

# In[ ]:

infile = sys.argv[1]
outfile = sys.argv[2]


# In[2]:

xfile = pd.ExcelFile(infile)


# In[3]:

parList = ['info', 'model', 'geometry', 
           'grid', 'initialization', 'defaults', 
           'numerics', 'physics', 'hydrology', 
           'time', 'external forcing', 
           'output', 'display', 'colors']


# In[4]:

shtList = xfile.sheet_names


# In[5]:

extraList = set(shtList).difference(set(parList))
extraList


# In[6]:

missingList = set(parList).difference(set(shtList))
missingList


# In[7]:

if len(extraList) != 0:
    print("blah")


# In[8]:

if len(extraList) == 0 and len(missingList) == 0:
    print("The number of parameter groups is correct!")
    
if len(extraList) != 0:
    print("Unknown parameter group {0} exist in the inputfile.".format(str(extraList)))

if len(missingList) != 0:
    print("Parameter group {0} missing in the inputfile.".format(str(missingList)))    


# ## Read contents

# ### Loop through sheets

# ```py
# with open('output.txt', 'wt', encoding='utf-8', newline='') as fout:
#     for sht in shtList: 
# #         print(sht)
#         df = pd.read_excel(xfile, sheetname=sht, index_col=None)
# #         print(list(df))
# 
#         if sht == "info":
#             for i in range(len(df)):    
#                 fout.write(str(df.ix[i][0]))    
#             fout.write('\n')    
#         else:
#             for i in range(len(df)):    
#                 fout.write(str(df.ix[i][0]) + ' = ' + str(df.ix[i][1]) + ' # ' + str(df.ix[i][2]) + '\n' )    
#             fout.write('\n')    
# ```

# In[9]:

with open(outfile + '.mdu', 'wt', encoding='utf-8', newline='') as fout:
    for sht in shtList: 
#         print(sht)
        df = pd.read_excel(xfile, sheetname=sht, index_col=None)
#         print(list(df))
#         print(df.columns)

        if sht == "info":
            for i in range(len(df)):    
                fout.write("# {0} {1} {2}\n".format(str(df.ix[i][0]), str(df.ix[i][1]), str(df.ix[i][2])))    
            fout.write('\n')    
        else:
            fout.write('[' + sht + ']' + '\n')    
            for i in range(len(df)):    
                if df.ix[i][0] == 1:
                    fout.write("{0:30s} = {1:45s} # {2}\n".format(str(df.ix[i][1]), 
                                                          str(df.ix[i][2]).replace('nan', ''), 
                                                          str(df.ix[i][3])).replace('nan', ''))
                else:
                    fout.write("#{0:30s} = {1:45s} # {2}\n".format(str(df.ix[i][1]), 
                                                            str(df.ix[i][2]).replace('nan', ''), 
                                                            str(df.ix[i][3])).replace('nan', ''))                    
            fout.write('\n')


# In[ ]:



