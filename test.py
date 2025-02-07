import pandas as pd
import pymongo

def fetch_data_from_mongo():
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.tifrq.mongodb.net/KNAcadeny?retryWrites=true&w=majority")
    db = client["KNAcadeny"]
    collection = db["NetworkData"]

    data = list(collection.find({}))  # Fetch all documents
    dataframe = pd.DataFrame(data)

    return dataframe


df = fetch_data_from_mongo()
print(df.shape)  # Should print (22110, columns)
print(df.head()) # Check the first few rows

train_set, test_set = train_test_split(dataframe, test_size=0.2, random_state=42)
print("DataFrame shape before splitting:", dataframe.shape)
