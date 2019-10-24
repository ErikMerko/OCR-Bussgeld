import pdf2image
from PIL import Image


#Moritz Rogalski

#Diese Klasse überprüft ob es sich bei der Datei bereits um ein JPG handelt, falls nicht wird eine JPG Image aus der Pdf erstellt.
class PdfConvertToJPG:
    __instance = None
    @staticmethod
    def getInstance():
       if PdfConvertToJPG.__instance == None:
         PdfConvertToJPG()
       return PdfConvertToJPG.__instance
    #Initialisierung der Klasse: Bei Erstellung wird überprüft ob schon eine Instanz der Klasse existiert. 
    def __init__(self):
       if PdfConvertToJPG.__instance != None:
         raise Exception("Klasse bereits instanziert")
       else:
         PdfConvertToJPG.__instance = self

    def jpgConvert (self,dateipfad):
        image = pdf2image.convert_from_path(dateipfad,fmt='jpg',dpi='400')
        return image


#Test der Klasse
test = PdfConvertToJPG()
images = test.jpgConvert('C:/Users/MO/Desktop/Bußgelder/test.pdf')

for image in images:
  image.show()
  image.save('C:/Users/MO/Desktop/Bußgelder/out.jpg')
