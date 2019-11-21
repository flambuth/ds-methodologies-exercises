#Nastia is better as drumAndbass, rather than her ugly techno sets

import pandas as pd

#       Define a function named get_lower_and_upper_bounds that has two arguments
#       The first argument is a pandas Series. 
#       The second argument is the multiplier, which should have a default argument of 1.5.

def get_lower_and_upper_bounds(series, multiplier=1.5):
    q1 = series.quantile(.25)
    q3 = series.quantile(.75)
    iqr = q3-q1
    upper_bounds = q3 + (iqr * multiplier)
    lower_bounds = q1 - (iqr * multiplier) 
    print(f"Any value in {series.name} above {upper_bounds} and lower than {lower_bounds} are considered outliers.")
    return upper_bounds, lower_bounds

df = pd.read_csv('lemonade.csv')

#df.Price is all the same value

####################
# 1
# Use the IQR Range Rule and the upper and lower bounds to identify the lower outliers of each 
# column of lemonade.csv, using the multiplier of 1.5. 
# Do these lower outliers make sense? Which outliers should be kept?

for i in df.select_dtypes('number'): 
    get_lower_and_upper_bounds(df[i]) 

# 2
# Use the IQR Range Rule and the upper and lower bounds to identify the upper outliers of each column of 
# lemonade.csv, using the multiplier of 1.5. Do these lower outliers make sense?Which outliers should be kept?

# 3
# Using the multiplier of 3, IQR Range Rule, and the lower and upper bounds, identify the outliers below the 
# lower bound in each colum of lemonade.csv. Do these lower outliers make sense?Which outliers should be kept?

# 4
# Using the multiplier of 3, IQR Range Rule, and the lower and upper bounds, identify the outliers above the 
# upper_bound in each colum of lemonade.csv. Do these upper outliers make sense? Which outliers should be kept?