# coding: utf-8
import os,sys
import pandas as pd
import glob

# ## Read files into list
xlsxlist = list()
for file in glob.glob("*.xlsx"):
    xlsxlist.append(file)

# ## Using pd.concat()
df = pd.DataFrame()
for file in xlsxlist:
    data = pd.read_excel(file)
    df = pd.concat([df, data], axis = 1)

df.to_excel('out.xlsx', index = False)