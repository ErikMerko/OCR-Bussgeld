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
