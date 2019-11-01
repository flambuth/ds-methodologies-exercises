import pandas as pd
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

def impute_mode():
    pass
