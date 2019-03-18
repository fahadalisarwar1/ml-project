import load_file as lf
import features_calculation as fc


path_file = '/home/fahad/DATA/WorkingData/B021_0/'
df = lf.load_file_data(path_file+'X222_FE_time', ['vib', 'Status'])
df = lf.add_time_stamp(df, 12000)


f1_mean = fc.cal_mean(df['vib'])
f2_rms = fc.cal_root_mean_sq(df['vib'])
f3_var = fc.cal_variance(df['vib'])
f4_skew = fc.cal_skewness(df['vib'])
f5_kur = fc.cal_kurtosis(df['vib'])
f6_imp_fac = fc.cal_impulse_factor(df['vib'])
f7_shap_fac = fc.cal_shape_factor(df['vib'])
f8_med = fc.cal_median(df['vib'])
f9_range = fc.cal_range(df['vib'])
ser = df['vib']
ser.mean()
