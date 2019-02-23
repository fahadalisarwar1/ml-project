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
import plots.plot_mach_features as pm
import tensorflow as tf


# The first step would be loading data

# ----------- Machine data ---------

# Plot of machine types and their ages
# There are two categorical features in the data set of machine [Age of machine and Machine type]
pm.plot_mach_features(data_mach, plt)



