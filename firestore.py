import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

# Replace with your Firebase project's credentials file
cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)

# Replace with the name of your Firestore collection
collection_name = "weather_data"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("modified_weatherAUS.csv")

# Create a Firestore client
db = firestore.client()

# Upload each row as a document in the Firestore collection
for index, row in df.iterrows():
    doc_id = str(row["id"])  # Use the "id" column as the document ID
    data = row.to_dict()     # Convert the row to a dictionary
    del data["id"]           # Remove the "id" key from the dictionary
    db.collection(collection_name).document(doc_id).set(data)
print("done!")