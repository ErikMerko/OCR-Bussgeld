import time
import random
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import PageBreak

#Ingo Speckens

count = 1
#Anzahl PDFs die erzeugt werden
while(count < 2):

    #Zeit
    datumJetzt = datetime.now()
    datum = datumJetzt.strftime("%d.%m.%Y")
    datumPdfName = datumJetzt.strftime("%d.%m.%Y %H.%M.%S")

    #name PDF
    namePdf = 'Bussgeldbescheid - %s.pdf' % (str(count) + " - " + datumPdfName)

    #Dokumentenbezeichnung 
    dokument = SimpleDocTemplate(namePdf ,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=50,bottomMargin=18)
    Story=[]

    #Variablen
    kennzeichen = random.choice(["HG VG 1928", "HG/VG/1928", "HG-VG 1928"])
    hersteller = random.choice(["TOYOTA", "BMW", "MERCEDES", "VOLKSWAGEN", "OPEL"])
    uhrzeit = "09:30"
    stadt = "Frankurt"
    strasse = "Miquelallee"
    betrag = random.randint(1,5000)
    betragFMT = random.choice(["EUR", "€", "Euro"])
    zimmerNR = random.randint(1,999)
    
    #Variablen AdresseEmpfänger
    vornameEmpfaenger = "Robert"
    nachnameEmpfaenger = "Schneider"
    nameEmpfaengerArray = [vornameEmpfaenger, nachnameEmpfaenger]
    strassenNameEmpfaenger = "Am Bahnhof"
    hausNrEmpfaenger = "5"
    strasseEmpfaengerArray = [strassenNameEmpfaenger, hausNrEmpfaenger]
    plzEmpfaenger = "61502"
    stadtEmpfaenger = "Berlin" 
    plzStadtEmpfaengerArray = [plzEmpfaenger, stadtEmpfaenger]
    
    #Logo
    logo = "StadtFulda_Logo.jpg"
    bild = Image(logo, 1*inch, 1*inch)
    bild.hAlign = "LEFT"
    
    #Stil
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    #Seite 1 - Anhörung/Fahrerfeststellung

    #Adresse und Sachbearbeiter
    inhaltAdresseSachbearbeiter = [[' '.join(nameEmpfaengerArray), ' ', ' ', ' ', ' ', ' ', 'Auskunft erteilt:', 'Herr Schneider'],
        [' '.join(strasseEmpfaengerArray), ' ', ' ', ' ', ' ', ' ', 'Zimmer:', str(zimmerNR)],
        [' '.join(plzStadtEmpfaengerArray), ' ', ' ', ' ', ' ', ' ', 'Telefon:', '0521 / 124 4287'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'Telefax:', '0521 / 124 4290'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'E-Mail:', 'bussgeldstelle@stadt.fulda.de'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'Datum:', '25.09.2019']]
    tabelleAdresseSachbearbeiter = Table(inhaltAdresseSachbearbeiter, hAlign='LEFT', rowHeights= 12)
    tabelleAdresseSachbearbeiter.setStyle(TableStyle([('ALIGN',(6,0),(-2,-1),'RIGHT'),
                       ('FONTSIZE',(0,0),(-1,-1), 10),
                       ]))

    #Aktenzeichen
    aktenzeichenTxt = '<font size=14><b>Aktenzeichen: </b> 40293.042488-7</font>'

    #Betreff
    betreffTxt = '<font size=14><b>Anhörung / Fahrerfeststellung</b></font>'

    #Anrede
    anredeTxt = '<font size=12>Sehr geehrte Damen und Herren,</font>' #% full_name.split()[0].strip()

    #Verkehrsordnungswidrigkeit
    verkehrsordnungswidrigkeitTxt = '<font size=12>dieses Schreiben ergeht an Sie als Halter des PKW, amtliches Kennzeichen: %s, Hersteller: %s.\
            Der Fahrer dieses Fahrzeuges hat am %s um %s Uhr in %s, %s, folgende Verkehrsordnungswidrigkeit(en) begangen:\
                                                                                        </font>' % (kennzeichen, 
                                                                                                    hersteller,
                                                                                                    datum,
                                                                                                    uhrzeit,
                                                                                                    stadt,
                                                                                                    strasse)
    
    #Geschwindigkeit + Gesetz
    geschwindigkeitGesetzTxt = '<font size=12>Sie überschritten die zulässige Höchstgeschwindigkeit innerhalb geschlossener Ortschaften\
            um 8 km/h in einem verkehrsberuhigten Bereich(Zeichen 321.5, 321.6). Zulässige Geschwindigkeit: 30 km/h.\
            Festgestellte Geschwindigkeit (nach Toleranzabzug): 38 km/h. § 42 Abs. 2 iVm. Anlage 3, § 49 StVO; §24 \
            StVG; 11.3.1 BKat.</font>'

    #Beweismittel
    beweismittelTxt = '<font size=12><b>Beweismittel: </b>Messung mit Lasergerät und Frontfoto, Zeuge Film-Nr. 2025832 Bild-Nr. 89</font>'

    #Zeuge
    zeugeTxt = '<font size=12><b>Zeuge: </b>Herr Kneip</font>'

    #Verwarnungsgeld
    verwarnungsgeldTxt = '<font size=12>Es wird ein Verwarnungsgeld in Höhe von %s %s erhoben(§§ 56,56 OWiG).</font>' % (format(betrag, '.2f').replace('.', ','), betragFMT)

    #Hinweise und Gruß
    hinweiseGrussTxt = '<font size=12>Wir bitten die weiteren Hinweise in der Anlage zu beachten. <br/> <br/> \
                            Im Auftrag <br/> <br/> \
                            Schneider</font>'

    #Unterschrift
    unterschriftTxt = '<font size=9>- Dieses Schreiben wurde maschinell erstellt und trägt keine Unterschrift -</font>'

    #Fussnote
    inhaltFussnote = [[' ', ' ' , ' ' , ' ', ' ' , ' ' , ' ', ' '],
        ['Postanschrift', ' ' , ' ' , 'Bankverbindung', ' ' , ' ' , 'Öffnungszeiten', ' '],
        ['Stadtverwaltung Fulda', ' ' , ' ' , 'Sparkasse Fulda', ' ' , ' ' , 'Montag und Dienstag', '08:00 - 12:00 '],
        ['-Ordnungsamt-', ' ' , ' ' , 'IBAN DE23530501800012345678', ' ' , ' ' , 'Mittwoch', '08:00 - 16:30'],
        ['Alexander-Erhard-Strasse 3', ' ' , ' ' , 'BIC HELADEF1FDS', ' ' , ' ' , 'Donnerstag und Freitag', '08:00 - 12:00'],
        ['50295 Fulda', ' ' , ' ' , ' ', ' ' , ' ' , ' ', ' ']]
    tabelleFussnote = Table(inhaltFussnote, hAlign='LEFT', rowHeights= 8)
    tabelleFussnote.setStyle(TableStyle([('ALIGN',(0,0),(0,-1),'RIGHT'),
                        ('LINEABOVE',(0,0),(-1,0), 1, colors.black),
                        ('FONTSIZE',(0,0),(-1,-1), 8),
                       ]))

    listTexts = [aktenzeichenTxt, betreffTxt, anredeTxt, verkehrsordnungswidrigkeitTxt, geschwindigkeitGesetzTxt, \
        beweismittelTxt, zeugeTxt, verwarnungsgeldTxt, hinweiseGrussTxt, unterschriftTxt, tabelleAdresseSachbearbeiter, \
        bild, tabelleFussnote]
    listTextsLength = len(listTexts)

    while (len(listTexts) > 0):
        txt = random.choice(listTexts)
        if(txt == tabelleAdresseSachbearbeiter or txt == bild or txt == tabelleFussnote):
            Story.append(txt)
            Story.append(Spacer(1, 12))
        elif(txt != tabelleAdresseSachbearbeiter):
            Story.append(Paragraph(txt,styles["Justify"]))
        listTexts.remove(txt)
        Story.append(Spacer(1, 12))

    Story.append(PageBreak())

    #Seite 2 - Anhörungsbogen
    
    #Aktenzeichen
    aktenzeichenTxt = '<font size=12>Aktenzeichen: <b>40293.042488-7</b></font>'

    #Anhöhrungsbogen Überschrift
    anhörungsbogenUeberschriftText = '<font size=14><b>Anhöhrungsbogen zum Vorwurf einer Ordnungswidrigkeit (§ 55 OWiG)</b></font>'

    #Anhöhrungsbogen Text,
    anhörungsbogenText = '<font size=12> Nach § 55 OWiG wird Ihnen hiermit Gelegenheit gegeben, sich zu dem Vorwurf zu äußern. <br/><br/> \
            Es steht Ihnen frei, sich zu der Beschuldigung zu äußern oder nicht zur Sache auszusagen. Sie sind aber in jedem Fall - auch \
            wenn Sie die Ordnungswidigkeit nicht begangen haben - verpflichtet, die Fragen zur Person (Nr. 1) vollständig und richtig \
            zu beantworten und den insoweit ausgefüllten Fragebogen innerhalb einer (ab Zugang dieses Schreiben) zurückzusenden; \
            die Verletzung dieser Pflicht ist nach $111 OWiG mit Geldbuße bedroht. <br/> \
            Sofern Sie sich nicht zu dem Vorwurf äußern, wird davon ausgegangen, dass Sie von Ihrem Äußerungsrecht keinen Gebrauch \
            machen wollen. Es wird dann eine Fahrzeugführerermittlung durchgeführt. Wenn Sie die Ordnungswidrigkeit nicht begangen \
            haben, teilen Sie uns innerhalb einer Woche ab Zugang dieses Schreibens neben Ihren Personalien zustäzlich die \
            Personalien des Verantwortlichen unter den Angaben Nr. 2 mit, hier sind Sie nicht verpflichtet. <br/> \
            Im Übringen kann dem Haltes eines Kfz bei Verkehrverstößen die Führung eines Fahrtenbuches auferlegt werden, \
            wenn nicht festgestellt werden kann, wer zur Tatzeit dsa Fahrzeug geführt hat (§ 31 a StVZO).</font>'

    listTextsAnhoerungsbogen = [aktenzeichenTxt, anhörungsbogenUeberschriftText, anhörungsbogenText]
    listTextsLength = len(listTextsAnhoerungsbogen)

    while (len(listTextsAnhoerungsbogen) > 0):
        txt = random.choice(listTextsAnhoerungsbogen)
        Story.append(Paragraph(txt,styles["Justify"]))
        listTextsAnhoerungsbogen.remove(txt)
        Story.append(Spacer(1, 12))


    dokument.build(Story)
    count = count + 1