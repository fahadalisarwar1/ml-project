import pandas as pd
import numpy as np
import load_file as lf
import slice_file as sf
import os


list_folder = ['Normal_0', 'B007_0', 'B014_0', 'B021_0', 'B028_0', 'IR007_0', 'IR014_0', 'IR021_0', 'IR028_0']
list_slice_folder_DE = ['Normal_0/Normal_0_slices_DE/',
                        'B007_0/B007_0_slices_DE/',
                        'B014_0/B014_0_slices_DE/',
                        'B021_0/B021_0_slices_DE/',
                        'B028_0/B028_0_slices_DE/',
                        'IR007_0/IR007_0_slices_DE/',
                        'IR014_0/IR014_0_slices_DE/',
                        'IR021_0/IR021_0_slices_DE/',
                        'IR028_0/IR028_0_slices_DE/']

list_slice_folder_FE = ['Normal_0/Normal_0_slices_FE/',
                        'B007_0/B007_0_slices_FE/',
                        'B014_0/B014_0_slices_FE/',
                        'B021_0/B021_0_slices_FE/',
                        'B028_0/B028_0_slices_FE/',
                        'IR007_0/IR007_0_slices_FE/',
                        'IR014_0/IR014_0_slices_FE/',
                        'IR021_0/IR021_0_slices_FE/',
                        'IR028_0/IR028_0_slices_FE/']

list_slice_folder_BA = ['Normal_0/Normal_0_slices_BA',
                        'B007_0/B007_0_slices_BA',
                        'B014_0/B014_0_slices_BA',
                        'B021_0/B021_0_slices_BA',
                        'B028_0/B028_0_slices_BA',
                        'IR007_0/IR007_0_slices_BA',
                        'IR014_0/IR014_0_slices_BA',
                        'IR021_0/IR021_0_slices_BA',
                        'IR028_0/IR028_0_slices_BA']
DE_file_name = 'DE_time'
FE_file_name = 'FE_time'


columns_read = ['vib', 'Status', 'Type']  # values to be read from the columns


####################################################################
list_full_df = []
# Reading main files to a list of data frames
for folder_name in list_folder:
    # path to the file to be slices
    path_file = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + '/'

    # print(path_file)
    df = lf.load_file_data(path_file + DE_file_name, columns_read)
    df = df = lf.add_time_stamp(df, 12000)
    list_full_df.append(df)
####################################################################


slices_path = []
for i in list_slice_folder_DE:
    slices_path.append('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/'+i)


for i in range(0, len(slices_path)):
    print(slices_path[i])

for i in range(0, len(list_full_df)):
    list_slices = sf.to_slices(list_full_df[i], 20)
    loc = slices_path[i]
    for j in np.arange(0, len(list_slices)):
        list_slices[j].to_csv(loc + str(j + 1) + "_DE_20.csv")

#  ---------------------------------DONE LOADING FILES AND DOING SLICES

















file_name = '_DE_30.csv'
for folder_name in list_slice_folder_DE:
    for i in range(0, 21):
        os.remove('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + str(i+1)+'_DE_30.csv')


for i in range(0, 20):
    os.remove('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/IR028_0_slices_DE/' + str(i+1)+'_DE_30.csv')
