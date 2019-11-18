# # data manipulation 
import numpy as np
import pandas as pd

# from datetime import datetime
import itertools

# # data visualization 
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from sklearn.model_selection import TimeSeriesSplit

import prepare

sales = pd.read_csv('sales.csv')
items = pd.read_csv('items.csv')
stores = pd.read_csv('stores.csv')

merged_df = pd.merge(sales, stores, how='inner', left_on = 'store', right_on = 'store_id')
df_final = pd.merge(merged_df, items, how='inner', left_on = 'item', right_on = 'item_id')
df2 = prepare.prep_store_data(df_final)


# 1
# Split your data into train and test using the sklearn.model_selection.TimeSeriesSplit method.
df_daily = df2.sale_amount.resample('D').sum().reset_index()
X = df_daily.sale_date
y = df_daily.sale_amount
tss = TimeSeriesSplit(n_splits=5, max_train_size=None)

for train_index, test_index in tss.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


# 2
# Validate your splits by plotting X_train and y_train.
plt.plot(X_train, y_train)
plt.plot(X_test, y_test)

# 2.X
#Using a 2016/2017 split for train and test. Getting the daily average as the time unit.
aggregation = 'sum'
train = df_final[:'2016'].sale_amount.resample('D').agg(aggregation)
test = df_final['2017':].sale_amount.resample('D').agg(aggregation)

# 3
# Plot the weekly average & the 7-day moving average. Compare the 2 plots.
# The weekly average
train.resample('W').mean().plot(figsize=(12, 4))
plt.show()
# The 7 day rolling average
train.rolling(7).mean().plot(figsize=(12, 4))
plt.show()

# 4
# Plot the daily difference. Observe whether usage seems to vary drastically from day to day or has more of a smooth transition.
train.diff(periods=1).plot(figsize=(12,4))

# 5
# Plot a time series decomposition.
decomp = sm.tsa.seasonal_decompose(train.resample('W').mean(), model='additive')

# 6
# Create a lag plot (day over day).
pd.plotting.lag_plot(train.resample('D').mean(), lag=1)

# 7
# Run a lag correlation.
df_corr = pd.concat([train.shift(1), train], axis=1)
df_corr.corr()