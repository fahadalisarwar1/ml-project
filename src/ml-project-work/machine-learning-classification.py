import matplotlib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


Normal_DE = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/features_DE_30.csv')
B007_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B007_0/features_DE_30.csv')
B014_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B014_0/features_DE_30.csv')
B021_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B021_0/features_DE_30.csv')
B028_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B028_0/features_DE_30.csv')
IR007_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR007_0/features_DE_30.csv')
IR014_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR014_0/features_DE_30.csv')
IR021_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR021_0/features_DE_30.csv')
IR028_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/IR028_0/features_DE_30.csv')


df = pd.concat([Normal_DE, B007_0, B014_0, B021_0, B028_0, IR007_0, IR014_0, IR021_0, IR028_0])
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
labels = ['Normal_DE', 'B007_0', 'B014_0', 'B021_0', 'B028_0', 'IR007_0', 'IR014_0', 'IR021_0', 'IR028_0']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


clf = KNeighborsClassifier(n_neighbors=4)
'''visualizer = ClassPredictionError(
    clf(), classes=labels
)'''

clf.fit(X_train, y_train)

#  visualizer.score(X_test, y_test)

y_pred = clf.predict(X_test)

ac = accuracy_score(y_pred, y_test)
conf_mat = confusion_matrix(y_pred, y_test)






