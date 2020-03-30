class Stop:
    def __init__(self, props):
        self.props = props

    @property
    def id(self):
        return self.props.get("id")

    @property
    def attributes(self):
        return self.props.get("attributes")

    @property
    def name(self):
        return self.attributes.get("name")

    @property
    def address(self):
        return self.attributes.get("address")

    def serialize(self):
        # The spec doesn't say which fields specifically need to be returned, so for simplicity let's
        # use same output format as for the routes
        return "ID: {}, NAME: {}".format(self.id, self.name)
