import pytesseract
import re
from PIL import Image
import rstr


class Regex:
    
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'Pfad zu einer tesseract.exe'
        self.ocrOutput = pytesseract.image_to_string(Image.open(r'Pfad zu einer PNG, JPG oder JPEG-Datei'), lang='deu')

    # Filtert Informationen aus den OCR-Output
    def filter_Information(self, regex, info_Type = ' '):
        pattern = re.compile(regex)
        matches = pattern.finditer(self.ocrOutput)
        for match in matches:
            print(info_Type+': '+self.ocrOutput[match.start():match.end()])

    # Erzeugt zufällige Strings anhand eines Regex (für Testzwecke)
    def random_Regex_Strings(self, regex, repeats = 1):
        for x in range(repeats):
            print(rstr.xeger(regex))

filter = Regex()
filter.filter_Information(r'\b([A-Z]|[\u00C4\u00D6\u00DC]){1,3}(\-|\s|\s\-)[A-Z]{1,2}\s\d{1,4}', "KFZ-Kennzeichen")
filter.filter_Information(r'\bam\s\d{2}\.\d{2}\.\d{2,4}', "Datum")
filter.filter_Information(r'\bum\s\d{1,2}\:\d{2}\sUhr', "Uhrzeit")
filter.filter_Information(r'\b\d{1,4}\,\d{2}\s(€|EUR)', "Höhe Verwarngeld")



