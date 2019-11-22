from flask import Flask, jsonify, make_response
import logging.config
from database import init_db
from config import DevelopmentConfig
from model import Message
import os
import slack


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    init_db(app)

    return app


app = create_app()
app.app_context().push()

SLACK_BOT_TOKEN = "xoxb-811268029777-806459553058-utf9HHsCJwJxmyXNoxdKMZDA"
slack_bot = slack.WebClient(token=SLACK_BOT_TOKEN)

attachments_json = [
  {
    "fallback": "Upgrade your Slack client to use messages like these.",
    "color": "#258ab5",
    "attachment_type": "default",
    "callback_id": "the_greatest_war",
    "actions": [
      {
        "name": "b1",
        "text": "I'm 休み",
        "value": "yasumi",
        "type": "button"
      }
    ]
  }
]

# API
#######
@app.route('/hello/')
def hello():
    name = "Hello World"


@app.route('/tweet/', methods=["GET"])
def tweet():
    response = slack_bot.chat_postMessage(
        username='obento-bot',
        channel='#general',
        text= '<!channel>\nHi',
        attachments=attachments_json
    )
    print(response)
    return jsonify({}), 200
#######


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10090)
