from bs4 import BeautifulSoup
import requests
import csv



liste_url=["https://www.bussgeldkatalog.org/bussgeldstelle/baden-wuerttemberg/","https://www.bussgeldkatalog.org/bussgeldstelle/muenchen/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/berlin/","https://www.bussgeldkatalog.org/bussgeldstelle/nuernberg/","https://www.bussgeldkatalog.org/bussgeldstelle/viechtach/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/straubing/","https://www.bussgeldkatalog.org/bussgeldstelle/polizeiverwaltungsamt-bayern/","https://www.bussgeldkatalog.org/bussgeldstelle/gransee/","https://www.bussgeldkatalog.org/bussgeldstelle/bremen/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/hamburg/","https://www.bussgeldkatalog.org/bussgeldstelle/kassel/","https://www.bussgeldkatalog.org/bussgeldstelle/frankfurt-am-main/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/mecklenburg-vorpommern/","https://www.bussgeldkatalog.org/bussgeldstelle/niedersachsen/","https://www.bussgeldkatalog.org/bussgeldstelle/nordrhein-westfalen/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/speyer/","https://www.bussgeldkatalog.org/bussgeldstelle/st-ingbert/","https://www.bussgeldkatalog.org/bussgeldstelle/sachsen/","https://www.bussgeldkatalog.org/bussgeldstelle/polizeiverwaltungsamt-sachsen/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/sachsen-anhalt/","https://www.bussgeldkatalog.org/bussgeldstelle/polizeidirektion-sachsen-anhalt/","https://www.bussgeldkatalog.org/bussgeldstelle/schleswig-holstein/","https://www.bussgeldkatalog.org/bussgeldstelle/artern/",
                  "https://www.bussgeldkatalog.org/bussgeldstelle/thueringen","https://www.bussgeldkatalog.org/bussgeldstelle/herford/"]      
       
liste_name=[]
liste_anschrift=[]
liste_kontakt=[]



#Iterieren durch die Urls mit den Bußgeldstellen und scrapping der Daten aus den Tabellen

for bußgeldstelle in liste_url:
                response = requests.get(bußgeldstelle)
                soup = BeautifulSoup(response.content)
                for table in soup.findAll("table"):
                        for zeile in table.findAll("tr"):
                                a=1
                                for spalte in zeile.findAll("td"):
                                        print(a)
                                        text = spalte.get_text()
                                        text = text.replace('\u00ad', '')
                                        text = text.replace("\n"," ")
                                        if a <=1:
                                                liste_name.append(text)
                                        elif a <=2:
                                                liste_anschrift.append(text)
                                        elif a <=3:
                                                liste_kontakt.append(text)
                                        a=a+1
                                        print("--------")
                                        print(text)
                                        

                        print("________________________________________________")


csv_input = zip(liste_name,liste_anschrift,liste_kontakt)

with open('bußgeldstellen.csv', 'w', newline='', encoding='utf-8') as new_file:
        csv_writer = csv.writer(new_file, escapechar=' ', quoting=csv.QUOTE_NONE, delimiter=';')
        for x in csv_input:
                csv_writer.writerow(x)




# liste=[]

with open('bußgeldstellen.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        search="www.aalen.de"
        for row in csv_reader:
                if (row[2].find(search) != -1): 
                        print ("Contains given substring ")
                        inx=row[2].find(search)
                        print("row",inx)
                        bußgeldstelle=row[0]
                        print(bußgeldstelle)
                else: 
                         print ("Doesn't contains given substring") 
                # print(row[0],row[1],row[2],)
                








# # for line in table.findAll('tr'):
# #     print(line)
# #     for l in line.findAll('td'):
# #         print(l)