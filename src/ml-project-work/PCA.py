import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

feat_df = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/features_new.csv')
pca = PCA(n_components=3)
# Separating inputs and outputs
X = feat_df.iloc[:, :-1].values
y = feat_df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)











