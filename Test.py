import json

from pdf2image import pdf2image
from BussgeldExtractor import Extractor

# pdf2image.convert_from_path("resources/ideal-images/600dpi/BußgeldVorlage1Scan2-600dpi.pdf", fmt='png', dpi='600', output_folder="resources/ideal-images/600dpi")

# extr = Extractor("resources/ideal-images/300dpi/d5debecb-5cb4-46da-890c-9ac60dcdb40c-1.png")
# extr = Extractor("resources/ideal-images/600dpi/f8bc9163-a6d6-44d9-bd5d-0baac4dfe4c7-1.png")
# extr = Extractor("resources/ideal-images/smartphone/7a8b2627-328f-45bd-b062-f51c1508d1d8-1.png")
extr = Extractor("resources/ideal-images/smartphone/38b3acaa-ac9a-4e2b-86d7-c829def36060-1.png")
# extr = Extractor("resources/images/BB_K-D-U-V-B-A-T-O-AV_15.jpg")
# extr = Extractor("resources/images/BB_D-U-V-AV_1.JPG")

context = extr.get_information_context()
print(json.dumps(context, default=lambda x: x.__dict__, ensure_ascii=False))

