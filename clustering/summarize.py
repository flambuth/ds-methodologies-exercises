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

def nulls_by_row(df):
    #Makes a series with same index as df. The values are the summed nulls in each row.
    num_cols_missing = df.isnull().sum(axis=1)
    #df.shape[1] is the width, the amount of columns. So nulls/columns is the null percentage
    pct_cols_missing = df.isnull().sum(axis=1)/df.shape[1]*100
    #Makes a dataframe that has the previous Series as columns.
    rows_missing = pd.DataFrame({'num_cols_missing': num_cols_missing, 'pct_cols_missing': pct_cols_missing}).reset_index().groupby(['num_cols_missing','pct_cols_missing']).count().rename(index=str, columns={'index': 'num_rows'}).reset_index()
    return rows_missing

def df_value_counts(df):
    counts = pd.Series([])
    for i, col in enumerate(df.columns.values):
        if df[col].dtype == 'object':
            col_count = df[col].value_counts()
        else:
            col_count = df[col].value_counts(bins=10, sort=False)
        counts = counts.append(col_count)
    return counts



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