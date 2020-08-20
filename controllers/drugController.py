from flask_restful import Resource
from flask import request, jsonify
from models.drug import Drug, drugSchema
from database import db, ma

drug_schema = drugSchema()
drugs_schema = drugSchema(many=True)

class drugController(Resource):
    def index():
        try:
            all_drugs = Drug.query.all()
            response = drugs_schema.dump(all_drugs)
            return jsonify(response), 200
        except:
            return {'status': 'error interno'}, 500

    def get(id):
        try:
            drug = Drug.query.get(id)
            
            return drug_schema.jsonify(drug), 200
        except:
            return {'status': 'error interno'}, 500
    def post():
        try:
            code = request.json['code']
            name = request.json['name']
            description = request.json['description']

            exists = db.session.query(Drug.code).filter_by(code=code).scalar()
            if exists is not None:
                return {'status': 'código ya existe', 'code': exists}, 400
            new_drug = Drug(code, name, description)
            db.session.add(new_drug)
            db.session.commit()
            return drug_schema.jsonify(new_drug), 201
        except:
            return {'status': 'error interno'}, 500
    def put(id):
        try:
            drug = Drug.query.get(id)

            name = request.json['name']
            description = request.json['description']

            drug.name = name
            drug.description = description

            db.session.commit()

            return drug_schema.jsonify(drug), 200
        except:
            return {'status': 'error interno'}, 500

    def delete(id):
        drug = Drug.query.get(id)
        db.session.delete(drug)
        db.session.commit()
        return drug_schema.jsonify(drug)