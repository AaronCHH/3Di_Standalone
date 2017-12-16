# coding: utf-8
import os, sys
import numpy as np
import pandas as pd

# read filenames
infile = sys.argv[1]
outfile = sys.argv[2]
print('read ' + infile)

# read ras.xlsx file
# ras = pd.read_excel('ras.xlsx', header=None)
ras = pd.read_excel(infile, header=None)

# write to file
with open(outfile + '.asc','w') as f:
    f.write('{0:14s}{1:14s}\n'.format('nrows', str(ras.shape[0])))
    f.write('{0:14s}{1:14s}\n'.format('ncols', str(ras.shape[1])))
    f.write('{0:14s}{1:14s}\n'.format('xllcorner', '302559.5'))
    f.write('{0:14s}{1:14s}\n'.format('yllcorner', '2766869.5'))
    f.write('{0:14s}{1:14s}\n'.format('cellsize', '1'))
    f.write('{0:14s}{1:14s}\n'.format('NODATA_value', '-9999'))
    f.write(ras.to_csv(sep=' ', index=False, header=False))  

# confirm results
print('Create raster done!')
os.system('pause')