import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer
from sklearn.model_selection import train_test_split

def find_upper_outliers(column):
    '''
    Give it a Pandas Series/Column. This will return a boolean mask series of values that 
    are 1.5X above the .75 quantile
    '''
    #Using the quantile function of a Series, lower and upper side of the IQR box is defined.
    q1, q3 = column.quantile([.25, .75])
    iqr = q3 - q1
    #IQR is all the values in the box made bewteen .25-.75 of the data. The middle 50.
    
    return column[column < (q3 + 1.5*iqr)]

def find_lower_outliers(column):
    '''
    Give it a Pandas Series/Column. This will return a boolean mask series of values that 
    are 1.5X above the .75 quantile
    '''
    #Using the quantile function of a Series, lower and upper side of the IQR box is defined.
    q1, q3 = column.quantile([.25, .75])
    iqr = q3 - q1
    #IQR is all the values in the box made bewteen .25-.75 of the data. The middle 50.
    
    return column[column < (q1 - 1.5*iqr)]

#Maybe a function that will iterate through all columns of a dataframe and prunes off the outliers.
#... maybe
# def remove_outliers(df):



def make_test_train(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123)
    return X_train, X_test, y_train, y_test

# Decide how to handle the remaining missing values

# fill with constant value
# impute with mean, median, mode
# drop row/column

def impute_median(column):
    median = column.median()
    column.fillna(median, inplace=True)
    return column

def handle_missing_rows(df, row_requirement):
    """
    Should take a dataframe. This will mutate it to return a dataframe with the rows that meet the minimum
    set in the given parameter.
    """

    df['pct_cols_missing'] = df.isnull().sum(axis=1)/df.shape[1]
    df = df[df.pct_cols_missing < row_requirement]   
    return df

def handle_missing_columns(df, col_requirement):
    """
    Should take a dataframe. This will mutate it to return a dataframe with the columns that meet the minimum
    set in the given parameter.
    """
    #creates a series that has columns as index. The values are the amount of null rows.
    num_missing = df.isnull().sum()
    #The df is is df.shape[0] columns long
    rows = df.shape[0]
    #nulls in the column by the columns size
    pct_missing = num_missing/rows
    #A data frame that uses those two Series as columns.
    good_columns = pct_missing[pct_missing < col_requirement] 
    return df[good_columns.index]

def handle_missing_nulls(df,cols_req,rows_req):
    df = handle_missing_columns(df,cols_req)
    df = handle_missing_columns(df, rows_req)
    return df
