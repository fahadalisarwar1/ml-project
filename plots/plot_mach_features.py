# Function to plot the histogram of machine features
def plot_mach_features(df_mach, plt):
    """
This function plots the histogram of machine age and model
    :param df_mach: data frame of machine data
    :param plt: matplotlib.pyplot object should be passed here
    """
    categorical_features = ["model", "age"]
    fig, ax = plt.subplots(1, len(categorical_features))
    for i, categorical_feature in enumerate(df_mach[categorical_features]):
        df_mach[categorical_feature].value_counts().plot("bar", ax=ax[i]).set_title(categorical_feature)
    fig.show()







