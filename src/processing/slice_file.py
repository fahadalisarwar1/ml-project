import numpy as np
import load_file as lf


def to_slices(df, nslices):
    """

    :param df:  dataframe to slice
    :param nslices: slices to be performed
    :return: list of sliced data frames
    """
    list1 = []
    length_df = df.shape[0]   # finding length of the data frame
    s_len = int(length_df / nslices)    # length of each slice
    for i in np.arange(0, length_df, s_len):
        list1.append(df[['time', 'vib', 'Status']].iloc[i + 1:i + s_len, :])          # slicing data frames

    list2 = []
    for i in range(0, nslices):         # resetting time index of each frame
        temp_df = list1[i]
        temp_df = lf.add_time_stamp(temp_df, 12000)
        temp_df = temp_df.reset_index().drop('index', axis=1)       # removing the extra column added by the reset_index
        list2.append(temp_df)
    return list2




