import pytesseract
import re
import datetime
import math
import numpy as np
from PIL import Image
import csv

from Levenshtein import *

# import rstr


class Extractor:

    # Erzeugt und speichert OCR-Output
    def __init__(self, bussgeld_path):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        #Ingo
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


        # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Erik\Tesseract-OCR\tesseract.exe'
        self.ocrOutput = pytesseract.image_to_string(Image.open(bussgeld_path), lang='deu', config='preserve_interword_spaces = true')

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

    # Gibt aus dem OCR-Output das Vergehen als String zurück
    def find_Vergehen(self):
        val = Vergehen_Validator(self.ocrOutput)
        return val.get_result()

    # Gibt aus dem OCR-Output das Vergehen als String zurück
    def find_AusstellerVerwarnung(self):
        val = Aussteller_Validator(self.ocrOutput)
        return val.get_result()

    def get_information_context(self):
        return InformationContext(self.find_Kennzeichen(), self.find_Tatdatum(), self.find_Tatuhrzeit(), self.find_Verwarngeld(), self.find_Vergehen(), self.find_AusstellerVerwarnung())


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
        self.__result = super().format_filter(r'\b([A-Z]|[\u00C4\u00D6\u00DC]){1,3}(\-|\s|\s\-)[A-Z]{1,2}\s\d{1,4}', self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = super().format_filter(r'([A-Z]|[\u00C4\u00D6\u00DC])+(\-|\s|\s\-)[A-Z]{1,2}\s\d{1,4}', self.ocrOutput)
        if len(self.__result) < 1:
            self.__result = super().format_filter(r'([A-Z]|[\u00C4\u00D6\u00DC])+(\-|\s|\s\-)[A-Z]{1,2}\s\d{1,4}(\sE|E)', self.ocrOutput)

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert das Tatdatum aus dem OCR-Output.
class Tatdatum_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        ocrOutput = re.sub('O', '0', self.ocrOutput)
        self.__result = super().format_filter(r'\s(3[01]|[12][0-9]|0[1-9])\.(1[0-2]|0[1-9])\.\d{2,4}', self.ocrOutput)

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert die Tatuhrzeit aus dem OCR-Output.
class Tatuhrzeit_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariabele.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'((?<!(\.|\d))\d{1,2}(:|\.)\d{1,2})(?!(\sEUR|\d\sEUR|\s€|\d\s€|\.|\d\.|\d))', self.ocrOutput)

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert das Verwarngeld aus dem OCR-Output.
class Verwarngeld_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        self.__result = super().format_filter(r'\b\d{1,4}\,\d{2}\s(€|EUR)', self.ocrOutput)

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert den Aussteller der Verwarnung aus dem OCR-Output.
class Aussteller_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
    
        if(self.__searchMail(ocrOutput) != -1 or self.__checkMail(self.__searchMail(ocrOutput)) != -1):
            self.__result=self.__checkMail(self.__searchMail(ocrOutput))
        elif(self.__searchURL(ocrOutput) != -1 or self.__checkURL(self.__searchURL(ocrOutput)) != -1):
            self.__result=self.__checkURL(self.__searchURL(ocrOutput))
        else:
            self.__result="???"     
            
    # def __searchBezVerwarnung(self,ocrOutput):
    #      with open('bußgeldstellen.csv', encoding='utf-8') as csv_file:
    #         csv_reader = csv.reader(csv_file, delimiter=';')
    #         for row in csv_reader:
    #             bez_aussteller = row[0]
    #             print(bez_aussteller)
    #             if(bez_aussteller in ocrOutput == True):
    #                 print(row[0])
    #                 print("Aussteller gefunden") 
    #                 return row[0]
                    
    #sucht nach der Mail des Austellers im Ocr Output
    def __searchMail(self,ocrOutput):
        regexmail =r'\S{1,40}@\S{1,20}.de'
        results = super().format_filter(regexmail, self.ocrOutput)
        for result in results:
            if len(results).bit_length()<1:
                print("Keine Mail gefunden")
                return -1   
            print(result) 
            return result


    # sucht in der Datei bußgeldstellen.csv ob er die zur Mail dazu gehörige Bußgeldstelle findet.
    def __checkMail(self,mail):
        try:
            kenn_mail=mail.split("@")[-1]
        except AttributeError:
            return "???"
        
        print(kenn_mail)
        with open('bußgeldstellen.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:

                if (row[2].find(kenn_mail) != -1 or row[2].find(kenn_mail.lower()) != -1): 
                    print("Match gefunden Mail")
                    aus_verw=row[0]
                    print(aus_verw)
                    return aus_verw    
            return -1

    def get_result(self):
        return self.__result       
                


    def __searchURL(self,ocrOutput):
        regexurl =r'www.\S{1,50}.de'
        results = super().format_filter(regexurl, self.ocrOutput)
        for result in results:
            if len(results).bit_length()==0:
                return -1   
            print(result) 
            return result

    def __checkURL(self,url):
        url=url
        print(url)
        with open('bußgeldstellen.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if (row[2].find(url) != -1 or row[2].find(url.lower()) != -1): 
                    print("Match gefunden")
                    aus_verw=row[0]
                    print(aus_verw)
                    return aus_verw
            return -1





# Extrahiert das Aktenzeichen aus dem OCR-Output.
class Aktenzeichen_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        # TODO Detector implementieren


# Extrahiert die Telefonnummer aus dem OCR-Output.
class Telefon_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        # TODO Detector implementieren


# Extrahiert den Ort des Vergehens aus dem OCR-Output.
class Tatort_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        # TODO Detector implementieren


# Extrahiert die Art des Vergehens aus dem OCR-Output.
class Vergehen_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        ocrOutput = re.sub('\s\n', ' ', self.ocrOutput)
        ocrOutput = re.sub('\n', ' ', self.ocrOutput)
        schlagworte = self.__schlagwort_Check(ocrOutput)
        formulierungen = self.__alle_Formulierungen_Regex()
        erg = [""]
        for schlagwort in schlagworte:
            if schlagwort != None:
                for formulierung in formulierungen:
                    if formulierung.find(schlagwort) != -1:
                        zerg = super().format_filter(formulierung, self.ocrOutput)
                        if len(zerg) == 1:
                            if len(erg) == 0 | (len(zerg[0]) > len(erg[0])):
                                erg[0] = zerg[0]
        if len(erg[0]) >= 1:
            erg.append("1")
            self.__result = erg
        else:
            for schlagwort in schlagworte:
                for counter in range(1,5):
                    regex = r'Sie ' + schlagwort + ' (([A-ZÄÖÜ]|[a-zäöü]|[0-9]|[ß]|[\,\§\$\/\(\)\-\+\"\\\;\&\:\']|[\s])*[\.]){' + str(counter) + '}'
                    a = super().format_filter(regex, self.ocrOutput)
                    if (len(a) >= 1) & (counter == 1):
                        erg[0] = schlagwort
                        erg.append(a[0])
                    elif (len(a) >= 1):
                        erg.append(a[0])
            if len(erg) >= 1:
                self.__result = erg

    # Überprüft ob eines der Schlagwörter im OCR-Output vorhanden ist.
    def __schlagwort_Check(self, ocrOutput):
        super().__init__(ocrOutput)
        schlagworte = self.__alle_Schlagworte()
        erg = []
        for schlagwort in schlagworte:
            zerg = super().format_filter(schlagwort, self.ocrOutput)
            if len(zerg) >= 1:
                erg.append(schlagwort)
        return erg

    # Gibt eine Stringliste mit allen Bussgeld-Schlagwörtern zurück
    def __alle_Schlagworte(self):

        with open("resources/Bussgeld-Schlagwoerter.txt", 'r', encoding='utf-8') as f:
        # with open(r"ocr-bussgeld\resources\Bussgeld-Schlagwoerter.txt", 'r', encoding='utf-8') as f:

            lines = f.readlines()
        schlagworte = []
        for line in lines:
                schlagworte.append(line.rstrip())
        return schlagworte

    # Gibt eine Stringliste mit allen Bussgeldformulierungen als Regex formuliert zurück
    def __alle_Formulierungen_Regex(self):
        with open("resources/Bussgeldformulierungen (Regex).txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        formulierungen = []
        for line in lines:
            formulierungen.append(line.rstrip())
        return formulierungen

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


class Kennzeichen_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        # TODO Plausibilität überprüfen!
        detec = Kennzeichen_Detector(self.ocrOutput)
        matches = detec.get_result()
        self.__result = matches
        for kennzeichen in matches:
            if self.__ortskennung_Check(kennzeichen):
                self.__result = kennzeichen
                return
            else:
                detec = Kennzeichen_Detector(self.__rechts_rotieren(kennzeichen))
                self.__result = detec.get_result()[0]
                return
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
        # with open(r"ocr-bussgeld\resources\KFZ-Kennzeichen.txt", 'r', encoding='utf-8') as f:


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
            return self.__rechts_rotieren(self.ocrOutput[self.ocrOutput.find(rotate_str, 0) + 1:self.ocrOutput.find(rotate_str,0) + len(rotate_str) + 1])
        else:
            return False

    def get_result(self):
        return self.__result


class Tatdatum_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Tatdatum_Detector(self.ocrOutput)
        matches = val.get_result()
        if len(matches) < 1:
            self.__result = '???'
        else:
            checked_matches = self.__check_Zukunft(matches)
            if len(checked_matches) < 1:
                self.__result = '???'
            else:
                self.__result = self.__check_Tatdatum(checked_matches)

    def __check_Tatdatum(self, matches):
        if (len(matches) == 1) | (len(matches) > 3):
            erg = '???'
        elif len(matches) == 2:
            if ((matches[0] + datetime.timedelta(days=3650)) < matches[1]) | ((matches[1] + datetime.timedelta(days=3650)) < matches[0]):
                if matches[0] > matches[1]:
                    zerg = datetime.date.strftime(matches[0], '%d.%m.%Y')
                else:
                    zerg = datetime.date.strftime(matches[1], '%d.%m.%Y')
            else:
                if matches[0] < matches[1]:
                    zerg = datetime.date.strftime(matches[0], '%d.%m.%Y')
                else:
                    zerg = datetime.date.strftime(matches[1], '%d.%m.%Y')
            erg = str(zerg)
        elif len(matches) == 3:
            if ((matches[0] < matches[1]) & (matches[0] > matches[2])) | ((matches[0] > matches[1]) & (matches[0] < matches[2])):
                zerg = datetime.date.strftime(matches[0], '%d.%m.%Y')
            elif ((matches[1] < matches[0]) & (matches[1] > matches[2])) | ((matches[1] > matches[0]) & (matches[1] < matches[2])):
                zerg = datetime.date.strftime(matches[1], '%d.%m.%Y')
            elif ((matches[2] < matches[0]) & (matches[2] > matches[1])) | ((matches[2] > matches[0]) & (matches[2] < matches[1])):
                zerg = datetime.date.strftime(matches[2], '%d.%m.%Y')
            erg = str(zerg)
        return erg

    def __check_Zukunft(self, datumliste):
        heute = datetime.datetime.today()
        erg = []
        for datum in datumliste:
            try:
                match = datetime.datetime.strptime(datum, ' %d.%m.%Y')
            except ValueError:
                try:
                    match = datetime.datetime.strptime(datum, ' %d.%m.%y')
                except ValueError:
                    erg = []
                    break
            if match < heute:
                erg.append(match)
                if len(erg) >= 2:
                    if erg[len(erg) - 1] == erg[len(erg) - 2]:
                        del erg[-1]
        return erg

    def get_result(self):
        return self.__result


class Tatuhrzeit_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        detec = Tatuhrzeit_Detector(self.ocrOutput)
        matches = detec.get_result()
        times = []
        for match in matches:
            if self.__is_time_valid(match):
                times.append(match)

        if len(times) == 1:
            self.__result = times[0].replace('.', ':')
        else:
            timeTuples = self.__ermittle_Koordinaten(times)
            timeMusterTuples = self.__ermittle_Musterindex(timeTuples)
            cumuli = [timeMusterTuple[3] for timeMusterTuple in timeMusterTuples]
            ausreisser = self.__get_Ausreisser(cumuli)
            if len(ausreisser) == 1:
                self.__result = timeMusterTuples[cumuli.index(ausreisser[0])][0]
            else:
                interval = self.__check_Interval(timeTuples)
                if interval:
                    self.__result = interval.replace('.', ':')
                else:
                    self.__result = '???'

        if len(matches) < 1:
            self.__result = '???'

    def __get_Ausreisser(self, cumuli):

        ausreisser = []
        threshold = 1
        mean = np.mean(cumuli)
        std = np.std(cumuli)

        for y in cumuli:
            z_score = (y - mean)/std
            if np.abs(z_score) > threshold:
                ausreisser.append(y)
        return ausreisser

    def __check_Interval(self, timeTuples):

        helperList = []
        for timeTuple in timeTuples:
            helperList.append(timeTuple)

        for timeTuple in timeTuples:
            helperList.remove(timeTuple)
            for helpItem in helperList:
                subindex = timeTuple[0].find(':')
                if not subindex == -1:
                    hourTime = timeTuple[0][:subindex]
                else:
                    subindex = timeTuple[0].find('.')
                    if not subindex == -1:
                        hourTime = timeTuple[0][:subindex]
                    else:
                        raise ValueError('Ungültiges Zeitformat')
                subindex = helpItem[0].find(':')
                if not subindex == -1:
                    helpHourTime = helpItem[0][:subindex]
                else:
                    subindex = helpItem[0].find('.')
                    if not subindex == -1:
                        helpHourTime = helpItem[0][:subindex]
                    else:
                        raise ValueError('Ungültiges Zeitformat')

                timeDifference = int(hourTime) - int(helpHourTime)
                np.linalg.norm(np.array((1, 2))-np.array((4, 5)))
                if ((timeDifference == 0 or abs(timeDifference) == 1) and np.linalg.norm(np.array((timeTuple[1], timeTuple[2]))-np.array((helpItem[1], helpItem[2]))) < 20):
                    return timeTuple[0]+' bis '+helpItem[0]
        return False

    def __ermittle_Koordinaten(self, times):

        ocrOutputLines = self.ocrOutput.splitlines()
        times = list(dict.fromkeys(times))
        timeTuples = []

        for time in times:
            lineCounter = 0
            for line in reversed(ocrOutputLines):
                columnCounter = line.find(time)

                if not columnCounter == -1:
                    timeTuple = (time, columnCounter, lineCounter)
                    timeTuples.append(timeTuple)
                lineCounter += 1

        return timeTuples

    def __ermittle_Musterindex(self, timeTuples):

        helperList = []
        for timeTuple in timeTuples:
            helperList.append(timeTuple)

        for timeTuple in timeTuples:
            cumulus = 0
            helperList.remove(timeTuple)
            for helpTuple in helperList:
                cumulus += np.linalg.norm(np.array((timeTuple[1], timeTuple[2]))-np.array((helpTuple[1], helpTuple[2])))
            cumulus -= 5*abs(timeTuple[2]- float(len(self.ocrOutput.splitlines()))/2)
            timeTuple = (timeTuple[0], timeTuple[1], timeTuple[2], cumulus)
            helperList.append(timeTuple)

        return helperList

    def __berechne_Punktabstand(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(y2-y1, 2)+math.pow(x2-x1, 2))

    def __is_time_valid(self, time):

        isValid = None

        try:
            validtime = datetime.datetime.strptime(time, "%H:%M")
            isValid = True
        except ValueError:
            try:
                validtime = datetime.datetime.strptime(time, "%H.%M")
                isValid = True
            except ValueError:
                isValid = False
        return isValid

    def get_result(self):
        return self.__result


class Verwarngeld_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Verwarngeld_Detector(self.ocrOutput)
        matches = val.get_result()
        if len(matches) < 1:
            self.__result = '???'
        else:
            self.__result = matches[0].replace(" ", "").replace("EUR", "").replace("€", "").replace(",", ".")
            for betrag in matches:
                betrag = betrag.replace(" ", "").replace("EUR", "").replace("€", "").replace(",", ".")
                if float(self.__result) < float(betrag):
                    self.__result = betrag

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Aussteller_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Aussteller_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Aktenzeichen_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Aktenzeichen_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Telefon_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Telefon_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


class Tatort_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Tatort_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result


# Hendrik Veips
# Prüft die Richtigkeit und die Vollständigkeit des Match
class Vergehen_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Vergehen_Detector(self.ocrOutput)
        matches = val.get_result()
        formulierungen = self.__alle_Formulierungen()
        levenshtein = 100
        checked_formulierung = ""
        checked_match = ""
        if len(matches) < 1:
            self.__result = '???'
        else:
            if matches[1] == "1":
                self.__result = matches[0]
            else:
                match = matches[0].replace("(l|I){2}", "ll").replace("(l|I)", "l")
                del matches[0]
                for formulierung in formulierungen:
                    if formulierung.find(match) != -1:
                        for mat in matches:
                            zerg = distance(formulierung, mat)
                            if zerg < levenshtein:
                                levenshtein = zerg
                                checked_formulierung = formulierung
                                checked_match = mat
                self.__result = self.__extrahiere_Formulierung(checked_formulierung, checked_match)

    # Vergleicht gefundenes Match und die ähnlichst Bußgeldformulierung (via Levenshtein gefunden)
    def __extrahiere_Formulierung(self, a, b):
        a_split = a.split(" ")
        b_split = b.split(" ")
        erg = ""
        x = 0
        delete = 0
        bool = True
        print(a)
        print(b)

        for wort in b_split:
            gesamt = x + delete
            if (distance(a_split[x], wort) <= 2) | (a_split[x] == 'XXX') | (a_split[x] == 'XXX,XX'):
                erg = erg + a_split[x] + " "
                x += 1
            elif (a_split[x] == '(…)') & (b_split[gesamt].find("(") != -1):
                while bool == True:
                    erg = erg + b_split[gesamt] + " "
                    if (b_split[gesamt].find(")") != -1) & (len(b_split[gesamt]) > 2):
                        bool = False
                    gesamt += 1
                x += 1
            elif (a_split[x] == '(…)') & (b_split[gesamt].find("(") == -1):
                if a_split[x + 1] == wort:
                    erg = erg + wort + " "
                    delete -= 1
                    x += 2
                else:
                    delete += 1
            elif (distance(a_split[x], wort) > 2):
                delete += 1
            if x == len(a_split):
                erg = erg[:-1]
                break
        if x != len(a_split):
            erg = '???'
        return erg

    # Gibt eine Stringliste mit allen Bussgeldformulierungen zurück
    def __alle_Formulierungen(self):
        with open("resources/Bussgeldformulierungen.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        formulierungen = []
        for line in lines:
            formulierungen.append(line.rstrip())
        return formulierungen

    def get_result(self):
        return self.__result

class InformationContext:
    def __init__(self, knz, date, time, verwarngeld, vergehen, aussteller):
        self.Kennzeichen = knz
        self.Tatdatum = date
        self.Tatzeit = time
        self.Verwarngeld = verwarngeld
        self.Vergehen = vergehen
        self.Aussteller = aussteller