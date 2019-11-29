import json
from Levenshtein import *

# from pdf2image import pdf2image
from BussgeldExtractor import Extractor

# pdf2image.convert_from_path("resources/ideal-images/600dpi/BußgeldVorlage1Scan2-600dpi.pdf", fmt='png', dpi='600', output_folder="resources/ideal-images/600dpi")

# Testfälle ideal-images/300dpi
# extr = Extractor("resources/ideal-images/300dpi/d5debecb-5cb4-46da-890c-9ac60dcdb40c-1.png")

# Testfälle ideal-images/600dpi
# extr = Extractor("resources/ideal-images/600dpi/Bußgeldbescheid-Aalen.png")
# extr = Extractor("resources/ideal-images/600dpi/Bußgeldbescheid-Dortmund.png")
# extr = Extractor("resources/ideal-images/600dpi/Bußgeldbescheid-Hamburg.png")
# extr = Extractor("resources/ideal-images/600dpi/Bußgeldbescheid-Koblenz.png")
# extr = Extractor("resources/ideal-images/600dpi/Bußgeldbescheid-Unbekannte Stadt.png")

# Testfälle ideal-images/smartphone
# extr = Extractor("resources/ideal-images/smartphone/7a8b2627-328f-45bd-b062-f51c1508d1d8-1.png")
# extr = Extractor("resources/ideal-images/smartphone/38b3acaa-ac9a-4e2b-86d7-c829def36060-1.png")

# Testfälle ideal-images/Testfälle
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Düsseldorf-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-FrankfurtamMain-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Goslar-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Kassel-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Stuttgart-1.png")
extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage6-Dresden-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage6-Dresden-2.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage6-Dresden-3.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage11-Zwickau-2.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage11-Zwickau-3.png")
# extr = Extractor("resources/ideal-images/Testfälle/Bußgeldbescheid-Vorlage18-Tübingen-2.png")
# extr = Extractor("resources/ideal-images/Testfälle/BußgeldbescheidTübingen-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/HavellandTestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/HerfordTestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/KonstanzTestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/LandBrandenburgTestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/MünsterTestv1.png")
# extr = Extractor("resources/ideal-images/Testfälle/OriginalDuisburg.jpg")
# extr = Extractor("resources/ideal-images/Testfälle/OriginalLandkreisKonstanz.png")
# extr = Extractor("resources/ideal-images/Testfälle/OrignalOstalbkreis.jpg")
# extr = Extractor("resources/ideal-images/Testfälle/Verwarngeldbescheid-Vorlage16Kassel-Test-1.png")
# extr = Extractor("resources/ideal-images/Testfälle/Verwarngeldbescheid-Vorlage19-Dortmund.png")
# extr = Extractor("resources/ideal-images/Testfälle/VerwarngeldbescheidVorlage3TestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/VerwarngeldbescheidVorlage4BielefeldTestNr1.png")
# extr = Extractor("resources/ideal-images/Testfälle/ZwickauTestNr1.png")

# Testfälle ideal-images/Testfälle/falsche Testfälle
#extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/1.png")
#extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/2.png")
#extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/3.png")
#extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/4.png")
extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/5.png")
# extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/3.png")
# extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/3.png")
# extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/3.png")
# extr = Extractor("resources/ideal-images/Testfälle/falsche Testfälle/3.png")

# Testfälle images/Anhörungsbogen
# extr = Extractor("resources/images/Anhörungsbogen/AB_B-AV-X_15.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-AV_1.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-B-O-AV_14.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-B-T-O-AV-X_9.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-B-T-O-AV_2.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-O-AV_3.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-V-B-O-AV_12.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_D-U-V-O-AV_4.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_6.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_7.png")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_16.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_20.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_21.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_22.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-B-A-T-O-AV_23.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-O-AV_13.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-V-B-A-T-O-AV_10.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-V-B-A-T-O-AV_17.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-V-B-A-T-O-AV_18.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_K-D-U-V-B-A-T-O-AV_19.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_X_5.jpg")
# extr = Extractor("resources/images/Anhörungsbogen/AB_X_11.jpg")

# Testfälle images/Bussgeldbescheide
# extr = Extractor("resources/images/Bussgeldbescheide/BB_AV-X_8.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_B-T-O-AV_14.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-AV_1.JPG")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-AV_11.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-B-A-O-AV_21.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-B-O-AV-X_3.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-B-O-AV_2.JPG")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-B-T-O-AV_20.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-O-AV_10.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_D-U-V-O-AV_19.jpeg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_4.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_12.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_15.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_17.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_23.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_24.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_25.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-A-T-O-AV_26.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-O-AV_5.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-B-T-O-AV_6.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_K-D-U-V-O-AV_13.JPG")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_V-B-A-T_22.jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_V-O-AV_7.JPG")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_X_9 (Nationalparkverwaltung).jpg")
# extr = Extractor("resources/images/Bussgeldbescheide/BB_X_18.jpg")


context = extr.get_information_context()
print(json.dumps(context, default=lambda x: x.__dict__, ensure_ascii=False))