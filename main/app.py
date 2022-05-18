import flask
import requests

from flask import jsonify

from main.controller.db_controller import db_blueprint
from main.controller.fen_controller import fen_blueprint


app = flask.Flask(__name__)
app.register_blueprint(fen_blueprint, url_prefix='/fen')
app.register_blueprint(db_blueprint, url_prefix='/db')




@fen_blueprint.route('/', methods=['GET'])
def home():
    return jsonify("Chess app!!!!"), 200


@app.route('/_ah/warmup')
def warmup():
    r = requests.get('http://localhost:9966/api/base')
    print(r.json())
    return '', 200, {}


if __name__ == '__main__':
    app.debug = True
    app.run()
