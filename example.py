import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")

# Load data from CSV file
df = pd.read_csv('modified_weatherAUS.csv')

# Select features and target
features = ['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustDir', 'WindGustSpeed', 
            'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 
            'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm', 'RainToday',
            'AvgTemp', 'AvgWind', 'AvgRainfall', 'AvgHumidity', 'AvgPressure']
target = 'RainTomorrow'
X = df[features]
y = df[target]

# Convert categorical features to numerical using LabelEncoder
categorical_features = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']
encoders = {}
for feature in categorical_features:
    encoders[feature] = LabelEncoder()
    X[feature] = encoders[feature].fit_transform(X[feature])

# Scale numeric features using StandardScaler
scaler = StandardScaler()
numeric_features = list(set(features) - set(categorical_features))
X[numeric_features] = scaler.fit_transform(X[numeric_features])

# Train random forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X, y)

#11
weather_today_1 = pd.DataFrame({
    'Location': ['Albury'],
    'MinTemp': [9.7],
    'MaxTemp': [31.9],
    'Rainfall': [0.0],
    'WindGustDir': ['NNW'],
    'WindGustSpeed': [80.0],
    'WindDir9am': ['SE'],
    'WindDir3pm': ['NW'],
    'WindSpeed9am': [7.0],
    'WindSpeed3pm': [28.0],
    'Humidity9am': [42.0],
    'Humidity3pm': [9.0],
    'Pressure9am': [1008.9],
    'Pressure3pm': [1003.6],
    'Temp9am': [18.3],
    'Temp3pm': [30.2],
    'RainToday': ['No'],
    'AvgTemp': [20.799999999999997],
    'AvgWind': [38.333333333333336],
    'AvgRainfall': [0.0],
    'AvgHumidity': [25.5],
    'AvgPressure': [1006.25]
})

#10
weather_today_2 = pd.DataFrame({
'Location': ['Albury'],
'MinTemp': [13.1],
'MaxTemp': [30.1],
'Rainfall': [1.4],
'WindGustDir': ['W'],
'WindGustSpeed': [28.0],
'WindDir9am': ['S'],
'WindDir3pm': ['SSE'],
'WindSpeed9am': [15.0],
'WindSpeed3pm': [11.0],
'Humidity9am': [58.0],
'Humidity3pm': [27.0],
'Pressure9am': [1007.0],
'Pressure3pm': [1005.7],
'Temp9am': [20.1],
'Temp3pm': [28.2],
'RainToday': ['Yes'],
'AvgTemp': [21.6],
'AvgWind': [14.0],
'AvgRainfall': [1.4],
'AvgHumidity': [42.5],
'AvgPressure': [1006.35]
})

# Dummy weather data for today
weather_today_3 = pd.DataFrame({
    'Location': ['Sydney'],  # dummy data from Sydney, Australia
    'MinTemp': [18.0],
    'MaxTemp': [25.0],
    'Rainfall': [0.0],
    'WindGustDir': ['NW'],
    'WindGustSpeed': [20.0],
    'WindDir9am': ['NW'],
    'WindDir3pm': ['W'],
    'WindSpeed9am': [10.0],
    'WindSpeed3pm': [15.0],
    'Humidity9am': [60.0],
    'Humidity3pm': [45.0],
    'Pressure9am': [1015.0],
    'Pressure3pm': [1012.0],
    'Temp9am': [22.0],
    'Temp3pm': [23.0],
    'RainToday': ['No'],
    'AvgTemp': [21.5],
    'AvgWind': [12.5],
    'AvgRainfall': [2.0],
    'AvgHumidity': [55.0],
    'AvgPressure': [1013.0]
})

weather_today = weather_today_1
# Convert categorical features to numerical using LabelEncoder
for feature in categorical_features:
    weather_today[feature] = encoders[feature].transform(weather_today[feature])

# Scale numeric features using StandardScaler
weather_today[numeric_features] = scaler.transform(weather_today[numeric_features])

# Make prediction for today's weather
prediction = rf_model.predict(weather_today)[0]

# Print prediction
if prediction == 'Yes':
    print('It will rain tomorrow.')
else:
    print('It will not rain tomorrow.')
