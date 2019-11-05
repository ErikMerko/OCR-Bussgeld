import pytesseract
import re
from PIL import Image

# import rstr


class Extractor:

    # Erzeugt und speichert OCR-Output
    def __init__(self, bussgeld_path):
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Erik\Tesseract-OCR\tesseract.exe'
        self.ocrOutput = pytesseract.image_to_string(Image.open(bussgeld_path), lang='deu')

        # Entfernt Zeilenumbrüche
        # self.ocrOutput = re.sub('\n', ' ', self.ocrOutput)

    # Gibt aus dem OCR-Output das Kennzeichen als String zurück
    def find_Kennzeichen(self):
        val = Kennzeichen_Validator(self.ocrOutput)
        return val.get_result()

    # Gibt aus dem OCR-Output das Tatdatum als String zurück
    def find_Tatdatum(self):
        val = Tatdatum_Validator(self.ocrOutput)
        return val.get_result()

        # Gibt aus dem OCR-Output die Tatuhrzeit als String zurück

    def find_Tatuhrzeit(self):
        val = Tatuhrzeit_Validator(self.ocrOutput)
        return val.get_result()

        # Gibt aus dem OCR-Output das Verwarngeld als String zurück

    def find_Verwarngeld(self):
        val = Verwarngeld_Validator(self.ocrOutput)
        return val.get_result()

    def get_information_context(self):
        return InformationContext(self.find_Kennzeichen(), self.find_Tatdatum(), self.find_Tatuhrzeit(), self.find_Verwarngeld())

    # Erzeugt zufällige Strings anhand eines Extractor (für Testzwecke)
    # def __random_Regex_Strings(self, Extractor, repeats = 1):
    #     for x in range(repeats):
    #         print(rstr.xeger(Extractor))


# Superklasse von der alle Validatorklassen erben
class Detector:

    # Alle Validatorklassen kriegen den OCR-Output aus der Extractorklasse
    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput

    # Filtert Informationen aus dem OCR-Output anhand eines Regex und gibt eine Stringliste mit Ergebnissen zurück. 
    def format_filter(self, regex, text):
        pattern = re.compile(regex)
        matches = pattern.finditer(text)
        matches_list = []
        for match in matches:
            matches_list.append(text[match.start():match.end()])
        return matches_list

    # Die Extractorklasse kriegt mit dieser Methode das Ergebnis der jeweiligen Validatorklasse.
    def get_result(self):
        raise NotImplementedError


# Extrahiert das Kennzeichen aus dem OCR-Output.
class Kennzeichen_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'([A-Z]|[\u00C4\u00D6\u00DC]){1,3}(\-|\s{|\s\-)[A-Z]{1,2}\s\d{1,4}',
                                              self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = '???'
            # TODO 2. Phasen implementieren - wenn Matches < 1 -> Regex lockern

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert das Tatdatum aus dem OCR-Output.
class Tatdatum_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'\bam\s\d{2}\.\d{2}\.\d{2,4}', self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = '???'
            # TODO 2. Phasen implementieren - wenn Matches < 1 -> Regex lockern

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert die Tatuhrzeit aus dem OCR-Output.
class Tatuhrzeit_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'\bum\s\d{1,2}\:\d{2}\sUhr', self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = '???'
            # TODO 2. Phasen implementieren - wenn Matches < 1 -> Regex lockern

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert das Verwarngeld aus dem OCR-Output.
class Verwarngeld_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'\b\d{1,4}\,\d{2}\s(€|EUR)', self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = '???'
            # TODO 2. Phasen implementieren - wenn Matches < 1 -> Regex lockern

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


class Verwarngeld_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Verwarngeld_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches[0].replace(" ", "").replace("EUR", "").replace("€", "").replace(",", ".")
        for betrag in matches:
            betrag = betrag.replace(" ", "").replace("EUR", "").replace("€", "").replace(",", ".")
            if float(self.__result) < float(betrag):
                self.__result = betrag

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Kennzeichen_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        # TODO Plausibilität überprüfen!
        val = Kennzeichen_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches
        for kennzeichen in matches:
            if self.__ortskennung_Check(kennzeichen):
                self.__result = kennzeichen
                return
            else:
                self.__result = '???'

    # Überprüft die Gültigkeit der Ortskennung. Rückgabewert ,,True" für gültig.
    def __ortskennung_Check(self, format_kennzeichen):
        subindex = format_kennzeichen.find(' ', 0)
        if subindex > 3:
            subindex = format_kennzeichen.find('-', 0)
        sub = format_kennzeichen[0:subindex]
        landkreise = self.__alle_Ortskennungen()
        for landkreis in landkreise:
            if sub == landkreis:
                return True
        return False

    # Gibt eine Stringliste mit allen deutschen KFZ-Ortskennungen zurück
    def __alle_Ortskennungen(self):
        with open("resources/KFZ-Kennzeichen.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]
        ortskennungen = []
        for line in lines:
            if line.isupper():
                ortskennungen.append(line)
        return ortskennungen

    # Rotiert im OCR-Output solange um eins nach rechts bis die Ortskennung gültig ist.
    # Gibt entweder den rotierten String zurück oder ein False falls die Ortskennung fehlgeschlagen ist.
    def __rechts_rotieren(self, rotate_str):

        if self.__ortskennung_Check(rotate_str):
            return rotate_str
        elif rotate_str[0].isupper():
            return self.__rechts_rotieren(self.ocrOutput[
                                          self.ocrOutput.find(rotate_str, 0) + 1:self.ocrOutput.find(rotate_str,
                                                                                                     0) + len(
                                              rotate_str) + 1])
        else:
            return False

    def get_result(self):
        return self.__result


class Tatuhrzeit_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Tatuhrzeit_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Tatdatum_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Tatdatum_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result

class InformationContext:
    def __init__(self, knz, date, time, verwarngeld):
        self.Kennzeichen = knz
        self.Tatdatum = date
        self.Tatzeit = time
        self.Verwarngeld = verwarngeld