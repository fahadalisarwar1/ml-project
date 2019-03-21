import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from yellowbrick.classifier import ClassPredictionError
from yellowbrick.classifier import ROCAUC
import matplotlib.pyplot as plt

feat_df = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/features_new.csv')

# Separating inputs and outputs
X = feat_df.iloc[:, :-1].values
y = feat_df.iloc[:, -1].values
pca = PCA(n_components=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = ExtraTreesClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(clf.feature_importances_)
dict_feat = {0: 'RMS', 1: 'Mean', 2: 'Var', 3: 'Skew', 4: 'Kurt',
             5: ' CrestFactor', 6: 'ImpulseFactor', 7: 'ShapeFactor',
             8: 'Median', 9: 'Range'}


feat_df = pd.Series(dict_feat)

importance = clf.feature_importances_
import_df = pd.Series(importance)
df = pd.concat([feat_df, import_df], axis=1)
sort_df = df.sort_values(by=[1], ascending=False)

plt.bar(sort_df[0], sort_df[1])
plt.title("Feature Importance VS feature")
plt.xticks(rotation=70)
plt.savefig('/home/fahad/DATA/ML-project/ml-project/Plots/Feature_imp_with_Ext_Tree_classifier.png')


# --------------------------------FOLDER NAMES GO HERE ---------------------------------------------------------------
classes = ['Normal_0', 'B007_0', 'B014_0',
           'B021_0', 'B028_0', 'IR007_0',
           'IR014_0', 'IR021_0', 'IR028_0']



visualizer = ROCAUC(clf, classes=classes)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof('/home/fahad/DATA/ML-project/ml-project/Plots/DE_plots/ROC_with_NaiveBayes_Gaussian.png')             # Draw/show/poof the data















visualizer = ClassPredictionError(
    clf, classes=classes
)

# clf.fit(X_train, y_train)
# print(clf.feature_importances_)
visualizer.fit(X_train, y_train)
visualizer.score(X_test, y_test)

# Draw visualization
g = visualizer.poof()

y_pred = clf.predict(X_test)
acc = accuracy_score(y_pred, y_test)

from yellowbrick.features import ParallelCoordinates

visualizer = ParallelCoordinates()
visualizer.fit_transform(X_train, y_train)
visualizer.poof()

