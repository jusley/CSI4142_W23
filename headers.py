import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('weatherAUS.csv')

# Clean and preprocess the data
data = data.dropna()  # remove rows with missing values
data['Date'] = pd.to_datetime(data['Date'])  # convert Date column to datetime format
data = data.set_index('Date')  # set Date column as index
data = data[['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity', 'WindGustSpeed']]  # extract relevant features

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('MaxTemp', axis=1), data['MaxTemp'], test_size=0.2, random_state=0)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model's performance
score = model.score(X_test, y_test)
print(f"R^2 score: {score:.2f}")

# Predict tomorrow's weather
today = pd.DataFrame({'MinTemp': [13.4], 'MaxTemp': [22.9], 'Rainfall': [0.6], 'Humidity': [44], 'WindGustSpeed': [44]})
tomorrow = model.predict(today)
print(f"Tomorrow's MaxTemp: {tomorrow[0]:.1f}")

