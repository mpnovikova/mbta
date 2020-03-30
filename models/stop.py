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
        return "ID: {}, NAME: {}".format(self.id, self.name)
