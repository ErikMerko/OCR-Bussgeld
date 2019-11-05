import pickle


class FileDataService:
    filename = "testdata.pk1"
    files = []

    def __init__(self):
        self.open()

    def save(self):
        with open(self.filename, 'wb') as output:
            pickle.dump(self.files, output)

    def open(self):
        with open(self.filename, 'rb') as inp:
            self.files = pickle.load(inp)


class FileContext:

    name = None
    asString = None
    asData = None

    def __init__(self, name, asString, asData):
        self.name = name
        self.asString = asString
        self.asData = asData
