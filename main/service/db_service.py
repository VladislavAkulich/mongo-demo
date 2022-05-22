from core.mongo_ctx_manager import MongoDBConnection

mongo = MongoDBConnection()
DEFAULT_DB = 'local'


def get_raw_data():
    with mongo:
        data = mongo.conn.get_database(DEFAULT_DB).test.find_one({"raw_data": {"$ne": None}})

    return data