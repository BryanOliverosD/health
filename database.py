from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def init_db(app):
    global db
    global ma

    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    return db, ma