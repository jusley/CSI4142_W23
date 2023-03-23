import pandas as pd
import numpy as np

# Load CSV data into a Pandas DataFrame
df = pd.read_csv('weatherAUS.csv', parse_dates=['Date'])


# Remove columns with all missing values (NA)
df = df.dropna(axis='columns', how='all')

# Define function to replace missing numeric values with mean by location and season
def fill_numeric_mean(df, col):
    df[col] = df.groupby(['Location', pd.Grouper(key='Date', freq='3M')])[col].apply(
        lambda x: x.fillna(x.mean())).values
    return df

# Define function to replace missing categorical values with most common by location and season
def fill_categorical_mode(df, col):
    df[col] = df.groupby(['Location', pd.Grouper(key='Date', freq='3M')])[col].apply(
        lambda x: x.fillna(x.mode().iloc[0])).values
    return df

# Loop over all columns to fill missing values with mean/mode as appropriate
for col in df.columns:
    if df[col].dtype == np.number:
        df = fill_numeric_mean(df, col)
    else:
        df = fill_categorical_mode(df, col)

# Print the updated DataFrame with filled missing values
print(df)
