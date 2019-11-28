import random 
import string
import re

#Ingo Speckens

testdaten_anzahl = 50

kennzeichen_textfile = 'resources/KFZ-Kennzeichen.txt'
kennzeichen_regex = '^([A-ZÄÖÜ]{1,3})\s*$'

bussgeld_textfile = 'resources/BussgeldformulierungenCSV.txt'
bussgeld_regex = '[A-zäöü].*?[\.!?][\n]'

orte_textfile = 'resources/Orte.txt'
orte_regex = '[A-zäöü]+.*'

#Erstellt aus einem Pfad und einem Regex eine Liste
def function_textfile_auslesen(pfad, regex):
    with open(pfad, 'r', encoding='UTF-8') as kfz:
    
        liste_textfile = []
        liste_textfile_ok = []
        for zeile in kfz:
            liste_match = re.findall(regex, zeile)
            match = ''.join(liste_match)
            #\n entfernen da sich python und regex \n teilen
            remove_char = match.replace('\n','')
            liste_textfile.append(remove_char)
        #zero-length-strings entfernen
        liste_textfile_ok = [i for i in liste_textfile if i]
        return liste_textfile_ok



#Kennzeichen_generator
def function_kennzeichen_generator():

    liste_kennzeichen = []
    for x in range(testdaten_anzahl):
        grossbuchstaben = string.ascii_uppercase
        kennzeichen = (random.choice(function_textfile_auslesen(kennzeichen_textfile, kennzeichen_regex))
        + random.choice([' ', ' -', '-']) 
        + ''.join(random.choice(grossbuchstaben) for i in range(random.randint(1,2)))
        + " "
        + str(random.randint(1,9999)))
        liste_kennzeichen.append(kennzeichen)
    return liste_kennzeichen

#Tatdatum_generator
def function_tatdatum_generator():
    liste_datum = []
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

        datum = (str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['2019', '19']))
        liste_datum.append(datum)
    return liste_datum

#Briefdatum_generator
def function_briefdatum_generator():
    liste_datum = []
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

        datum = (str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['2019', '19']))
        liste_datum.append(datum)
    return liste_datum

#Geburtstag_generator
def function_geburtstag_generator():
    liste_datum = []
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

        datum = (str(tag)
        + "."
        + str(monat)
        + "."
        + random.choice(['1997', '97', '1998', '98', '1999', '99', '2000', '00']))
        liste_datum.append(datum)
    return liste_datum

#Uhrzeit_generator
def function_uhrzeit_generator():
    liste_uhrzeit = []
    for x in range(testdaten_anzahl):
        uhrzeit = (random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08','09', '10', 
                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                  '21', '22', '23', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        + ":"
        + str(random.randint(0,5))
        + str(random.randint(0,9)))
        liste_uhrzeit.append(uhrzeit)
    return liste_uhrzeit

#Verwarngeld_generator
def function_verwarngeld_generator():
    liste_verwarngeld = []
    for x in range(testdaten_anzahl):
        betrag = random.randint(1,5000)
        verwarngeld = ("{:,.2f}".format(betrag).replace(",", "X").replace(".", ",").replace("X", "."))
        liste_verwarngeld.append(verwarngeld)
    return liste_verwarngeld

#Anrede_generator
def function_anrede_generator():
    liste_anrede = []
    for x in range(testdaten_anzahl):
        anrede = (random.choice(["Herr", "Frau"]))
        liste_anrede.append(anrede)
    return liste_anrede

#Vorname_generator
def function_vorname_generator():
    liste_vorname = []
    for x in range(testdaten_anzahl):
        vorname = (random.choice(["Thomas", "Steffen", "Ben", "Lena", "Lisa", "Julia"]))
        liste_vorname.append(vorname)
    return liste_vorname

#Nachname_generator
def function_nachname_generator():
    liste_nachname = []
    for x in range(testdaten_anzahl):
        nachname = (random.choice(["Schneider", "Müller", "Schmidt", "Fischer", "Hofmann", "Wagner", "Schulz"]))
        liste_nachname.append(nachname)
    return liste_nachname

#Ort_generator
def function_ort_generator():
    liste_ort = []
    for x in range(testdaten_anzahl):
        ort = (random.choice(function_textfile_auslesen(orte_textfile, orte_regex)))
        liste_ort.append(ort)
    return liste_ort

#Vergehen_generator
def function_vergehen_generator():
    liste_vergehen = []
    for x in range(testdaten_anzahl):
        vergehen = (random.choice(function_textfile_auslesen(bussgeld_textfile, bussgeld_regex)))
        liste_vergehen.append(vergehen)
    return liste_vergehen

#Austeller_generator
def function_austeller_generator():
    liste_austeller = []
    for x in range(testdaten_anzahl):
        austeller = (random.choice(["Landeshauptstadt ", "Landkreis ", "Stadt ", "Universitätsstadt ", 
                                    "Regierungspräsidium ", "Kreis ", "Polizeipräsidium ", "Ordnungsamt ", "Städteregion ",
                                    "Stadtverwaltung ", "Rhein-Kreis ", "Seestadt ", "Freie Hansestadt ", "Freie und Hansestadt",
                                    "Landratsamt ", "Stadtamt ", "Altmarkkreis ", "Lutherstadt "])
            + random.choice(["Hamburg", "München", "Berlin", "Bielefeld", "Paderborn", "Frankurt am Main", "Bremen"]))
        liste_austeller.append(austeller)
    return liste_austeller

#Telefon_generator
def function_telefon_generator():
    liste_telefon = []
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
        liste_telefon.append(telefon)
    return liste_telefon

#Random_Index_generator
def get_random_index():
    return random.choice([0, 1, 2, 3, 4, 5])

#Aktenzeichen_generator
def function_aktenzeichen_generator():
    liste_aktenzeichen = []
    for x in range(testdaten_anzahl):
        grossbuchstaben = string.ascii_uppercase
        aktenzeichen = [random.choice([''.join(random.choice(grossbuchstaben)), str(random.randint(0,9))])]
        for x in range(random.randrange(5,13)):
            liste = [''.join(random.choice(grossbuchstaben)), str(random.randint(1,9)), "-", "|", "/", "." ]
            index = get_random_index()
            if len(aktenzeichen) > 0:
                while aktenzeichen[len(aktenzeichen)-1] == str(liste[index]):
                    index = get_random_index()
            #Pruefen ob -, |, /, . schon benutzt wurden
            if (aktenzeichen[len(aktenzeichen)-1] == "-" 
            or aktenzeichen[len(aktenzeichen)-1] == "|" 
            or aktenzeichen[len(aktenzeichen)-1] == "/"
            or aktenzeichen[len(aktenzeichen)-1] == "."):
                index = random.choice([0, 1])
                pass
            aktenzeichen.append(str(liste[index]))
        aktenzeichen += [random.choice([''.join(random.choice(grossbuchstaben)), str(random.randint(0,9))])]
        aktenzeichen = "".join(aktenzeichen)
        liste_aktenzeichen.append(aktenzeichen)
    return liste_aktenzeichen

