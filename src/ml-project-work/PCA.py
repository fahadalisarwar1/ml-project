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


feat_df1 = pd.Series(dict_feat)

importance = clf.feature_importances_
import_df = pd.Series(importance)
df = pd.concat([feat_df1, import_df], axis=1)
sort_df = df.sort_values(by=[1], ascending=False)
RMS_Norm = feat_df[feat_df['FaultType'] == 'Normal_0']['RMS']
Var_Norm = feat_df[feat_df['FaultType'] == 'Normal_0']['Var']
RMS_B7 = feat_df[feat_df['FaultType'] == 'B007_0']['RMS']
Var_B7 = feat_df[feat_df['FaultType'] == 'B007_0']['Var']
RMS_B14 = feat_df[feat_df['FaultType'] == 'B014_0']['RMS']
Var_B14 = feat_df[feat_df['FaultType'] == 'B014_0']['Var']
RMS_B21 = feat_df[feat_df['FaultType'] == 'B021_0']['RMS']
Var_B21 = feat_df[feat_df['FaultType'] == 'B021_0']['Var']
RMS_B28 = feat_df[feat_df['FaultType'] == 'B028_0']['RMS']
Var_B28 = feat_df[feat_df['FaultType'] == 'B028_0']['Var']
RMS_IR7 = feat_df[feat_df['FaultType'] == 'IR007_0']['RMS']
Var_IR7 = feat_df[feat_df['FaultType'] == 'IR007_0']['Var']
RMS_IR14 = feat_df[feat_df['FaultType'] == 'IR014_0']['RMS']
Var_IR14 = feat_df[feat_df['FaultType'] == 'IR014_0']['Var']
RMS_IR21 = feat_df[feat_df['FaultType'] == 'IR021_0']['RMS']
Var_IR21 = feat_df[feat_df['FaultType'] == 'IR021_0']['Var']
RMS_IR28 = feat_df[feat_df['FaultType'] == 'IR028_0']['RMS']
Var_IR28 = feat_df[feat_df['FaultType'] == 'IR028_0']['Var']

data = ((RMS_Norm, Var_Norm), (RMS_B7, Var_B7), (RMS_B14, Var_B14), (RMS_B21, Var_B21), (RMS_B28, Var_B28),
        (RMS_IR7, Var_IR7), (RMS_IR14, Var_IR14), (RMS_IR21, Var_IR21), (RMS_IR28, Var_IR28))
colors = ("red", "green", "blue", "yellow", "orange", "black", "pink", "purple", "brown", "gray")
groups = ("Normal", "B007", "B014", "B021", "B028", "IR007", "IR014", "IR021", "IR028")
markers = ()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, c=color, edgecolors='none', label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()


plt.scatter(RMS_Norm, Var_Norm, 'ro',
            RMS_B7, Var_B7, 'bs',
            RMS_B14, Var_B14, 'go',
            RMS_B21, Var_B21, 'r-',
            RMS_B28, Var_B28, 'yo')

plt.legend()














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

