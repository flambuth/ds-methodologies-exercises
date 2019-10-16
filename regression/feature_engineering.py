#Roll out the barrell. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, RFECV
import warnings
warnings.filterwarnings("ignore")

import env
import wrangle
import split_scale

import statsmodels.api as sm

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

#Backwards elimination notes:
# 1     Select a significance level, say 5% (0.05)
# 2     Fit a model with all features (variables)
# 3     Consider the feature with the highest P-Value. If its P-value is greater than significance 
#       level (P > SL), go to step 4. Else, your model is ready.
# 4     Eliminate this feature (variable).
# 5     Fit a model with the new set of features, and go to step 3.


#Every step is a model is being 1Instantiated, 2Fitted, 3Transformed. The p-values after each 1-2-3
#is tested to see if its above 0.05 and worthy of being a not-cut feature
#Ordinary Least Squares is the ML Algorithm we are testing on each iteration

def ols_backwards_elimination(X_train, y_train):
    train, test = split_scale.split_my_data(grades_data)
    scaler, train, test = split_scale.standard_scaler(train, test)
    X_train = train.drop(columns='final_grade')
    y_train = train[['final_grade']]
    X_test = test.drop(columns='final_grade')
    y_test = test[['final_grade']]
    cols = list(X_train.columns)
    pmax = 1
    while (len(cols)>0):
        p= []
        X_1 = X_train[cols]
        X_1 = sm.add_constant(X_1)
        model = sm.OLS(y_train,X_1).fit()    
    #Looks like p is an array with each value being hte pvalue of each row.
    #Apparently model objects have a pvalues attribute
        p = pd.Series(model.pvalues.values[1:],index = cols)
    #Of those pvalues in that series, pmax is the one with the highest p-value. That's the first feature to go!
        pmax = max(p)
        feature_with_p_max = p.idxmax()
    #This will iterate through until there is only features that havea p-value above 0.05
        if(pmax>0.05):
            cols.remove(feature_with_p_max)
        else:
    #Once there are no p-values that are larger than 0.05, the loop breaks and we're left with cols that made the cut
            break

    selected_features_BE = cols
    print(selected_features_BE)


#4
# Write a function, lasso_cv_coef() that takes X_train and y_train as input and returns the coefficients 
# for each feature, along with a plot of the features and their weights.

def lasso_cv_coef():
    from sklearn.linear_model import LassoCV

    reg = LassoCV()
    reg.fit(X_train, y_train)

    print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
    print("Best score using built-in LassoCV: %f" %reg.score(X_train,y_train))
    coef = pd.Series(reg.coef_, index = X_train.columns)


    print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")
        
    pass

#5
# Write three functions

#the first computes the number of optimum features (n) using rfe

#Gonna need REFCV
def find_optimum_with_rfe(model, X, y):
    # Create recursive feature eliminator that scores features by mean squared errors
    rfecv = RFECV(estimator=ols, step=1, scoring='neg_mean_squared_error')
    #Transforming data using RFE
    fit = rfe.fit(X,y)  
    rfecv.fit(X, y)
    rfecv.transform(X)
    return rfecv.n_features_
#This might be too lazy, cuz i ran this on some other data. It said use 8 of 9 features. I'd believe it. Maybe.

# the second takes n as input and returns the top n features, 
def find_top_n_features(model, n, X, y):
    rfe = RFE(model, n)

    #Transforming data using RFE
    selected_features = rfe.fit(X,y) 
    return selected_features.ranking_
#This returns the ranking array. I need to match up the 1s to their column name and returns that

# third takes the list of the top n features as input and returns a new X_train and X_test dataframe with 
# those top features , recursive_feature_elimination() 
# that computes the optimum number of features (n) and returns the top n features.

#Looks like i'll just call the two previous functions and display them in a new format.
def the_third_function():
    pass