import pandas as pd
import glob
import matplotlib.pyplot as plt
import features_calculation as fc
from pandas import Series

path_files = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B014_0/B014_0_slices_FE/'
all_files = glob.glob(path_files+'*_FE.csv')
list1 = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.drop('Unnamed: 0', axis=1)
    list1.append(df)

'''
for i in range(1, 21):
    plt.subplot(4, 5, i)
    plt.plot(list1[i-1]['time'], list1[i-1]['vib'])
    plt.xlabel('time')
    plt.ylabel('vibration')
    plt.ylim(-0.5, 0.5)
    # plt.savefig('normal_0_plots.svg')
'''

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

df1 = pd.concat(feat_list_total, axis=1)
df2 = df1.T
col_names = ['RMS', 'Mean', 'Var', 'Skew', 'Kurt', 'CrestFactor', 'ImpulseFactor', 'ShapeFactor', 'Median', 'Range']
df2.columns = col_names

df2['FaultType'] = 'B014'

df2.to_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B014_0/features_FE.csv', index=None)



