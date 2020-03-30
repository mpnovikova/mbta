from flask import Blueprint, jsonify

from services.service_container import ServiceContainer
from services.exceptions.api_error import ApiError

subway_api = Blueprint("subway_api", __name__, url_prefix="")


@subway_api.route("/routes", methods=["GET"])
def index_routes():
    result = ServiceContainer.subway_data_service().index_routes()
    response = [r.serialize() for r in result]
    return jsonify({"response": response}), 200


@subway_api.route("/routes/<route_id>", methods=["GET"])
def index_stops(route_id):
    try:
        result = ServiceContainer.subway_data_service().index_stops(route_id=route_id)
    except ValueError:
        raise ApiError("Invalid route ID", status_code=400)

    response = [r.serialize() for r in result]
    return jsonify({"response": response}), 200


@subway_api.errorhandler(ApiError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
