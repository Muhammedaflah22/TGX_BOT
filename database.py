from pymongo import MongoClient
from config import DATABASE_URIS, DATABASE_NAMES, COLLECTION_NAMES

def get_db_instance(db_key):
    uri = DATABASE_URIS.get(db_key)
    db_name = DATABASE_NAMES.get(db_key)
    col_name = COLLECTION_NAMES.get(db_key)

    if not uri or not db_name or not col_name:
        raise ValueError(f"Invalid DB config for: {db_key}")

    client = MongoClient(uri)
    db = client[db_name]
    return db[col_name]