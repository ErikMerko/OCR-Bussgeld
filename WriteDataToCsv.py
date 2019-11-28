import csv
from DataGenerator import function_kennzeichen_generator 
from DataGenerator import function_tatdatum_generator
from DataGenerator import function_briefdatum_generator
from DataGenerator import function_uhrzeit_generator
from DataGenerator import function_verwarngeld_generator
from DataGenerator import function_geburtstag_generator
from DataGenerator import function_telefon_generator
from DataGenerator import function_anrede_generator
from DataGenerator import function_aktenzeichen_generator
from DataGenerator import function_vorname_generator
from DataGenerator import function_nachname_generator
from DataGenerator import function_ort_generator
from DataGenerator import function_austeller_generator
from DataGenerator import function_vergehen_generator

#Ingo Speckens

with open('data.csv', 'w', newline='', encoding='utf-8') as new_file:
        #escapechar tritt bei " bei Vergehen auf
        csv_writer = csv.writer(new_file, escapechar='?', quoting=csv.QUOTE_NONE, delimiter='\t')
       
        liste_kennzeichen = function_kennzeichen_generator()
        liste_tatdatum = function_tatdatum_generator()
        liste_briefdatum = function_briefdatum_generator()
        liste_geburtstag = function_geburtstag_generator()
        liste_uhrzeit = function_uhrzeit_generator()
        liste_verwarngeld = function_verwarngeld_generator()
        liste_telefon = function_telefon_generator()
        liste_anrede = function_anrede_generator()
        liste_aktenzeichen = function_aktenzeichen_generator()
        liste_vorname = function_vorname_generator()
        liste_nachname = function_nachname_generator()
        liste_ort = function_ort_generator()
        liste_austeller = function_austeller_generator()
        liste_vergehen = function_vergehen_generator()
        listen = zip(liste_kennzeichen, liste_tatdatum, liste_briefdatum, liste_geburtstag, liste_uhrzeit,
                     liste_telefon, liste_anrede, liste_verwarngeld, liste_aktenzeichen, liste_vorname, liste_nachname, liste_ort, 
                     liste_austeller, liste_vergehen)

        csv_writer.writerow(['Kennzeichen', 'Tatdatum', 'Briefdatum', 'Geburtstag', 'Uhrzeit', 'Telefon', 'Anrede',
                             'Verwarngeld', 'Aktenzeichen', 'Vorname', 'Nachname', 'Ort', 'Austeller', 'Vergehen'])

        for x in listen:
                csv_writer.writerow(x)



            