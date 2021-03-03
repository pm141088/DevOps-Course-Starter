import os
import pymongo


def get_db_collection():
    dbClientUri = f"mongodb+srv://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@cluster0.vslql.mongodb.net/database?retryWrites=true&w=majority"
    databaseName = os.getenv('MONGO_DB_DATABASE_NAME')
    collectionName = 'collection'

    dbClient = pymongo.MongoClient(dbClientUri)
    db = dbClient[databaseName]
    return db[collectionName]