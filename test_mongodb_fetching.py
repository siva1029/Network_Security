def export_collection_as_dataframe(self):
    try:
        database_name = self.data_ingestion_config.database_name
        collection_name = self.data_ingestion_config.collection_name
        
        self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
        collection = self.mongo_client[database_name][collection_name]
        
        # Fetch data
        data = list(collection.find())
        
        # Debugging: Print sample data
        print(f"Retrieved {len(data)} records from MongoDB")
        
        df = pd.DataFrame(data)
        
        if df.empty:
            raise ValueError("MongoDB collection is empty. Check database connection and collection name.")
        
        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)
        return df
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
