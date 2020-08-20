from flask import Flask, request
from flask_restful import Resource
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
    return response

if __name__ == '__main__':
    app.run()