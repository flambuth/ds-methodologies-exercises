#the first of time series exercises 
import requests
import pandas as pd

#Using the code from the lesson as a guide, create a dataframe named items that has all of the data for items.

base_url = 'https://python.zach.lol'

response = requests.get('https://python.zach.lol/api/v1/items')

data = response.json()   

pd.DataFrame.from_dict(data)