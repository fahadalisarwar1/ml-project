def load_file_data(filename, col_names):
    """

    :param filename: name of the file without extension
    :param col_names: column names of the file
    :return: data-frame
    """
    import pandas as pd
    filepath = str(filename) + ".csv"
    df = pd.read_csv(filepath, names=col_names)

    return df


def add_time_stamp(df, sampling_rate):
    """

    :param df: data-frame to which time stamp is to be added
    :param sampling_rate: sampling rate of the data frame (samples per second)
    :return: data-frame with added timestamp

    """
    import numpy as np
    len_df = df.shape[0]
    time_df = len_df / sampling_rate
    time_array = np.arange(0, time_df, time_df / len_df)
    df['time'] = time_array
    return df
