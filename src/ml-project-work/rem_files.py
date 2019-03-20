import os


def remove_files(list_slice_folder_DE, file_name):
    for folder_name in list_slice_folder_DE:
        for i in range(1, 21):
            os.remove('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/' + folder_name + str(i)+str(file_name))
