from database import db


class Message(db.Model):
    __table__name = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(256))
