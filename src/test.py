import slice_file as sf
import numpy as np
import matplotlib.pyplot as plt
import load_file as lf
import pandas as pd


DE_norm_df = lf.load_file_data('X097_DE_time', ['vib'])
DE_norm_df = lf.add_time_stamp(DE_norm_df, 12000)

fig1, (ax0, ax1) = plt.subplots(ncols=2)
ax0.plot(DE_norm_df['time'][0:1000], DE_norm_df['vib'][0:1000])
ax0.set_title('Drive End Data Normal')
ax0.set_xlabel('Time (t)')
ax0.set_ylabel('vibration ')


FE_norm_df = lf.load_file_data('X097_FE_time', ['vib'])
FE_norm_df = lf.add_time_stamp(FE_norm_df, 12000)


ax1.plot(FE_norm_df['time'][0:1000], FE_norm_df['vib'][0:1000])
ax1.set_title('Fan End Data Normal')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('vibration ')
plt.legend()
plt.show()

DE_fault_df = lf.load_file_data('X105_DE_time', ['vib'])
DE_fault_df = lf.add_time_stamp(DE_fault_df, 12000)

fig2, (ax0, ax1) = plt.subplots(nrows=2)
ax0.plot(DE_fault_df['time'][0:1000], DE_fault_df['vib'][0:1000])
ax0.set_title('Drive End Data Fault')
ax0.set_xlabel('Time (t)')
ax0.set_ylabel('vibration ')

FE_fault_df = lf.load_file_data('X105_FE_time', ['vib'])
FE_fault_df = lf.add_time_stamp(FE_fault_df, 12000)

ax1.plot(FE_fault_df['time'][0:1000], FE_fault_df['vib'][0:1000])
ax1.set_title('Fan End Data Fault')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('vibration ')
plt.legend()
plt.show()


df_BA = pd.read_csv('X118_BA_time.csv', names=['vib'])
df_BA = lf.add_time_stamp(df_BA, 12000)


Normal_0_path = '/home/fahad/DATA/DATA_CSV/12K Fault/B007_0/B007_0_slices_BA/'
list_slices = sf.to_slices(df_BA, 20)


for i in np.arange(0, len(list_slices)):
    list_slices[i].to_csv(Normal_0_path+str(i)+"X118_BA.csv")

