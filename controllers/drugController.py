from flask_restful import Resource
from flask import request, jsonify
from models.drug import Drug, drugSchema
from database import db, ma
from helpers import validations

drug_schema = drugSchema()
drugs_schema = drugSchema(many=True)

class drugController(Resource):
    def index():
        try:
            all_drugs = Drug.query.all()
            response = drugs_schema.dump(all_drugs)
            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500

    def get(id):
        try:
            drug = Drug.query.get(id)
            if drug is None:
                return jsonify(success=True, message='drug not found'), 404
            response = drug_schema.dump(drug)
            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500
    def post():
        try:
            if not request.headers.get('Content-Type') or not request.headers['Content-Type'] == 'application/json':
                return jsonify(success=True, message='header not valid'), 400

            code = request.json['code']
            if validations.validateSize(code, 10):
                return jsonify(success=True, message='code exceeded the maximum size'), 400
            
            name = request.json['name']
            description = request.json['description']
            if validations.validateSize(description, 255):
                return jsonify(success=True, message='description exceeded the maximum size'), 400

            # validate if element exist
            exists = db.session.query(Drug.code).filter_by(code=code).scalar()
            if exists is not None:
                return jsonify(success=True, message='code exist', result= exists), 400
            new_drug = Drug(code, name, description)
            db.session.add(new_drug)
            db.session.commit()
            response = drug_schema.dump(new_drug)
            return jsonify(success=True, result=response), 201
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500
    def put(id):
        try:
            if not request.headers.get('Content-Type') or not request.headers['Content-Type'] == 'application/json':
                return jsonify(success=True, message='header not valid'), 400

            drug = Drug.query.get(id)
            if drug is None:
                return jsonify(success=True, message='drug not found'), 404

            name = request.json['name']
            description = request.json['description']
            if validations.validateSize(description, 255):
                return jsonify(success=True, message='description exceeded the maximum size'), 400

            drug.name = name
            drug.description = description

            db.session.commit()
            response = drug_schema.dump(drug)

            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500

    def delete(id):
        try:
            drug = Drug.query.get(id)
            if drug is None:
                return jsonify(success=True, message='drug not found'), 404
            db.session.delete(drug)
            db.session.commit()
            return jsonify(success=True, message='resource deleted successfully'), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500