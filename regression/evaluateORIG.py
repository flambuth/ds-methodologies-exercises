#My eyes are so heavy. So, so heavy.
#Lots of imports
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.feature_selection import f_regression 
from math import sqrt
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import env
import wrangle
import split_scale

# Load the tips dataset from either pydataset or seaborn.
df = sns.load_dataset('tips')

# Fit a linear regression model (ordinary least squares) and compute yhat, predictions of tip using total_bill. 

#make a ols model object, fit it to the tips DataFrame.
def make_ols_model(y = df.tip, x = df.total_bill):
    #Woah. After review I see I was treating the wrong variable as the target.
    #Apparently I was supposed to be looking for the tip using the total bill as the predictor
    # y = df.total_bill
    # x = df.tip
    regr = ols('y ~ x', data=df).fit()
    #I could've used this one. this way allows for column names to be used as long as the data== the 
    #dataframe with the column names
    #regr = ols('tip ~ total_bill', data=df).fit()
    
    
    #use that fitted ols model's predict method on the x column . So the df made with sns.load data set
    #gets mutilated by getting a new column. The precited-y aka yhat
    df["yhat"] = regr.predict(pd.DataFrame(x))
    #Note sure if i should return the regr or leave it in here
    return regr

# Write a function, plot_residuals(x, y, dataframe) that takes the feature, the target, and the dataframe 
# as input and returns a residual plot. (hint: seaborn has an easy way to do this!)

def plot_residuals(x,y, dataframe):
    df['residual'] = df['yhat'] - df['y']
    sns.residplot(x=x, y=y, data=dataframe)

# Write a function, regression_errors(y, yhat), that takes in y and yhat, returns the sum of squared errors 
# (SSE), explained sum of squares (ESS), total sum of squares (TSS), mean squared error (MSE) and 
# root mean squared error (RMSE).
def regression_errors(y, yhat):   
    residual = y - yhat
    residual2 = residual ** 2
    SSE = residual2.sum()
    MSE = SSE/y.size
    RMSE = sqrt(MSE)
    y_mean = y.mean()
    ESS = sum((yhat - y.mean.values)**2)
    TSS = ESS + SSE
    return SSE, ESS, TSS, MSE, RMSE

#This could've been done with MSE being found first using a sklearn function
# from sklearn.metrics import mean_squared_error
# mse = mean_squared_error(y, yhat)



# Write a function, baseline_mean_errors(y), that takes in your target, y, computes the SSE, MSE & RMSE 
# when yhat is equal to the mean of all y, and returns the error values (SSE, MSE, and RMSE).

def baseline_mean_errors(y):
#The yhat in this case is the mean of the target variable. Which is the baseline for predictions. Any model
#will have to improve on that.    
    yhat = y.mean() 
    df['residual'] = yhat - df['y']
    df['residual^2'] = df.residual ** 2
    SSE = sum(df['residual^2'])
    MSE = SSE/len(df)
    RMSE = sqrt(MSE)
    ESS = sum((df.yhat - df.tip.mean())**2)
    TSS = ESS + SSE
    return SSE, ESS, RMSE

#In hindsight I should've called the function I made earlier that returns all the error terms when given 
#a predicted-y(yhat) and an actual-y(y).

# Write a function, better_than_baseline(SSE), that returns true if your model performs better than the 
# baseline, otherwise false.

def better_than_baseline(x,y):
    #This will add a column to the dataframe x and y were sliced from.
    make_ols_model(x,y)
    df['residual'] = df['yhat'] - df['y']
    df['residual^2'] = df.residual ** 2
    SSE = sum(df['residual^2'])
    ESS = sum((df.yhat - df.tip.mean())**2)
    TSS = ESS + SSE
    Rsquared = ESS/TSS
    #Now make the baselien to cmpare their rsquard scores. I'm assigned them all because it returns that many.
    base_sse, base_ess, base_rmse = baseline_mean_errors(y)
    base_tss = base_ess + base_sse
    base_Rsquared = base_ess/base_tss
    return Rsquared > base_Rsquared

    
# Write a function, model_significance(ols_model), that takes the ols model as input and returns the amount 
# of variance explained in your model, and the value telling you whether the correlation between the model 
# and the tip value are statistically significant.


def model_significance(ols_model):    

    regr = make_ols_model()
    r2 = regr.ess/regr.centered_tss
    r_pval = regr.f_pvalue

#I didnt get to it, but i know we have to make a T-TEST betwen the predicted y and the mean of y. We want to
#see a P-value below 0.05 to say that is is "siginficatly different".
# from scipy.stats import ttest_ind
# data1, data2 = this would be predicted-y and y.mean()

# stat, p = ttest_rel(data1, data2)
    pass

