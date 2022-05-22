from flask import jsonify, Blueprint, request

from main.service import db_service

db_blueprint = Blueprint('db_blueprint', __name__)

DEFAULT_DB='local'


@db_blueprint.route('/', methods = ['GET'])
def get_whole_db():
    data = db_service.get_raw_data()
    return jsonify(data['raw_data']), 200