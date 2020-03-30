import dependency_injector.containers as containers
import dependency_injector.providers as providers

from services.data.subway import SubwayDataService


class ServiceContainer(containers.DeclarativeContainer):
    subway_data_service = providers.Factory(SubwayDataService)
