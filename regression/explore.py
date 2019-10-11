#exploring the depths of Powershell blue
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
warnings.filterwarnings("ignore")

import env
import wrangle
import split_scale

#1
# Write a function, plot_variable_pairs(dataframe) that plots all of the pairwise 
# relationships along with the regression line for each pair.

def plot_variable_pairs(dataframe):
    train, test = split_scale.split_my_data(dataframe)
    g = sns.PairGrid(train)
    g.map_diag(plt.hist)
    g.map_offdiag(plt.scatter);

#2
#Write a function, months_to_years(tenure_months, df) that returns your dataframe 
#with a new feature tenure_years, in complete years as a customer.

def months_to_years(tenure_months, df):
    df['tenure_years'] = df.tenure/12
    df['tenure_years'] = df.tenure_years.astype('category')
    return df
#3
# Write a function, plot_categorical_and_continous_vars(categorical_var, continuous_var, 
# df), that outputs 3 different plots for plotting a categorical variable with a 
# continuous variable, e.g. tenure_years with total_charges. For ideas on effective 
# ways to visualize categorical with continuous: https://datavizcatalogue.com/. You 
# can then look into seaborn and matplotlib documentation for ways to create plots.

def plot_categorical_and_continous_vars(categorical_var, continuous_var):
    plt.figure(figsize=(8,6))
    sns.heatmap(train.corr(), cmap='Blues', annot=True)
    plt.ylim(0, 4)
    sns.catplot(x='tenure_years', y='monthly_charges', data=train);
#############
wrangle.wrangle_telco()