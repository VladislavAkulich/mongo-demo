import flask

from flask_caching import Cache

from main.controller.db_controller import db_blueprint
from main.controller.fen_controller import fen_blueprint


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = flask.Flask(__name__)
app.register_blueprint(fen_blueprint, url_prefix='/fen')
app.register_blueprint(db_blueprint, url_prefix='/db')

cache = Cache()


if __name__ == '__main__':
    app.debug = True
    cache.init_app(app, config=config)
    app.run()
