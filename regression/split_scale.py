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
#from wrangle import wrangle_telco as wr_telco
import env
#for some reason, when i import this, it does not work.
def wrangle_telco(): 
    """ 
    This will create a dataframe that is made from the telco_churn/customers table. Just 3 numerical columns with the customer id to index. 
    No null-values anywhere in the df. 
    """ 
    import pandas as pd 
    import numpy as np 
    from env import host, user, password
    database = 'telco_churn' 
    table = 'customers' 
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    query = f'SELECT * FROM {table} WHERE contract_type_id = 3' 
    data = pd.read_sql(query, url) 
    data.replace(r'^\s*$', np.nan, regex=True, inplace=True) 
    data['total_charges'] = data.total_charges.astype(float) 
    data = data.dropna() 
    return data 

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
train_scaled_data = scaler.transform(train)
test_scaled_data = scaler.transform(test)
#Each one of those is a numpy array that is n_rows long. Each value is a STD-DEV score of: 


# transform train, uses the pandas dataframe constructor. The parameters look like it takes what we used to make
# 'train_scaled data', and then an argument that defines the column names
train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
# transform test, repeat process for making train_scaled, but using 'test' in the boxes to fill.
test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

########################



#Our block of data, that i had to use with the in-module funciton because mine wont work when it's imported.
#Why i dont know. I will bother me on long grey mornings as I grieve about it.
telco_data = wrangle_telco()

#X, our predictor is all the columns except for total chages
X = telco_data.drop(columns=['customer_id', 'total_charges'])
#y, is our target variable, the total charges of each customer(row). We want to predict that based on the 
#data we have in X
y = telco_data['total_charges']

#Split each up into 80/20 train/test groups. They both have teh same random seed, and they each have the indexing
#from their original DataFrame, 'telco_data'.
trainX, testX, trainy, testy = train_test_split(df, train_size = .80, random_state = 123)

