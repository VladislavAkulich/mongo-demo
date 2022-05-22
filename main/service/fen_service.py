from core.mongo_ctx_manager import MongoDBConnection

mongo = MongoDBConnection()
DEFAULT_DB = 'local'

def get_all_fens():
    data = []

    with mongo:
        cursor = mongo.conn.get_database(DEFAULT_DB).test.find({})
        for doc in cursor:
            del doc['_id']
            data.append(doc)

    return data


def get_fen_info(fen):
    with mongo:
        data = mongo.conn.get_database(DEFAULT_DB).test.find_one({'fen': fen})
        del data['_id']

    return data