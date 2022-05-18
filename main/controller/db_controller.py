from flask import jsonify, Blueprint, request

from main.service.fen_service import mongo

db_blueprint = Blueprint('db_blueprint', __name__)

DEFAULT_DB='local'


@db_blueprint.route('/', methods = ['GET'])
def get_whole_db():
    with mongo:
        data = mongo.conn.get_database(DEFAULT_DB).test.find_one({"raw_data": {"$ne":None}})
        print(data)
    return jsonify(data['raw_data']), 200