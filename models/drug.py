from database import db

class Drug(db.Model):
    __tablename__ = 'drug'
    name = db.Column(db.String(100))
    code = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, name, code, description):
        self.name = name
        self.code = code
        self.description = description