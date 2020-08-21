from flask import Flask, request
from database import init_db
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:testing@172.17.0.4:3306/health'
init_db(app)

from models.drug import Drug
from models.vaccination import Vaccination
from controllers.drugController import drugController
from controllers.vaccinationController import vaccinationController

##### drugs crud #######

@app.route('/drugs', methods=['POST'])
def create_drug():
    response = drugController.post()
    return response

@app.route('/drugs', methods=['GET'])
def get_drugs():
    response = drugController.index()
    return response

@app.route('/drugs/<id>', methods=['GET'])
def get_drug(id):
    response = drugController.get(id)
    return response

@app.route('/drugs/<id>', methods=['PUT'])
def update_drug(id):
    response = drugController.put(id)
    return response

@app.route('/drugs/<id>', methods=['DELETE'])
def delete_drug(id):
    response = drugController.delete(id)
    print("CHAO", response)
    return response

##### vaccination crud #######

@app.route('/vaccinations', methods=['POST'])
def create_vaccination():
    response = vaccinationController.post()
    return response

@app.route('/vaccinations', methods=['GET'])
def get_vaccinations():
    response = vaccinationController.index()
    return response

@app.route('/vaccinations/<id>', methods=['GET'])
def get_vaccination(id):
    response = vaccinationController.get(id)
    return response

@app.route('/vaccinations/<id>', methods=['PUT'])
def update_vaccination(id):
    response = vaccinationController.put(id)
    return response

@app.route('/vaccinations/<id>', methods=['DELETE'])
def delete_vaccination(id):
    response = vaccinationController.delete(id)
    return response

if __name__ == '__main__':
    app.run()