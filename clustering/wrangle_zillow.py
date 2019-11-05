#Use acquire and summarize to pump out a 'wrangled' zillow dataframe
# Wrangling
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# Exploring
import scipy.stats as stats

# Visualizing
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from sklearn.model_selection import learning_curve
# %matplotlib inline

import acquire
import summarize
import prepare

df = acquire.get_real_zillow_singles()

wrangled_df = prepare.handle_missing_columns(df, .5)
wrangled_df = prepare.handle_missing_rows(df, .4)
