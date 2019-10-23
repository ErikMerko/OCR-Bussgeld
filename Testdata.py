import pytesseract
from PIL import Image
import os

from services.FileDataService import FileDataService
from entities.FileContext import FileContext

##write data to file
# filelist = []
# for image in os.listdir("resources/images/"):
#    filelist.append(FileContext(image, \
#                                pytesseract.image_to_string(Image.open("resources/images/" + image), lang="deu"), \
#                                pytesseract.image_to_data(Image.open("resources/images/" + image), lang="deu")))
# service = FileDataService()
# service.files = filelist
# service.save()

## load data-
service = FileDataService()
for fileContext in service.files:
    print(fileContext.asString)
