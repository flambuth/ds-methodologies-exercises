# As a customer analyst, I want to know who has spent the most money with us over their lifetime. I have 
# monthly charges and tenure, so I think I will be able to use those two attributes as features to estimate 
# total_charges. I need to do this within an average of $5.00 per customer.

# Create split_scale.py that will contain the functions that follow. Each scaler function should create the 
# object, fit and transform both train and test. They should return the scaler, train df scaled, test df 
# scaled. Be sure your indices represent the original indices from train/test, as those represent the indices 
# from the original dataframe. Be sure to set a random state where applicable for reproducibility!

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import wrangle_grades
import wrangle
#from wrangle import wrangle_telco as wr_telco
import env
#for some reason, when i import this, it does not work.


#Use our home-baked data cleaning function
df = wrangle_grades.wrangle_grades()

#Split up the data into a 80/20 split. Training our model with .8 of the data, and then testing the model
#on the remaining .2
#The random state dictates the randomness of how each row is assigned in this 80/20 split.
#If you use the same random state, the members of test and train will be the same
train, test = train_test_split(df, train_size = .80, random_state = 123)

#Create the scaling object that will transform our train&test data.
#This transformation will just be a scale operation, so a change in the range of the data,
#but the data will keep it's order and relation to one another. They're just widened or narrowed in range.
#This scaler object before it is assigned. The .fit() method that takes the trained data.
scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
#This operation is cramming the .fit into the assignment


#The scaler object has a method called transform that takes a DataFrame as an argument. We assign it to a 
#variable.
# train_scaled_data = scaler.transform(train)
# test_scaled_data = scaler.transform(test)
#Each one of those is a numpy array that is n_rows long. Each value is a STD-DEV score of: 


# transform train, uses the pandas dataframe constructor. The parameters look like it takes what we used to make
# 'train_scaled data', and then an argument that defines the column names
train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
# transform test, repeat process for making train_scaled, but using 'test' in the boxes to fill.
test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

########################



#Our block of data, that i had to use with the in-module funciton because mine wont work when it's imported.
#Why i dont know. I will bother me on long grey mornings as I grieve about it.
telco_data = wrangle.wrangle_telco()

#X, our predictor is all the columns except for total chages
X = telco_data.drop(columns=['customer_id', 'total_charges'])
#y, is our target variable, the total charges of each customer(row). We want to predict that based on the 
#data we have in X
y = telco_data['total_charges']
y = pd.DataFrame(y)

#Split each up into 80/20 train/test groups. They both have teh same random seed, and they each have the indexing
#from their original DataFrame, 'telco_data'.
trainX, testX = train_test_split(X, train_size = .80, random_state = 123)
trainy, testy = train_test_split(y, train_size = .80, random_state = 123)

# standard_scaler()
scalerX = StandardScaler(copy=True, with_mean=True, with_std=True).fit(trainX)
scalery = StandardScaler(copy=True, with_mean=True, with_std=True).fit(trainy)
scalerx = stand().fit()

trainX_scaled = pd.DataFrame(scalerX.transform(trainX), columns=trainX.columns.values).set_index(trainX.index.values)
testX_scaled = pd.DataFrame(scalerX.transform(testX), columns=testX.columns.values).set_index(testX.index.values)

trainy_scaled = pd.DataFrame(scalery.transform(trainy), columns=trainy.columns.values).set_index(trainy.index.values)
testy_scaled = pd.DataFrame(scalery.transform(testy), columns=testy.columns.values).set_index(testy.index.values)

# scale_inverse()
################




# uniform_scaler()
scalerX = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(trainX)
scalery = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(trainy)

trainX_scaled = pd.DataFrame(scalerX.transform(trainX), columns=trainX.columns.values).set_index([trainX.index.values])
trainy_scaled = pd.DataFrame(scalery.transform(trainy), columns=trainy.columns.values).set_index([trainy.index.values])


testy_scaled = pd.DataFrame(scaleryX.transform(testX), columns=testX.columns.values).set_index([testX.index.values])
testy_scaled = pd.DataFrame(scaleryy.transform(testy), columns=testy.columns.values).set_index([testy.index.values])


# gaussian_scaler()
scalerX = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(trainX)
scalery = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(trainy)
# apply to train
train_scaledX = pd.DataFrame(scalerX.transform(train), columns=trainX.columns.values).set_index([trainX.index.values])
train_scaledy = pd.DataFrame(scalery.transform(train), columns=trainy.columns.values).set_index([trainy.index.values])

# apply to test
test_scaledX = pd.DataFrame(scalerX.transform(test), columns=testX.columns.values).set_index([testX.index.values])
test_scaledy = pd.DataFrame(scalery.transform(test), columns=testy.columns.values).set_index([testy.index.values])


# min_max_scaler()



# iqr_robust_scaler()