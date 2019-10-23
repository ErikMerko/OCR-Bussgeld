import re

import pytesseract

data = pytesseract.image_to_string('resources/images/unnamed.jpg', lang='deu')

amounts = re.findall("\d+,\d+", data)
eur = re.findall("EUR", data)

print(amounts)
print(eur)

