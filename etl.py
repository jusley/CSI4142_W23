import numpy as np
import pandas as pd

# Replace numerical columns with median
def replace_numerical(df):
    for col in df.select_dtypes(['int', 'float']):
        df[col] = df[col].fillna(df[col].median())
    return df

# Replace object columns with mode
def replace_object(df):
    for col in df.select_dtypes('object'):
        df[col] = df[col].fillna(method='ffill')
    return df

# Add surrogate key
def add_id(df):
    df.insert(0, 'id', range(1, 1+len(df)))
    return df

data = pd.read_csv('weatherAUS.csv')
df = data.copy()
df = add_id(df)

# Since most of the values are null, so drop Sunshine, Evaporation, Cloud9am and Cloud3pm 
col = ['Sunshine', 'Evaporation', 'Cloud9am', 'Cloud3pm']
df.drop(col, axis=1, inplace=True)


df = replace_numerical(df)
df = replace_object(df)
df.to_csv('modified_weatherAUS.csv', index=False)