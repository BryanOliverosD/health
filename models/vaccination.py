from database import db, ma

class Vaccination(db.Model):
    __tablename__ = 'vaccination'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True)
    dose = db.Column(db.Float())
    date = db.Column(db.DateTime)
    drug = db.Column(db.String(10), db.ForeignKey('drug.code'))
    drug_data = db.relationship("Drug", backref=db.backref("drug", uselist=False))

    def __init__(self, rut, dose, date, drug):
        self.rut = rut
        self.dose = dose
        self.date = date
        self.drug = drug
db.create_all()

class vaccinationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rut', 'dose', 'date', 'drug')