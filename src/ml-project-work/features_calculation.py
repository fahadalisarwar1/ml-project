import math


def cal_root_mean_sq(ser):
    """

    :param ser: pandas series for which RMS is to be calculated
    :return: RMS value of series in float.
    """
    len_of_series = ser.shape[0]
    sqr_of_value = ser**2
    total_sum = sqr_of_value.sum()
    temp = total_sum / len_of_series
    root_mean_sq = math.sqrt(temp)
    return root_mean_sq


def cal_mean(ser):
    """

    :param ser: Pandas series
    :return: mean of the series
    """
    len_of_series = ser.shape[0]
    sum_series = ser.sum()
    mean = sum_series / len_of_series
    return mean


def power(my_list, pow1):
    """

    :param my_list: list whose power is to be calculated
    :param pow1: power to be calculated
    :return: list raised to the power
    """
    return [x**pow1 for x in my_list]


def cal_variance(ser):
    """

    :param ser: Pandas series
    :return: variance of the series in float.
    """
    var = ser.var()
    '''mean = cal_mean(ser)
    delta = []
    len_series = ser.shape[0]
    for i in range(1, len_series):
        delta.append(ser[i]-mean)
    delta = power(delta, 2)
    sum_delta = sum(delta)
    var = sum_delta / len_series'''
    return var


def cal_skewness(ser):
    """

    :param ser: pandas series for which we want to calculate skewness
    :return: skewness of the series
    """
    mean = cal_mean(ser)
    var = cal_variance(ser)
    std_dev = math.sqrt(var)
    list1 = []
    len_series = ser.shape[0]
    for i in range(1, len_series):
        list1.append((ser[i]-mean) / std_dev)
    list2 = power(list1, 3)
    res = sum(list2)
    skew = res / len_series
    return skew


def cal_kurtosis(ser):
    """

        :param ser: pandas series for which we want to calculate Kurtosis
        :return: Kurtosis of the series
        """
    '''
    mean = cal_mean(ser)
    var = cal_variance(ser)
    std_dev = math.sqrt(var)
    list1 = []
    len_series = ser.shape[0]
    for i in range(0, len_series):
        list1.append((ser[i] - mean) / std_dev)
    list2 = power(list1, 4)
    res = sum(list2)
    kurtosis = res / len_series
    '''

    return ser.kurtosis()


def cal_impulse_factor(ser):
    """

    :param ser: Series for which we want to calculate the impulse factor
    :return: Impulse factor
    """
    max_ser = ser.abs().max()
    len_ser = ser.shape[0]
    abs_ser = ser.abs()
    summation = abs_ser.sum()
    den = summation / len_ser
    impulse_factor = max_ser / den
    return impulse_factor


def cal_crest_factor(ser):
    """

        :param ser: Series for which we want to calculate the Crest factor
        :return: Crest factor
    """
    max1 = ser.abs().max()
    rms = cal_root_mean_sq(ser)
    crest_factor = max1 / rms
    return crest_factor


def cal_shape_factor(ser):
    """
        :param ser: Series for which we want to calculate the Shape factor
        :return: Shape factor
    """
    rms = cal_root_mean_sq(ser)
    len_ser = ser.shape[0]
    abs_ser = ser.abs()
    summation = abs_ser.sum()
    den = summation / len_ser
    sh_fac = rms / den
    return sh_fac


def cal_median(ser):
    """

    :param ser: Series for which we want to calculate the median
    :return: median of the series
    """
    med = ser.median()
    return med


def cal_range(ser):
    """

    :param ser: Series for which we want to calculate the range
    :return: range of the series
    """
    ran = ser.max() - ser.min()
    return ran


def cal_spectral_flatness():
    ''' TODO '''




