from pymongo import MongoClient


class MongoDBConnection(object):
    """Mongo database connection"""

    host = None
    port = None
    conn = None

    def __int__(self, host='localhost', port='27017'):
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
