from flask import Flask, jsonify
import logging.config
from database import init_db
from config import DevelopmentConfig
from model import Message


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    init_db(app)

    return app


app = create_app()
app.app_context().push()


# API
#######
@app.route('/hello/')
def hello():
    name = "Hello World"
    return jsonify({"msg": name}), 200
#######


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10090)
