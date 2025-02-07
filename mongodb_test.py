import pymongo
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Check connection
try:
    client = pymongo.MongoClient(MONGO_DB_URL)
    db = client["KNAcadeny"]
    collection = db["NetworkData"]
    
    # Fetch some records
    data = list(collection.find().limit(5))
    print(f"Sample Data from MongoDB: {data}")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
