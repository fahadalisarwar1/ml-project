# Naive Bayes Classifier

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/features_new.csv')

# Separating inputs and outputs
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# classifier
clf = GaussianNB()

# splitting data into train and test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
ac = accuracy_score(y_pred, y_test)
conf_mat = confusion_matrix(y_pred, y_test)


y_test_df = pd.DataFrame(y_test)



