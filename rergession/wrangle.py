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
    return pd.read_sql(f'SELECT customer_id, tenure, monthly_charges, total_charges, churn FROM {table}', url)

#
data = read_sql_to_df('telco_churn','customers')