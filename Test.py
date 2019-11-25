import json

# from pdf2image import pdf2image
from BussgeldExtractor import Extractor

# pdf2image.convert_from_path("resources/ideal-images/600dpi/BußgeldVorlage1Scan2-600dpi.pdf", fmt='png', dpi='600', output_folder="resources/ideal-images/600dpi")

# extr = Extractor("resources/ideal-images/300dpi/d5debecb-5cb4-46da-890c-9ac60dcdb40c-1.png")
# extr = Extractor("resources/ideal-images/600dpi/f8bc9163-a6d6-44d9-bd5d-0baac4dfe4c7-1.png")
# extr = Extractor("resources/ideal-images/smartphone/7a8b2627-328f-45bd-b062-f51c1508d1d8-1.png")
# extr = Extractor(r"ocr-bussgeld\resources\images\BB_K-D-U-V-B-O-AV_5.jpg")
# extr = Extractor("resources/images/BB_K-D-U-V-B-A-T-O-AV_15.jpg")
# extr = Extractor("resources/images/BB_D-U-V-AV_1.JPG")
# extr = Extractor(r"resources/ideal-images/600dpi/Bußgeldbescheid-Aalen.png")
# extr = Extractor("resources/ideal-images/TestbilderWordSerienbriefe/KonstanzTestNr1.png")
extr = Extractor(r"ocr-bussgeld\resources\ideal-images\Testfälle\OriginalDuisburg.jpg")
print(extr.find_Tatuhrzeit())
# context = extr.get_information_context()
# print(json.dumps(context, default=lambda x: x.__dict__, ensure_ascii=False))

