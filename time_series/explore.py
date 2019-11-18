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
df_daily = df2.sale_amount.resample('D').sum().reset_index()




# Plot a time series decomposition.
# Create a lag plot (day over day).
# Run a lag correlation.

# 1
# Split your data into train and test using the sklearn.model_selection.TimeSeriesSplit method.
X = df_daily.sale_date
y = df_daily.sale_amount
tss = TimeSeriesSplit(n_splits=5, max_train_size=None)

tss = TimeSeriesSplit(n_splits=5, max_train_size=None)

for train_index, test_index in tss.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

# 2
# Validate your splits by plotting X_train and y_train.
plt.plot(X_train, y_train)
plt.plot(X_test, y_test)

# 3
# Plot the weekly average & the 7-day moving average. Compare the 2 plots.

# 4
# Plot the daily difference. Observe whether usage seems to vary drastically from day to day or has more of a smooth transition.