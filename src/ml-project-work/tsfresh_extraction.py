import pandas as pd
import glob
import features_calculation as fc
from pandas import Series
from tsfresh import extract_features
from tsfresh.utilities.distribution import MultiprocessingDistributor
Distributor = MultiprocessingDistributor(n_workers=4,
                                         disable_progressbar=False,
                                         progressbar_title="Feature Extraction")

path_files = '/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/Normal_0_slices_DE/'
all_files = glob.glob(path_files+'*_DE.csv')
list1 = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.drop('Unnamed: 0', axis=1)
    list1.append(df)
feat=[]
#for i in range(0, 20):
df1 = list1[1][['vib', 'Status']]
feat.append(extract_features(df1, column_id='Status', distributor=Distributor))

feat[0].to_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/tsfresh_features_DE_1.csv')

df_temp = pd.concat(feat)

df_temp.shape
df_temp.to_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/tsfresh_features_DE.csv', index=None)
df_temp.to_pickle('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/tsfresh_features_DE.pkl')
