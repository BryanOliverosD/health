from flask_restful import Resource
from flask import request, jsonify
from models.vaccination import Vaccination, vaccinationSchema
from models.drug import Drug
from database import db, ma
from helpers import validations

vaccination_schema = vaccinationSchema()
vaccinations_schema = vaccinationSchema(many=True)

class vaccinationController(Resource):
    def index():
        try:
            all_vaccinations = Vaccination.query.all()
            response = vaccinations_schema.dump(all_vaccinations)
            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500

    def get(id):
        try:
            vaccination = Vaccination.query.get(id)
            if vaccination is None:
                return jsonify(success=True, message='vaccination not found'), 404
            response = vaccination_schema.dump(vaccination)
            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500
    def post():
        try:
            if not request.headers.get('Content-Type') or not request.headers['Content-Type'] == 'application/json':
                return jsonify(success=True, message='header not valid'), 400

            rut = request.json['rut']
            # validate rut
            if not validations.validateRut(rut):
                return jsonify(success=True, message='rut not valid'), 400
            dose = request.json['dose']
            # validate dose within range
            if not validations.validateDose(dose):
                return jsonify(success=True, message='dose not valid'), 400
            date = request.json['date']

            drug = request.json['drug']
            
            # drug_element = Drug.query.whereclause({'code':drug})
            # if not drug_element:
            #     return jsonify(success=True, message='drug not exist'), 400
            
            # validate if element exist
            exists = db.session.query(Vaccination.rut).filter_by(rut=rut).scalar()
            if exists is not None:
                return jsonify(success=True, message='rut exist', result= exists), 400
            new_vaccination = Vaccination(rut, dose, date, drug)
            db.session.add(new_vaccination)
            db.session.commit()
            response = vaccination_schema.dump(new_vaccination)
            return jsonify(success=True, result=response), 201
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500
    def put(id):
        try:
            if not request.headers.get('Content-Type') or not request.headers['Content-Type'] == 'application/json':
                return jsonify(success=True, message='header not valid'), 400
                
            vaccination = Vaccination.query.get(id)
            if vaccination is None:
                return jsonify(success=True, message='vaccination not found'), 404

            dose = request.json['dose']
            # validate dose within range
            if not validations.validateDose(dose):
                return {'status': 'dose not valid'}, 400

            date = request.json['date']
            drug = request.json['drug']

            vaccination.dose = dose
            vaccination.date = date
            vaccination.drug = drug

            db.session.commit()
            response = vaccination_schema.dump(vaccination)
            return jsonify(success=True, result=response), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500

    def delete(id):
        try:
            vaccination = Vaccination.query.get(id)
            if vaccination is None:
                return jsonify(success=True, message='vaccination not found'), 404
            db.session.delete(vaccination)
            db.session.commit()
            return jsonify(success=True, message='resource deleted successfully'), 200
        except(Exception) as e: 
            print(e)
            return jsonify(success=False, errors='internal error'), 500