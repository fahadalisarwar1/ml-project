import os

# -----------------------------------------CODE TO REMOVE FILES
list_folder = ['Normal_0', 'B007_0', 'B014_0',
               'B021_0', 'B028_0', 'IR007_0',
               'IR014_0', 'IR021_0', 'IR028_0']

list2 = []
for folder_name in list_folder:
    list2.append(folder_name + '/' + folder_name + '_slices_DE/')
list_slice_folder_DE = list2

file_name = '_DE.csv'

for folder_name in list_slice_folder_DE:
    for i in range(1, 21):
        os.remove('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + str(i)+str(file_name))
