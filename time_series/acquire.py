#the first of time series exercises 
import requests
import pandas as pd

#Using the code from the lesson as a guide, create a dataframe named items that has all of the data for items.

base_url = 'https://python.zach.lol'


# items_url = requests.get('https://python.zach.lol/api/v1/items')
# items_data = items_url.json()
# items = pd.DataFrame(items_data['payload']['items'])

# #going through the 'next pages' to get 20 items per page
# response = requests.get(base_url + items_data['payload']['next_page'])
# data = response.json()
# items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index()

# response = requests.get(base_url + items_data['payload']['next_page'])
# data = response.json()
# items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index()
# #Items is now a 60 row deep data frame. but with some weird columns


def get_items_df():
    response = requests.get(base_url + "/api/v1/items?page=1")
    data = response.json()
    items_df = pd.DataFrame(data['payload']['items'])
    
    total_pages = data['payload']['max_page']

    for i in range(2, total_pages+1): 
        response = requests.get(base_url + f"/api/v1/items?page={i}")
        data = response.json()
        items_df = pd.concat([items_df, pd.DataFrame(data['payload']['items'])])
    
    return items_df.reset_index()

# STORES
# 

def get_stores_df():
    stores_url = requests.get('https://python.zach.lol/api/v1/stores')
    stores_data = stores_url.json() 
    stores_df = pd.DataFrame(stores_data['payload']['stores'])
    return stores_df

#####
#SALES
# This comes out to 183. So we'll need to concat 183 times
# data['payload']['max_page']

def get_sales():
    response = requests.get(base_url + "/api/v1/sales?page=1")
    data = response.json()
    sales_df = pd.DataFrame(data['payload']['sales'])
    
    total_pages = data['payload']['max_page']

    for i in range(2, total_pages+1): 
        response = requests.get(base_url + f"/api/v1/sales?page={i}")
        data = response.json()
        sales_df = pd.concat([sales_df, pd.DataFrame(data['payload']['sales'])])
        
    return sales_df.reset_index()

def save_sales_as_csv():
    blob = get_sales()
    export_csv = blob.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/sales.csv', index = None, header=True)

def save_stores_as_csv():
    blob = get_stores_df()
    export_csv = blob.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/stores.csv', index = None, header=True)


