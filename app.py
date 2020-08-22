from flask import Flask, request
from database import init_db
import os
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:testing@172.17.0.4:3306/health'
app.config['JWT_SECRET_KEY'] = '23people'
jwt = JWTManager(app)
init_db(app)

from models.drug import Drug
from models.vaccination import Vaccination
from controllers.drugController import drugController
from controllers.vaccinationController import vaccinationController
from helpers import token

### get token ####

@app.route('/token', methods=['GET'])
def get_token():

    response = token.generate_token()
    return response


### drugs crud ###

@app.route('/drugs', methods=['POST'])
@jwt_required
def create_drug():
    response = drugController.post()
    return response

@app.route('/drugs', methods=['GET'])
@jwt_required
def get_drugs():
    response = drugController.index()
    return response

@app.route('/drugs/<id>', methods=['GET'])
@jwt_required
def get_drug(id):
    response = drugController.get(id)
    return response

@app.route('/drugs/<id>', methods=['PUT'])
@jwt_required
def update_drug(id):
    response = drugController.put(id)
    return response

@app.route('/drugs/<id>', methods=['DELETE'])
@jwt_required
def delete_drug(id):
    response = drugController.delete(id)
    print("CHAO", response)
    return response

### vaccination crud ###

@app.route('/vaccinations', methods=['POST'])
@jwt_required
def create_vaccination():
    response = vaccinationController.post()
    return response

@app.route('/vaccinations', methods=['GET'])
@jwt_required
def get_vaccinations():
    response = vaccinationController.index()
    return response

@app.route('/vaccinations/<id>', methods=['GET'])
@jwt_required
def get_vaccination(id):
    response = vaccinationController.get(id)
    return response

@app.route('/vaccinations/<id>', methods=['PUT'])
@jwt_required
def update_vaccination(id):
    response = vaccinationController.put(id)
    return response

@app.route('/vaccinations/<id>', methods=['DELETE'])
@jwt_required
def delete_vaccination(id):
    response = vaccinationController.delete(id)
    return response

if __name__ == '__main__':
    app.run(port=os.environ['PORT'])