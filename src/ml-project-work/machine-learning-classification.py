import pandas as pd

Normal_DE = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/Normal_0/features_DE.csv')
B007_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B007_0/features_DE.csv')
B014_0 = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/B014_0/features_DE.csv')


df = pd.concat([Normal_DE, B007_0, B014_0])

from sklearn.svm import SVC
clf = SVC()

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred, y_test)
