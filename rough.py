from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME, COLLECTION_NAME
from pymongo.errors import ServerSelectionTimeoutError
import pandas as pd

try:
    # Step 1: Connect to MongoDB
    client = MongoDBClient(database_name=DATABASE_NAME)
    print(f"✅ Connected to DB: {DATABASE_NAME}")

    # Step 2: Get collection
    collection = client.database[COLLECTION_NAME]
    print(f"✅ Accessing Collection: {COLLECTION_NAME}")

    # Step 3: Count documents
    count = collection.count_documents({})
    print(f"📦 Total documents in collection: {count}")

    if count == 0:
        print("⚠️ Collection is empty. Please check the MongoDB source.")
    else:
        # Step 4: Preview first few documents
        docs = list(collection.find().limit(5))
        print("🔍 Sample Documents:")
        for doc in docs:
            print(doc)

        # Step 5: Convert to DataFrame
        df = pd.DataFrame(docs)
        print(f"\n✅ DataFrame shape: {df.shape}")
        print(f"\n📄 Columns: {df.columns.tolist()}")
        print("\n🧾 Head of DataFrame:")
        print(df.head())

except ServerSelectionTimeoutError as timeout_err:
    print("❌ Could not connect to MongoDB. Check internet/connection string.")
    print(timeout_err)

except Exception as e:
    print("❌ Unexpected error occurred.")
    print(e)
