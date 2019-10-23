class InformationContext:

    knz = None
    date = None
    time = None
    verwarngeld = None

    def __init__(self, knz, date, time, verwarngeld):
        self.knz = knz
        self.date = date
        self.time = time
        self.verwarngeld = verwarngeld
