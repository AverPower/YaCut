from datetime import datetime

from yacut import db


class URL_map(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    original = db.Column(db.URL, unique=True)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
