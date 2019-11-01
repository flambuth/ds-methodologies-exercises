import pandas as pd
import env

# Acquire data from mySQL using the python module to connect and query. You will want to end with a single 
# dataframe. Make sure to include: the logerror, all fields related to the properties that are available. 
# You will end up using all the tables in the database.

# Be sure to do the correct join. 

#   only include properties with a transaction in 2017, and include only the last transaction for each 
#   properity (so no duplicate property id's), along with zestimate error and date of transaction.

#   only include properties that include a latitude and longitude value

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_bite():
    query = '''
    SELECT prop.*, pred.logerror, pred.transactiondate
    FROM predictions_2017 AS pred
    LEFT JOIN properties_2017 AS prop  USING(parcelid)
    WHERE (bedroomcnt > 0 AND bathroomcnt > 0 AND calculatedfinishedsquarefeet > 500 AND latitude IS NOT NULL AND longitude IS NOT NULL) 
    AND (unitcnt = 1 OR unitcnt IS NULL)
    ;
    '''
    df = pd.read_sql(query, get_connection('zillow'))
    # df.sort_values(by='transactiondate', ascending=False)
    # df.drop_duplicates(subset ="parcelid", keep = 'first', inplace = True) 
    return df

def get_zillow_chunk():
    query = '''
    SELECT prop.*, pred.logerror, pred.transactiondate
    FROM predictions_2017 AS pred
    LEFT JOIN properties_2017 AS prop  USING(parcelid)
    WHERE (latitude IS NOT NULL AND longitude IS NOT NULL) 
    ;
    '''
    df = pd.read_sql(query, get_connection('zillow'))
    df.sort_values(by='transactiondate', ascending=False)
    df.drop_duplicates(subset ="parcelid", keep = 'first', inplace = True) 
    return df