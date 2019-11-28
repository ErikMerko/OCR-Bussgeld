import pdf2image  # pip install pdf2image
from PIL import Image
import os


# Moritz Rogalski

# Diese Klasse erstellt ein png Image aus einer Pdf.
class PdfConvertToJPG:
    __instance = None

    @staticmethod
    def getInstance():
        if PdfConvertToJPG.__instance == None:
            PdfConvertToJPG()
        return PdfConvertToJPG.__instance

    # Initialisierung der Klasse: Bei Erstellung wird überprüft ob schon eine Instanz der Klasse existiert.
    def __init__(self):
        if PdfConvertToJPG.__instance != None:
            raise Exception("Klasse bereits instanziert")
        else:
            PdfConvertToJPG.__instance = self

    def jpgConvert(self, dateipfad):
        #  if os.path.basename(dateipfad).split(".") == ".pdf":
        image = pdf2image.convert_from_path(dateipfad, fmt='png', dpi='600', output_folder="resources/ideal-images/Testfälle/falsche Testfälle")
        return image
    # else:
    #   raise Exception("Keine PDF")

# Test der Klasse
test = PdfConvertToJPG()
#images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Bußgeldbescheid-Unbekannte Stadt.pdf')
#images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Bußgeldbescheid-Koblenz.pdf')
#images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage22Bußgeldbescheid-FrankfurtamMain.pdf')
images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage21Bußgeldbescheid-Stuttgart.pdf')
# images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage24Bußgeldbescheid-Goslar.pdf')
# images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage24Bußgeldbescheid-Goslar.pdf')
# images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage24Bußgeldbescheid-Goslar.pdf')
# images = test.jpgConvert('C:/Users/soc4real/TesseractData/GitRepo/ocr-bussgeld/resources/ideal-images/Testfälle/falsche Testfälle/Vorlage24Bußgeldbescheid-Goslar.pdf')