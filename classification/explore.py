#'Allo. Je suis parle pur le radio de jambone.
import numpy as np
import pandas as pd
# Import visualization modules
import matplotlib.pyplot as plt
import seaborn as sns

#USE df.nunique()<5 instead of this temp list
def pick_viable_categories(df):
    discretes = df.select_dtypes(include='object')
    temp = []
    for column in discretes:
        columnSeriesObj = discretes[column]
        if len(columnSeriesObj.unique()) < 4:
            temp.append(columnSeriesObj.name)
    return temp

def plot_viable_categories(target, df):
    x = pick_viable_categories(df)
    _, ax = plt.subplots(nrows=1, ncols=len(x), figsize=(16,5))
    average_rate = df.target.mean()
    for i, feature in enumerate(x):
        sns.barplot(feature, target, data=df, ax=ax[i], alpha=.5)
        ax[i].set_ylabel('average_rate')
        ax[i].axhline(average_rate, ls='--', color='grey')

def pick_viable_regressors(df):
    regressors = df.select_dtypes(include=['float64','int64'])
    temp = []
    for column in regressors:
        columnSeriesObj = regressors[column]
        temp.append(columnSeriesObj.name)
    return temp


#Need to figure out how to make them take a nice space. Maybe keep it one column. Lots of rows.
#Some sort of figsize will need to be adjusted.
def plot_viable_regressors(target, df):
    x = pick_viable_regressors(df)
    _, ax = plt.subplots(nrows=len(x), ncols=1, figsize=(16,5))
    average_rate = df[target].mean()
    for i, feature in enumerate(x):
        sns.violinplot(feature, target, data=df, ax=ax[i], alpha=.5)
        ax[i].set_ylabel('average_rate')
        ax[i].axhline(average_rate, ls='--', color='grey')