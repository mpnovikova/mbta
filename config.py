class Core(object):
    DEBUG = True
    MBTA_API = "https://www.mbta.com/developers/v3-api"


class Development(Core):
    pass


class Test(Core):
    pass


class Production(Core):
    pass