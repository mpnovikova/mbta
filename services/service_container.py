from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Factory

from services.data.subway import SubwayDataService


class ServiceContainer(DeclarativeContainer):
    subway_data_service = Factory(SubwayDataService)
