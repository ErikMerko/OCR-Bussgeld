import pytesseract
import re
import datetime
import math
import numpy as np
from PIL import Image


# import rstr


class Extractor:

    # Erzeugt und speichert OCR-Output
    def __init__(self, bussgeld_path):
       # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Erik\Tesseract-OCR\tesseract.exe'
        self.ocrOutput = pytesseract.image_to_string(Image.open(bussgeld_path), lang='deu', config='preserve_interword_spaces = true')

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

    # Gibt aus dem OCR-Output das Vergehen als String zurück
    def find_Vergehen(self):
        val = Vergehen_Validator(self.ocrOutput)
        return val.get_result()

    def get_information_context(self):
        return InformationContext(self.find_Kennzeichen(), self.find_Tatdatum(), self.find_Tatuhrzeit(), self.find_Verwarngeld(), self.find_Vergehen())
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
        self.__result = super().format_filter(r'(3[01]|[12][0-9]|0[1-9])\.(1[0-2]|0[1-9])\.\d{2,4}', self.ocrOutput)

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
        if len(self.__result) < 1:
            self.__result = '???'
            # TODO 2. Phasen implementieren - wenn Matches < 1 -> Regex lockern

    # Gibt den finalen Ergebnissstring zurück.
    def get_result(self):
        return self.__result


# Extrahiert den Aussteller der Verwarnung aus dem OCR-Output.
class Aussteller_Detector(Detector):

    # Speichert den finalen Ergebnisstring in der Result-Instanzvariable.
    def __init__(self, ocrOutput):
        super().__init__(ocrOutput)
        # TODO Detector implementieren


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
        schlagworte = self.__schlagwort_Check(ocrOutput)
        for schlagwort in schlagworte:
            if schlagwort != None:
                regex = r'Sie([A-ZÄÖÜ]|[a-zäöüß]|[0-9]|[\/]|[\s]|[\,]|[\(]|[\)]|[\§]|[\.]|[\"]|[\$])+' + schlagwort + '([A-ZÄÖÜ]|[a-zäöüß]|[0-9]|[\/]|[\s]|[\,]|[\(]|[\)]|[\§]|[\.]|[\"]|[\$])+\.'
                self.__result = super().format_filter(regex, self.ocrOutput)
        if len(self.__result) == 0:
            for schlagwort in schlagworte:
                if schlagwort != None:
                    regex = r'Sie(.)+' + schlagwort + '(.)+\.'
                    self.__result = super().format_filter(regex, self.ocrOutput)
                else:
                    self.__result = '???'

    # Überprüft ob eines der Schlagwörter im OCR-Output vorhanden ist.
    def __schlagwort_Check(self, ocrOutput):
        super().__init__(ocrOutput)
        schlagworte = self.__alle_Schlagworte()
        erg = []
        for schlagwort in schlagworte:
            self.__result = super().format_filter(schlagwort, self.ocrOutput)
            if len(self.__result) >= 1:
                erg.append(schlagwort)
        return erg

    # Gibt eine Stringliste mit allen Bussgeld-Schlagwörtern zurück
    def __alle_Schlagworte(self):
       # with open("resources/Bussgeld-Schlagwoerter.txt", 'r', encoding='utf-8') as f:
        with open(r"ocr-bussgeld\resources\Bussgeld-Schlagwoerter.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        schlagworte = []
        for line in lines:
                schlagworte.append(line.rstrip())
        return schlagworte

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
        # with open("resources/KFZ-Kennzeichen.txt", 'r', encoding='utf-8') as f:
        with open(r"ocr-bussgeld\resources\KFZ-Kennzeichen.txt", 'r', encoding='utf-8') as f:
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
        print(ocrOutput)
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Tatdatum_Detector(self.ocrOutput)
        matches = val.get_result()
        check_matches = []
        if len(matches) < 1:
            self.__result = '???'
        else:
            for match in matches:
                zukunft = self.__check_Zukunft(match)
                if zukunft == False:
                    try:
                        erg = datetime.datetime.strptime(match, '%d.%m.%Y')
                    except ValueError:
                        erg = datetime.datetime.strptime(match, '%d.%m.%y')
                    check_matches.append(erg)
            self.__result = self.__check_Tatdatum(check_matches)

    def __check_Tatdatum(self, matches):
        if (len(matches) == 1) | (len(matches) > 3):
            erg = '???'
        elif len(matches) == 2:
            if ((matches[0] + datetime.timedelta(days=3650)) < matches[1]) | ((matches[1] + datetime.timedelta(days=3650)) < matches[0]):
                print(matches[0] + datetime.timedelta(days=3650))
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

    def __check_Zukunft(self, datum):
        heute = datetime.datetime.today()
        try:
            match = datetime.datetime.strptime(datum, '%d.%m.%Y')
        except ValueError:
            match = datetime.datetime.strptime(datum, '%d.%m.%y')
        if match > heute:
            return True
        else:
            return False

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


class Vergehen_Validator:

    def __init__(self, ocrOutput):
        self.ocrOutput = ocrOutput
        self.__check_plausibility()

    def __check_plausibility(self):
        val = Vergehen_Detector(self.ocrOutput)
        matches = val.get_result()
        self.__result = matches

        # TODO Plausibilität überprüfen!

    def get_result(self):
        return self.__result

class InformationContext:
    def __init__(self, knz, date, time, verwarngeld, vergehen):
        self.Kennzeichen = knz
        self.Tatdatum = date
        self.Tatzeit = time
        self.Verwarngeld = verwarngeld
        self.Vergehen = vergehen