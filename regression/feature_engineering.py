#Roll out the barrell. 
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


# Our scenario continues:
# As a customer analyst, I want to know who has spent the most money with us over their lifetime. I 
# have monthly charges and tenure, so I think I will be able to use those two attributes as features 
# to estimate total_charges. I need to do this within an average of $5.00 per customer.

#1
# Write a function, select_kbest_chisquared() that takes X_train, y_train and k as input (X_train and 
# y_train should not be scaled!) and returns a list of the top k features.

def select_kbest_chisquared(X_train, y_train, k_features):
    chi_selector = SelectKBest(chi2, k=k_features)
    chi_selector.fit(X_train, y_train)
    chi_support = chi_selector.get_support()
    chi_feature = X.loc[:,chi_support].columns.tolist()
    return chi_feature

#2
# Write a function, select_kbest_freg() that takes X_train, y_train (scaled) and k as input and returns 
# a list of the top k features.

def select_kbest_freg(X_train, y_train, k_features):
    f_selector = SelectKBest(f_regression, k=k_features)
    f_selector.fit(X_train, y_train)
    f_support = f_selector.get_support()
    f_feature = X.loc[:,f_support].columns.tolist()
    return f_feature

#3
# Write a function, ols_backware_elimination() that takes X_train and y_train (scaled) as input and 
# returns selected features based on the ols backwards elimination method.
def ols_backware_elimination():
    pass

#4
# Write a function, lasso_cv_coef() that takes X_train and y_train as input and returns the coefficients 
# for each feature, along with a plot of the features and their weights.

def lasso_cv_coef():
    pass

#5
# Write 3 functions

#the first computes the number of optimum features (n) using rfe
def find_optimum_with_rfe():
    pass

# the second takes n as input and returns the top n features, 
def find_top_n_features():
    pass

# third takes the list of the top n features as input and returns a new X_train and X_test dataframe with 
# those top features , recursive_feature_elimination() 
# that computes the optimum number of features (n) and returns the top n features.

def the_third_function():
    pass