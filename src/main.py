########################################################################################################################

'''
VERSION: 1.1.1
AUTHOR: Fahad Ali SARWAR
Email: fahadalisarwar@gmail.com

'''
########################################################################################################################

# imports
from preparation.load_mach_data import *
from preparation.load_sensor_data import *
from preparation.load_mach_fail import *
from preparation.load_error_data import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# The first step would be loading data

# ----------- Machine data ---------

# Plot of machine types and their ages
# There are two categorical features in the data set of machine [Age of machine and Machine type]

categorical_features = ["model", "age"]
fig, ax = plt.subplots(1, len(categorical_features))
for i, categorical_feature in enumerate(data_mach[categorical_features]):
    data_mach[categorical_feature].value_counts().plot("bar", ax=ax[i]).set_title(categorical_feature)
fig.show()


