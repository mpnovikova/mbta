import requests

import config
from models.route import Route
from models.stop import Stop


class SubwayDataService:
    def __init__(self):
        self.routes = self.fetch_routes()
        self.valid_routes = [route.id for route in self.routes]

    def index_routes(self):
        if not self.routes:
            self.routes = self.fetch_routes()

        return self.routes

    @staticmethod
    def fetch_routes():
        url = "{}/routes?filter[type]=0,1".format(config.Core.MBTA_API)
        response = requests.get(url=url)
        data = response.json()
        return [Route(r) for r in data.get("data")]

    def is_valid_route(self, route_id):
        return route_id in self.valid_routes

    def index_stops(self, route_id):
        if self.is_valid_route(route_id):
            return self.fetch_stops(route_id)
        else:
            raise ValueError("Invalid route ID")

    @staticmethod
    def fetch_stops(route_id):
        url = "{}/stops?filter[route]={}".format(config.Core.MBTA_API, route_id)
        response = requests.get(url=url)
        data = response.json()
        return [Stop(s) for s in data.get("data")]
