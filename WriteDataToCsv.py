import csv
from DataGenerator import function_Kennzeichen_Generator 
from DataGenerator import function_Tatdatum_Generator
from DataGenerator import function_Briefdatum_Generator
from DataGenerator import function_Uhrzeit_Generator
from DataGenerator import function_Verwarngeld_Generator
from DataGenerator import function_Geburtstag_Generator
from DataGenerator import function_Telefon_Generator
from DataGenerator import function_Anrede_Generator
from DataGenerator import function_Aktenzeichen_Generator
from DataGenerator import function_Vorname_Generator
from DataGenerator import function_Nachname_Generator
from DataGenerator import function_Ort_Generator
from DataGenerator import function_Austeller_Generator
from DataGenerator import function_Vergehen_Generator

#Ingo Speckens

with open('data.csv', 'w', newline='', encoding='utf-8') as new_file:
        #escapechar tritt bei " bei Vergehen auf
        csv_writer = csv.writer(new_file, escapechar='?', quoting=csv.QUOTE_NONE, delimiter='\t')
       
        list_Kennzeichen = function_Kennzeichen_Generator()
        list_Tatdatum = function_Tatdatum_Generator()
        list_Briefdatum = function_Briefdatum_Generator()
        list_Geburtstag = function_Geburtstag_Generator()
        list_Uhrzeit = function_Uhrzeit_Generator()
        list_Verwarngeld = function_Verwarngeld_Generator()
        list_Telefon = function_Telefon_Generator()
        list_Anrede = function_Anrede_Generator()
        list_Aktenzeichen = function_Aktenzeichen_Generator()
        list_Vorname = function_Vorname_Generator()
        list_Nachname = function_Nachname_Generator()
        list_Ort = function_Ort_Generator()
        list_Austeller = function_Austeller_Generator()
        list_Vergehen = function_Vergehen_Generator()
        listen = zip(list_Kennzeichen, list_Tatdatum, list_Briefdatum, list_Geburtstag, list_Uhrzeit,
                     list_Telefon, list_Anrede, list_Verwarngeld, list_Aktenzeichen, list_Vorname, list_Nachname, list_Ort, 
                     list_Austeller, list_Vergehen)

        csv_writer.writerow(['Kennzeichen', 'Tatdatum', 'Briefdatum', 'Geburtstag', 'Uhrzeit', 'Telefon', 'Anrede',
                             'Verwarngeld', 'Aktenzeichen', 'Vorname', 'Nachname', 'Ort', 'Austeller', 'Vergehen'])

        for x in listen:
                csv_writer.writerow(x)



            