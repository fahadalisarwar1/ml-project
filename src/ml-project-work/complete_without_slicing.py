import pandas as pd
import numpy as np
import load_file as lf
import slice_file as sf
import os
import features_calculation as fc
from pandas import Series
import glob
import natsort


list_folder = ['Normal_0', 'B007_0', 'B014_0', 'B021_0', 'B028_0', 'IR007_0', 'IR014_0', 'IR021_0', 'IR028_0']
list2 = []
len_folders = len(list_folder)

for folder_name in list_folder:
    list2.append(folder_name + '/' + folder_name + '_slices_DE/')
list_slice_folder_DE = list2

DE_file_name = 'DE_time'

columns_read = ['vib', 'Status', 'Type']  # values to be read from the columns


slices_path = []
for i in list_slice_folder_DE:
    slices_path.append('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/'+i)

list_paths_all = []
for path in slices_path:
    all_files = glob.glob(path+'DE_*.csv')
    list_paths_all.append(all_files)

# sorting the loading slices. For some reason the files are loaded randomly

num_files = len(list_paths_all)
num_slices = len(list_paths_all[0])

all_files_sorted = []
for x in range(0, num_files):
    temp_list = list_paths_all[x]
    temp_list = natsort.natsorted(temp_list, reverse=False)
    all_files_sorted.append(temp_list)


list1 = []
for filename in all_files_sorted[0]:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.drop('Unnamed: 0', axis=1)
    list1.append(df)

feat_list_per_frame = []
feat_list_total = []


for x in range(0, num_slices):
    feat_list_per_frame = []
    feat_list_per_frame.append(fc.cal_root_mean_sq(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_mean(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_variance(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_skewness(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_kurtosis(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_crest_factor(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_impulse_factor(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_shape_factor(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_median(list1[x]['vib']))
    feat_list_per_frame.append(fc.cal_range(list1[x]['vib']))
    ser = Series(feat_list_per_frame)
    feat_list_total.append(ser)


import pandas as pd

df1 = pd.concat(feat_list_total, axis=1)  # make a single data frame of the features of all slices
df2 = df1.T
col_names = ['RMS', 'Mean', 'Var', 'Skew', 'Kurt', 'CrestFactor', 'ImpulseFactor', 'ShapeFactor', 'Median', 'Range']
df2.columns = col_names

df2['FaultType'] = 'Normal'       # add label to the type of fault

# store calculated features of the slices
df2.to_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/features_DE_new2.csv', index=None)














