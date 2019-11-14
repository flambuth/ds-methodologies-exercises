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
    """
    This funnction returns a Dataframe that is the sum of items (located at /api/v1/items...) on each page given by the api.
      The first dataframe is made by created a json object from the first page.
      The max pages is collected on the first page and sets the amount of iterations in the for loop.
      Each Iteration of the loop creates a JSON object from the next page and concats the rows onto the Dataframe created in the first step
      The Dataframe has its index reset when returned, giving it a fresh 0-n index.
    """
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
    """
    This funnction returns a Dataframe that is the sum of stores (located at /api/v1/items...) on each page given by the api.
      The dataframe is made by created a json object from the only page.
      There is only one page of items, so no iteration through pages is required.
    """
    stores_url = requests.get('https://python.zach.lol/api/v1/stores')
    stores_data = stores_url.json() 
    stores_df = pd.DataFrame(stores_data['payload']['stores'])
    return stores_df

#####
#SALES
# This comes out to 183. So we'll need to concat 183 times
# data['payload']['max_page']

def get_sales():
    """
    WARNING! THIS WILL TAKE AT LEAST 5 MINUTES TO EXECUTE
    This funnction returns a Dataframe that is the sum of SALES (located at /api/v1/items...) on each page given by the api.
      The first dataframe is made by created a json object from the first page.
      The max pages is collected on the first page and sets the amount of iterations in the for loop.
      Each Iteration of the loop creates a JSON object from the next page and concats the rows onto the Dataframe created in the first step
      The Dataframe has its index reset when returned, giving it a fresh 0-n index.
    """
    response = requests.get(base_url + "/api/v1/sales?page=1")
    data = response.json()
    sales_df = pd.DataFrame(data['payload']['sales'])
    
    total_pages = data['payload']['max_page']

    for i in range(2, total_pages+1): 
        print(f"Retrieving sales from page {i}")
        response = requests.get(base_url + f"/api/v1/sales?page={i}")
        data = response.json()
        sales_df = pd.concat([sales_df, pd.DataFrame(data['payload']['sales'])])
        
    return sales_df.reset_index()

def save_sales_as_csv():
    """
    Function calls the function that creates a Dataframe of the SALES in the web api.
    The dataframe made at the end of that function is transformed into a CSV located in my Mac user's home directory.
    """
    blob = get_sales()
    export_csv = blob.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/sales.csv', index = None, header=True)

def save_stores_as_csv():
    """
    Function calls the function that creates a Dataframe of the STORES in the web api.
    The dataframe made at the end of that function is transformed into a CSV located in my Mac user's home directory.
    """
    blob = get_stores_df()
    export_csv = blob.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/stores.csv', index = None, header=True)

def save_items_as_csv():
    """
    Function calls the function that creates a Dataframe of the ITEMS in the web api.
    The dataframe made at the end of that function is transformed into a CSV located in my Mac user's home directory.
    """
    blob = get_items_df()
    export_csv = blob.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/items.csv', index = None, header=True)

def merge_dataframes():
    """
    WARNING! WILL TAKE AT LEAST 5 MINUTES TO EXCECUTE
    Calls every API requisition function and makes an inner join on them. Essentially it appends item and store data to the very very
    long SALES dataframe.
    """
    sales = get_sales()
    items = get_items_df()
    stores = get_stores_df()
    merged_df = pd.merge(sales, stores, how='inner', left_on = 'store', right_on = 'store_id')
    merged_df2 = pd.merge(merged_df, items, how='inner', left_on = 'item', right_on = 'item_id')
    return merged_df2

# merged_df = pd.merge(sales, stores, how='inner', left_on = 'store', right_on = 'store_id')

# export_csv = merged_df2.to_csv (r'/Users/fredricklambuth/codeup-data-science/ds-methodologies-exercises/time_series/merged.csv', index = None, header=True)
