class FileContext:

    name = None
    asString = None
    asData = None

    def __init__(self, name, asString, asData):
        self.name = name
        self.asString = asString
        self.asData = asData
