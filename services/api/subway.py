from flask import Blueprint, jsonify

from services import service_container

subway_api = Blueprint('subway_api', __name__, url_prefix='')


@subway_api.route('/subway', methods=['GET'])
def index():
    response = []

    result = service_container.subway_data_service().index()
    for doc in result:
        response.append(doc.to_dict())

    return jsonify({'response': response}), 200
