from database import db, ma

class Drug(db.Model):
    __tablename__ = 'drug'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(10), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, code, name, description):
        self.name = name
        self.code = code
        self.description = description
db.create_all()

class drugSchema(ma.Schema):
    class Meta:
        fields = ('id', 'code', 'name', 'description')