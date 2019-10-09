# #howdy partners. commence the jiggling. mostly the belly.

# Acquire customer_id, monthly_charges, tenure, and total_charges from telco_churn database for all customers with a 2 year contract.

# Walk through the steps above using your new dataframe. You may handle the missing values however you feel is appropriate.

# End with a python file wrangle.py that contains the function, wrangle_telco(), that will acquire the data and return a 
# dataframe cleaned with no missing values.

import pandas as pd
import numpy as np
from env import host, user, password

#I modified this funciton to select just a few columns.
#Maybe I should make a variable with a big sophisticated SQL query that I pass as an argument to this function to modify the size
#of the dataframe I construct.
def read_sql_to_df(database, table, username=user, hostname=host, password=password):
    """Returns a dataframe that is made from the a SQL SELECT * FROM. Only thing not-defualted and needs as input is DB and table."""
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return pd.read_sql(f'SELECT customer_id, tenure, monthly_charges, total_charges FROM {table}', url)

#Make the df
data = read_sql_to_df('telco_churn','customers')
#Get rid of string values that start, end, and contain nothing but whitespaces (/s)*
data.replace(r'^\s*$', np.nan, regex=True, inplace=True)
#Make the total charges a float.
data['total_charges'] = data.total_charges.astype(float)

#Data is now just 3 columns of integers, all non-null. After this command that drops nulls and replaces that tyep with a int.
data = data.dropna().astype('int')

# def wrangle_telco(sql_query):
#     """
#     This will create a dataframe that is made from the telco_churn/customers table. Just 3 numerical columns with the customer id to index.
#     No null-values anywhere in the df.
#     """
#     import pandas as pd
#     import numpy as np
#     from env import host, user, password

#     database = 'telco_churn'
#     table = 'customers'
#     url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
#     data = pd.read_sql(f'SELECT customer_id, tenure, monthly_charges, total_charges FROM {table} WHERE contract_type = 3', url)
#     data.replace(r'^\s*$', np.nan, regex=True, inplace=True)
#     data['total_charges'] = data.total_charges.astype(float)
#     df = df.dropna()
#     return data

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
    query = f'SELECT customer_id, tenure, monthly_charges, total_charges FROM {table} WHERE contract_type_id = 3' 
    data = pd.read_sql(query, url) 
    data.replace(r'^\s*$', np.nan, regex=True, inplace=True) 
    data['total_charges'] = data.total_charges.astype(float) 
    data = data.dropna() 
    return data 

