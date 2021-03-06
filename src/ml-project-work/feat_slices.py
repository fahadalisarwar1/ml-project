# file to determine features of the slices
# import slices
import pandas as pd
import glob
import features_calculation as fc
from pandas import Series
import natsort
# load all the slices of the file available
path_files = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/Normal_0_slices_DE/'
all_files = glob.glob(path_files+'DE_*.csv')  # path to slices

all_files_sorted = natsort.natsorted(all_files, reverse=False)
# Create a list of data frames of slices
list1 = []
for filename in all_files_sorted:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.drop('Unnamed: 0', axis=1)
    list1.append(df)

# plot of slices
'''
for i in range(1, 21):
    plt.subplot(4, 5, i)
    plt.plot(list1[i-1]['time'], list1[i-1]['vib'])
    plt.xlabel('time')
    plt.ylabel('vibration')
    plt.ylim(-0.5, 0.5)
    # plt.savefig('normal_0_plots.svg')
'''

# features calculation
# there are 10 features that we calculate from this data
feat_list_per_frame = []
feat_list_total = []

for x in range(0, len(list1)):
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



