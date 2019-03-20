import pandas as pd
import numpy as np
import load_file as lf
import slice_file as sf
import os
import features_calculation as fc
from pandas import Series


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
    df = lf.add_time_stamp(df, 12000)
    list_full_df.append(df)
####################################################################


slices_path = []
for i in list_slice_folder_DE:
    slices_path.append('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/'+i)

'''
for i in range(0, len(slices_path)):
    print(slices_path[i])
'''

list_all_slices = []
for i in range(0, len(list_full_df)):
    list_slices = sf.to_slices(list_full_df[i], 20)
    list_all_slices.append(list_slices)
    loc = slices_path[i]
    for j in np.arange(0, len(list_slices)):
        list_slices[j].to_csv(loc + "DE_" + str(j + 1)+".csv")

#  ---------------------------------DONE LOADING FILES AND DOING SLICES -------------------------------------
'''
for folder_name in list_slice_folder_DE:
    for i in range(1, 21):
        os.remove('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + str(i)+'DE_1.csv')
'''


# Feature Calculation
len_total_files = len(list_all_slices)
len_slice_per_file = len(list_all_slices[0])

#list_all_feat_files = []
#for k in range(0, len_total_files):
feature_list_total = []
for j in range(0, len_slice_per_file):
    feat_list_per_frame = []
    feat_list_per_frame.append(fc.cal_root_mean_sq(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_mean(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_variance(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_skewness(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_kurtosis(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_crest_factor(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_impulse_factor(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_shape_factor(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_median(list_all_slices[0][j]['vib']))
    feat_list_per_frame.append(fc.cal_range(list_all_slices[0][j]['vib']))
    ser = Series(feat_list_per_frame)
    feature_list_total.append(ser)
    # list_all_feat_files.append(feature_list_total)

df1 = pd.concat(feature_list_total, axis=1)  # make a single data frame of the features of all slices
df2 = df1.T
col_names1 = ['RMS', 'Mean', 'Var', 'Skew', 'Kurt', 'CrestFactor', 'ImpulseFactor', 'ShapeFactor', 'Median', 'Range']
# df2['FaultType'] = 'Normal_0'

df2.columns = col_names1
df2.to_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/features_DE_new2.csv', index=None)








