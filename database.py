from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = None


def init_db(app):
    global db

    db = SQLAlchemy(app)
    Migrate(app, db)

    return db