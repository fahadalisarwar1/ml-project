import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
# import dask    # for parallel computing
# import seaborn as sns  # for graphs

# reading Data
df100 = pd.read_csv('100.tsv', sep='\t', names=['Counter', 'datetime', 'x', 'y', 'z', 'filename'])
df100 = df100.drop('filename', axis=1)  # dropping the last column which is useless

mean100 = df100.mean()                  # calculating the mean value of numerical columns of the data-frame
x100_mean = mean100.loc['x']            # separating individual means for x, y and z axis
y100_mean = mean100.loc['y']
z100_mean = mean100.loc['z']

df100['datetime'] = pd.to_datetime(df100['datetime'], unit='ms')  # conversion to datetime standard format
df100['off-time'] = 100                             # label
df100['x_rationalized'] = df100['x']-x100_mean          # normalizing values
df100['y_rationalized'] = df100['y']-y100_mean
df100['z_rationalized'] = df100['z']-z100_mean

N_100 = df100.shape[0]  # number of samples

# finding the time difference between last and first sample
time100 = df100['datetime'].iloc[N_100-1]-df100['datetime'].iloc[0]

# no comments here since the procedures are all the same as mentioned above
df200 = pd.read_csv('200.tsv', sep='\t', names=['Counter', 'datetime', 'x', 'y', 'z', 'filename'])
df200 = df200.drop('filename', axis=1)
mean200 = df200.mean()
x200_mean = mean200.loc['x']
y200_mean = mean200.loc['y']
z200_mean = mean200.loc['z']


df200['datetime'] = pd.to_datetime(df200['datetime'], unit='ms')
df200['off-time'] = 200
df200['x_rationalized'] = df200['x']-x200_mean
df200['y_rationalized'] = df200['y']-y200_mean
df200['z_rationalized'] = df200['z']-z200_mean

N_200 = df200.shape[0]  # number of samples
time200 = df200['datetime'].iloc[N_200-1]-df200['datetime'].iloc[0]


df300 = pd.read_csv('300.tsv', sep='\t', names=['Counter', 'datetime', 'x', 'y', 'z', 'filename'])
df300 = df300.drop('filename', axis=1)
mean300 = df300.mean()

x300_mean = mean300.loc['x']
y300_mean = mean300.loc['y']
z300_mean = mean300.loc['z']
df300['datetime'] = pd.to_datetime(df300['datetime'], unit='ms')
df300['off-time'] = 300
df300['x_rationalized'] = df300['x']-x300_mean
df300['y_rationalized'] = df300['y']-y300_mean
df300['z_rationalized'] = df300['z']-z300_mean

N_300 = df300.shape[0]  # number of samples
time300 = df300['datetime'].iloc[N_300-1]-df300['datetime'].iloc[0]

# --------------------------------------- DONE
# finding time duration of signals
# conversion from date time seconds to float seconds
t100 = time100.total_seconds()
t200 = time200.total_seconds()
t300 = time300.total_seconds()

# finding the sampling frequency
f100 = N_100 / t100
f200 = N_200 / t200
f300 = N_300 / t300

# finding time difference between samples
d100 = t100 / N_100         # time duration divided by number of samples
d200 = t200 / N_200
d300 = t300 / N_300

# creating time array for plots
t_array_100 = np.arange(0, t100, d100)
t_array_200 = np.arange(0, t200, d200)
t_array_300 = np.arange(0, t300, d300)


# plots here
plt.subplot(1, 3, 1)
plt.title('Z Rationalized plot')
plt.plot(t_array_100, df100['z_rationalized'])
# plt.plot(df100['datetime'], df100['z_rationalized'])
plt.ylabel('100 ms pause')
plt.ylim((-0.5, 0.4))  # setting y axis limits so graphs are aligned

plt.subplot(1, 3, 2)
plt.plot(t_array_200, df200['z_rationalized'])
plt.ylabel('200 ms pause')
plt.ylim((-0.5, 0.4))

plt.subplot(1, 3, 3)
plt.plot(t_array_300, df300['z_rationalized'])
plt.ylabel('300 ms pause')
plt.ylim((-0.5, 0.4))
plt.show()


# now features calculation
# FFT calculation




















