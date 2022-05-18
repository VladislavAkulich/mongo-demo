from flask import jsonify, Blueprint, request

from main.service import fen_service


fen_blueprint = Blueprint('fen_blueprint', __name__)

@fen_blueprint.route('/info', methods = ['GET'])
def get_fen():
    fen = request.args.get('fen')
    return jsonify(fen_service.get_fen_info(fen)), 200



@fen_blueprint.route('/fenBase', methods = ['GET'])
def get_fen_base():
    return jsonify(fen_service.get_all_fens()), 200