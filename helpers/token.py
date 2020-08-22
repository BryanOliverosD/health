from flask_jwt_extended import (create_access_token, create_refresh_token)
from flask import jsonify
def generate_token():
    access_token = create_access_token('admin')
    return jsonify(status=True, token=access_token)