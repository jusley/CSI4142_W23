import numpy as np
import pandas as pd

# Replace numerical columns with median and add new columns for mean temperature, wind, rainfall, humidity, pressure, and cloud
def replace_numerical(df):
    numerical_cols = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']
    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())
    df['AvgTemp'] = (df['MinTemp'] + df['MaxTemp'] + df['Temp9am'] + df['Temp3pm']) / 4
    df['AvgWind'] = (df['WindGustSpeed'] + df['WindSpeed9am'] + df['WindSpeed3pm']) / 3
    df['AvgRainfall'] = df[['Rainfall', 'RainToday']].mean(axis=1)
    df['AvgHumidity'] = (df['Humidity9am'] + df['Humidity3pm']) / 2
    df['AvgPressure'] = (df['Pressure9am'] + df['Pressure3pm']) / 2
    if 'Cloud9am' in df.columns and 'Cloud3pm' in df.columns:
        df['AvgCloud'] = (df['Cloud9am'] + df['Cloud3pm']) / 2
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