#Le jambon c'est un viande bonne
import numpy as np
import pandas as pd
# Import visualization modules
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

import acquire

# Iris Data

# Use the function defined in acquire.py to load the iris data.
df_iris = acquire.get_iris_data()

# Drop the species_id and measurement_id columns.
df_iris.drop(['species_id','measurement_id'],inplace=True,axis=1)

# Rename the species_name column to just species.
df_iris = df_iris.rename(columns={"species_name": "species"})

# Encode the species name using a sklearn label encoder. 
# Research the inverse_transform method of the label encoder. How might this be useful?
labelencoder = LabelEncoder()
labelencoder.fit(df_iris.species)
df_iris.species = labelencoder.transform(df_iris.species)

# Create a function named prep_iris that accepts the untransformed iris data, and returns 
# the data with the transformations above applied.

def prep_iris():
    df_iris = acquire.get_iris_data()
    df_iris.drop(['species_id','measurement_id'],inplace=True,axis=1)
    df_iris = df_iris.rename(columns={"species_name": "species"})

    labelencoder = LabelEncoder()
    labelencoder.fit(df_iris.species)
    df_iris.species = labelencoder.transform(df_iris.species)
    return df_iris


# Titanic Data

# Use the function you defined in acquire.py to load the titanic data set.
df_titanic = acquire.get_titanic_data()

# Handle the missing values in the embark_town and embarked columns.
# Remove the deck column.
# Use a label encoder to transform the embarked column.
# Scale the age and fare columns using a min max scaler. Why might this be beneficial? When might you not want to do this?
# Create a function named prep_titanic that accepts the untransformed titanic data, and returns the data with the transformations above applied.