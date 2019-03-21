import numpy as np
import load_file as lf
import slice_file as sf

# --------------------------------FOLDER NAMES GO HERE ---------------------------------------------------------------
list_folder = ['Normal_0', 'B007_0', 'B014_0',
               'B021_0', 'B028_0', 'IR007_0',
               'IR014_0', 'IR021_0', 'IR028_0']

list2 = []
for folder_name in list_folder:
    list2.append(folder_name + '/' + folder_name + '_slices_DE/')
list_slice_folder_DE = list2


DE_file_name = 'DE_time'
columns_read = ['vib', 'Status', 'Type']  # values to be read from the columns

# -------------------------------READING FILES AND ADDING TIME STAMP --------------------------------------------------
# Reading main files to a list of data frames
list_full_df = []
for folder_name in list_folder:
    # path to the file to be sliced

    path_file = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + '/'
    df = lf.load_file_data(path_file + DE_file_name, columns_read)
    df = df = lf.add_time_stamp(df, 12000)  # Adding Time Stamp with 12000 Hz Sampling Rate
    list_full_df.append(df)


slices_path = []
for i in list_slice_folder_DE:
    slices_path.append('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/'+i)


# --------------------------------DOING SLICES HERE -------------------------------------------------------
list_all_slices = []
for i in range(0, len(list_full_df)):
    list_slices = sf.to_slices(list_full_df[i], 20)
    list_all_slices.append(list_slices)
    loc = slices_path[i]
    for j in np.arange(0, len(list_slices)):
        list_slices[j].to_csv(loc + "DE_" + str(j + 1)+".csv")

#  ---------------------------------DONE LOADING FILES AND DOING SLICES -------------------------------------






