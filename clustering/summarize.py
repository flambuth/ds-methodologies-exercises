import pandas as pd

def nulls_by_col(df):
    #creates a series that has columns as index. The values are the amount of null rows.
    num_missing = df.isnull().sum()
    #The df is is df.shape[0] columns long
    rows = df.shape[0]
    #nulls in the column by the columns size
    pct_missing = num_missing/rows
    #A data frame that uses those two Series as columns.
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'pct_rows_missing': pct_missing})
    return cols_missing

# 3
# Write a function that takes in a dataframe of observations and attributes and returns a df where each row is an atttribute name, 
# the first column is the number of rows with missing values for that attribute, and the second column is percent of total rows that 
# have missing values for that attribute. Run the function and document takeaways from this on how you want to handle missing values.

def nulls_by_row(df):
    #Makes a series with same index as df. The values are the summed nulls in each row.
    num_cols_missing = df.isnull().sum(axis=1)
    #df.shape[1] is the width, the amount of columns. So nulls/columns is the null percentage
    pct_cols_missing = df.isnull().sum(axis=1)/df.shape[1]*100
    #Makes a dataframe that has the previous Series as columns.
    row_missing = pd.DataFrame()
    row_missing['pct_cols_missing'] = pct_cols_missing 
    row_missing['num_cols_missing'] = num_cols_missing 
    # rows_missing = pd.DataFrame({'num_cols_missing': num_cols_missing, 'pct_cols_missing': pct_cols_missing}).reset_index().groupby(['num_cols_missing','pct_cols_missing']).count().rename(index=str, columns={'index': 'num_rows'}).reset_index()
    return row_missing

def df_value_counts(df):
    counts = pd.Series([])
    for i, col in enumerate(df.columns.values):
        if df[col].dtype == 'object':
            col_count = df[col].value_counts()
        else:
            col_count = df[col].value_counts(bins=10, sort=False)
        counts = counts.append(col_count)
    return counts

# 2
# Summarize your data (summary stats, info, dtypes, shape, distributions, value_counts, etc.)


def df_summary(df):
    print('--- Shape: {}'.format(df.shape))
    print('--- Info')
    df.info()
    print('--- Descriptions')
    print(df.describe(include='all'))
    print('--- Nulls By Column')
    print(nulls_by_col(df))
    print('--- Nulls By Row')
    print(nulls_by_row(df))
    print('--- Value Counts')
    print(df_value_counts(df))

# create a function that will drop rows or columns based on the percent of values that are missing: 
# handle_missing_values(df, prop_required_column, prop_required_row).

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
