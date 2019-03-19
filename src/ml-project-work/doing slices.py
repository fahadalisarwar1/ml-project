import slice_file as sf
import numpy as np
import load_file as lf

path_file = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/'
df = lf.load_file_data(path_file+'DE_time', ['vib', 'Status', 'Type'])

df = lf.add_time_stamp(df, 12000)

df_path = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/IR028_0_slices_DE/'

list_slices = sf.to_slices(df, 30)

for i in np.arange(0, len(list_slices)):
    list_slices[i].to_csv(df_path+str(i+1)+"_DE_30.csv")

