import random 
import string
import re

#Ingo Speckens

testdaten_anzahl = 50

kennzeichen_textfile = 'resources/KFZ-Kennzeichen.txt'
kennzeichen_regex = '^([A-ZÄÖÜ]{1,3})\s*$'

bussgeld_textfile = 'resources/Bussgeldformulierungen.txt'
bussgeld_regex = '[A-zäöü].*?[\.!?][\n]'

orte_textfile = 'resources/Orte.txt'
orte_regex = '[A-zäöü]+.*'


def function_Textfile_auslesen(pfad, regex):
    with open(pfad, 'r', encoding='UTF-8') as kfz:
    
        listeTextfile = []
        listeTextfileOk = []
        for zeile in kfz:
            listeMatch = re.findall(regex, zeile)
            match = ''.join(listeMatch)
            #\n entfernen da sich python und regex \n teilen
            removeChar = match.replace('\n','')
            listeTextfile.append(removeChar)
        #zero-length-strings entfernen
        listeTextfileOk = [i for i in listeTextfile if i]
        #print(listeTextfileOk)
        return listeTextfileOk



#Kennzeichen_Generator
def function_Kennzeichen_Generator():

    listeKennzeichen = []
    for x in range(testdaten_anzahl):
        grossbuchstaben = string.ascii_uppercase
        kennzeichen = (random.choice(function_Textfile_auslesen(kennzeichen_textfile, kennzeichen_regex))
        + random.choice([' ', ' -', '-']) 
        + ''.join(random.choice(grossbuchstaben) for i in range(random.randint(1,2)))
        + " "
        + str(random.randint(1,9999)))
        listeKennzeichen.append(kennzeichen)
    return listeKennzeichen

#Tatdatum_Generator
def function_Tatdatum_Generator():
    listeDatum = []
    for x in range(testdaten_anzahl):
        monat = random.choice(['08', '09'])
        if monat !='02' or monat !='04' or monat !='05' or monat !='09' or monat !='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                 '31'])
        if monat =='02':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28'])
        if monat =='04' or monat =='05' or monat =='09' or monat =='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])

        datum = (random.choice([' ', 'am ']) 
        + str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['2019', '19']))
        listeDatum.append(datum)
    return listeDatum

#Briefdatum_Generator
def function_Briefdatum_Generator():
    listeDatum = []
    for x in range(testdaten_anzahl):
        monat = random.choice(['10'])
        if monat !='02' or monat !='04' or monat !='05' or monat !='09' or monat !='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                 '31'])
        if monat =='02':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28'])
        if monat =='04' or monat =='05' or monat =='09' or monat =='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])

        datum = (random.choice([' ', 'am '])
        + str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['2019', '19']))
        listeDatum.append(datum)
    return listeDatum

#Geburtstag_Generator
def function_Geburtstag_Generator():
    listeDatum = []
    for x in range(testdaten_anzahl):
        monat = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        if monat !='02' or monat !='04' or monat !='05' or monat !='09' or monat !='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                 '31'])
        if monat =='02':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                 '20', '21', '22', '23', '24', '25', '26', '27', '28'])
        if monat =='04' or monat =='05' or monat =='09' or monat =='11':
            tag = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                 '11', '12', '13', '14', '15', '16', '17', '18', '19', 
                                 '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])

        datum = (random.choice([' ', 'am ']) 
        + str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['1997', '97', '1998', '98', '1999', '99', '2000', '00']))
        listeDatum.append(datum)
    return listeDatum

#Uhrzeit_Generator
def function_Uhrzeit_Generator():
    listeUhrzeit = []
    for x in range(testdaten_anzahl):
        uhrzeit = (random.choice([' ', 'um '])
        + random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08','09', '10', 
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                         '21', '22', '23', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        + ":"
        + str(random.randint(0,5))
        + str(random.randint(0,9))
        + random.choice([' Uhr']))
        listeUhrzeit.append(uhrzeit)
    return listeUhrzeit

#Verwarngeld_Generator
def function_Verwarngeld_Generator():
    listeVerwarngeld = []
    for x in range(testdaten_anzahl):
        betrag = random.randint(1,5000)
        verwarngeld = (format(betrag, '.2f').replace('.', ',')
        + random.choice([" EUR", " €"]))
        listeVerwarngeld.append(verwarngeld)
    return listeVerwarngeld

#Anrede_Generator
def function_Anrede_Generator():
    listeAnrede = []
    for x in range(testdaten_anzahl):
        anrede = (random.choice(["Herr", "Frau"]))
        listeAnrede.append(anrede)
    return listeAnrede

#Vorname_Generator
def function_Vorname_Generator():
    listeVorname = []
    for x in range(testdaten_anzahl):
        vorname = (random.choice(["Thomas", "Steffen", "Ben", "Lena", "Lisa", "Julia"]))
        listeVorname.append(vorname)
    return listeVorname

#Nachname_Generator
def function_Nachname_Generator():
    listeNachname = []
    for x in range(testdaten_anzahl):
        nachname = (random.choice(["Schneider", "Müller", "Schmidt", "Fischer", "Hofmann", "Wagner", "Schulz"]))
        listeNachname.append(nachname)
    return listeNachname

#Ort_Generator
def function_Ort_Generator():
    listeOrt = []
    for x in range(testdaten_anzahl):
        ort = (random.choice(function_Textfile_auslesen(orte_textfile, orte_regex)))
        listeOrt.append(ort)
    return listeOrt

#Vergehen_Generator
def function_Vergehen_Generator():
    listeVergehen = []
    for x in range(testdaten_anzahl):
        vergehen = (random.choice(function_Textfile_auslesen(bussgeld_textfile, bussgeld_regex)))
        listeVergehen.append(vergehen)
    return listeVergehen

#Austeller_Generator
def function_Austeller_Generator():
    listeAusteller = []
    for x in range(testdaten_anzahl):
        austeller = (random.choice(["Landeshauptstadt ", "Landkreis ", "Stadt ", "Universitätsstadt ", 
                                    "Regierungspräsidium ", "Kreis ", "Polizeipräsidium ", "Ordnungsamt ", "Städteregion ",
                                    "Stadtverwaltung ", "Rhein-Kreis ", "Seestadt ", "Freie Hansestadt ", "Freie und Hansestadt",
                                    "Landratsamt ", "Stadtamt ", "Altmarkkreis ", "Lutherstadt "])
            + random.choice(["Hamburg", "München", "Berlin", "Bielefeld", "Paderborn", "Frankurt am Main", "Bremen"]))
        listeAusteller.append(austeller)
    return listeAusteller

#Telefon_Generator
def function_Telefon_Generator():
    listeTelefon = []
    for x in range(testdaten_anzahl):
        telefon = (random.choice(["0" + str(random.randint(10,9999)), 
        "+49 " + str(random.randint(1,9999)), 
        "(" + "0" + str(random.randint(10,9999)) + ")"
        ])
        + random.choice(["/"," / ", " ", " - ", "-"])
        + random.choice([str(random.randint(1,999)) 
        + str(random.choice([" ", "-"])) 
        + str(random.randint(1,9999)), 
        str(random.randint(1,999999))]))
        listeTelefon.append(telefon)
    return listeTelefon

#Random_Index_Generator
def get_random_index():
    return random.choice([0, 1, 2, 3, 4, 5])

#Aktenzeichen_Generator
def function_Aktenzeichen_Generator():
    listeAktenzeichen = []
    for x in range(testdaten_anzahl):
        grossbuchstaben = string.ascii_uppercase
        aktenzeichen = [random.choice([''.join(random.choice(grossbuchstaben)), str(random.randint(0,9))])]
        for x in range(random.randrange(5,13)):
            liste = [''.join(random.choice(grossbuchstaben)), str(random.randint(1,9)), "-", "|", "/", "." ]
            index = get_random_index()
            if len(aktenzeichen) > 0:
                while aktenzeichen[len(aktenzeichen)-1] == str(liste[index]):
                    index = get_random_index()
            if (aktenzeichen[len(aktenzeichen)-1] == "-" 
            or aktenzeichen[len(aktenzeichen)-1] == "|" 
            or aktenzeichen[len(aktenzeichen)-1] == "/"
            or aktenzeichen[len(aktenzeichen)-1] == "."):
                index = random.choice([0, 1])
                pass
            aktenzeichen.append(str(liste[index]))
        aktenzeichen += [random.choice([''.join(random.choice(grossbuchstaben)), str(random.randint(0,9))])]
        aktenzeichen = "".join(aktenzeichen)
        listeAktenzeichen.append(aktenzeichen)
    return listeAktenzeichen

