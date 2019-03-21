import pandas as pd
import glob
import matplotlib.pyplot as plt
from tsfresh import extract_features


path_files = '/home/fahad/DATA/WorkingData/B007_0/B007_0_slices_DE/'
all_files = glob.glob(path_files+'*_X118_DE.csv')
list1 = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.drop('Unnamed: 0')
    list1.append(df)


frame = pd.concat(list1[0:2], axis=0).drop('Unnamed: 0', axis=1)

plt.plot(list1[0]['time'], list1[0]['vib'])

len1 = frame.shape[0]


extd_features = extract_features(list1[0][['time', 'vib', 'Status']], column_id='Status', column_sort='time')

df_1 = list1[0]
len1 = df_1.shape[0]
vib_sq = df_1['vib']**2
tot_sum = vib_sq.sum()
qw  = tot_sum/len1


