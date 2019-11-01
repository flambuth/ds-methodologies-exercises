def find_upper_outliers(column):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the
    series.

    The values returned will be either 0 (if the point is not an outlier), or a
    number that indicates how far away from the upper bound the observation is.
    '''
    #Using the quantile function of a Series, lower and upper side of the IQR box is defined.
    q1, q3 = column.quantile([.25, .75])
    #IQR is all the values in the box made bewteen .25-.75 of the data. The middle 50.
    iqr = q3 - q1
    
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x - upper_bound, 0]))

def find_upper_outliers(column):
    '''
    Give it a Pandas Series/Column. This will return the values that are 1.5X above the .75 quantile
    '''
    #Using the quantile function of a Series, lower and upper side of the IQR box is defined.
    q1, q3 = column.quantile([.25, .75])
    #IQR is all the values in the box made bewteen .25-.75 of the data. The middle 50.
    
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x - upper_bound, 0]))

def add_upper_outlier_columns(df, k):
    '''
    Give it a Pandas Series/Column. This will return the values that are 1.5X below the .25 quantile

    '''
    # outlier_cols = {col + '_outliers': get_upper_outliers(df[col], k)
    #                 for col in df.select_dtypes('number')}
    # return df.assign(**outlier_cols)

    for col in df.select_dtypes('number'):
        df[col + '_outliers'] = get_upper_outliers(df[col], k)

    return df