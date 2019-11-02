from flask import Flask, jsonify
import logging.config
import yaml
from database import db
from config import DevelopmentConfig
from handler import logger_before_request

logging.config.dictConfig(yaml.load(open('./logger.yml').read(), Loader=yaml.SafeLoader))


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.before_request(logger_before_request)
    db.init_app(app)

    return app


app = create_app()
app.app_context().push()
app.logger.disabled = True
logging.getLogger('werkzeug').disabled = True


# API
#######
@app.route('/hello/')
def hello():
    name = "Hello World"
    return jsonify({"msg": name}), 200
#######


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10090)
