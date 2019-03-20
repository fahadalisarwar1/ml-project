# import statements here
import slice_file as sf
import numpy as np
import load_file as lf

path_file = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/'  # path to the file to be slices
df = lf.load_file_data(path_file+'DE_time', ['vib', 'Status', 'Type'])    # filename and values to extract from the file

df = lf.add_time_stamp(df, 12000)       # adding a time stamp to the file with 12000 sampling rate

df_path = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/IR028_0_slices_DE/'  # path to store slices

list_slices = sf.to_slices(df, 30)          # number of slices here 30

for i in np.arange(0, len(list_slices)):
    list_slices[i].to_csv(df_path+str(i+1)+"_DE_30.csv")    # storing slices


