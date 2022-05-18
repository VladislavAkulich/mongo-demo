import requests

from core.mongo_ctx_manager import MongoDBConnection

mongo = MongoDBConnection()
DEFAULT_DB = 'local'
FEN_API = 'http://localhost:9966/api/fenbase'
BASE_API = 'http://localhost:9966/api/base'

def insert_fen_data():
    data = requests.get(FEN_API).json()
    docs = []

    for i in range(0, len(data) - 1):
        docs.append({"fen": data[i][0], "info": data[i][1]})

    with mongo:
        mongo.conn.get_database(DEFAULT_DB).test.insert_many(docs)


def insert_raw_data():
    data = requests.get(BASE_API).text
    doc = {"raw_data" : data}
    with mongo:
        mongo.conn.get_database(DEFAULT_DB).test.insert_one(doc)

if __name__ == '__main__':
    insert_fen_data()
    insert_raw_data()



