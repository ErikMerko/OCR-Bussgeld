import time
import random
import string
from datetime import datetime
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import PageBreak

from reportlab.lib import utils
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Frame, Image
#Fusszeile
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph

#Ingo Speckens

zaehlerPdf = 1
#Anzahl PDFs die erzeugt werden
while(zaehlerPdf < 2):

    #Zeit
    datumJetzt = datetime.now()
    datumPdfName = datumJetzt.strftime("%d.%m.%Y %H.%M.%S")

    #name PDF
    namePdf = 'Bussgeldbescheid - %s.pdf' % (str(zaehlerPdf) + " - " + datumPdfName)

    #Dokumentenbezeichnung 
    dokument = SimpleDocTemplate(namePdf ,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=50,bottomMargin=18)
    Story = []

    #Generators ggf. in andere Klassen auslagern
    #Kennzeichengenerator
    grossbuchstaben = string.ascii_uppercase
    kennzeichenGenerator = (''.join(random.choice(grossbuchstaben) for i in range(random.randint(1,3))) 
    + random.choice([' ', ' -', '-']) 
    + ''.join(random.choice(grossbuchstaben) for i in range(random.randint(1,2)))
    + " "
    + str(random.randint(1,9999)))
    #print(kennzeichen)

    #Datumgenerator
    monat = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
    if monat !='02' or monat !='04' or monat !='05' or monat !='09' or monat !='11':
        tag = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
    if monat =='02':
        tag = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'])
    if monat =='04' or monat =='05' or monat =='09' or monat =='11':
        tag = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])

    datumGenerator = (random.choice(['', 'am ']) 
    + str(tag)
    + "."
    + str(monat)
    + "."
    + random.choice(['2019 ', '19 ', '2020 ', '20 ']))
    #print(datum)

    #Uhrzeitgenerator
    uhrzeitGenerator = (random.choice(['', 'um '])
    + random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '1', '2', '3', '4', '5', '6', '7', '8', '9',])
    + ":"
    + str(random.randint(0,5))
    + str(random.randint(0,9))
    + random.choice([' ', ' Uhr ']))
    #print(uhrzeit)

    #Verwarngeldgenerator
    betrag = random.randint(1,5000)
    verwarngeldGenerator = (format(betrag, '.2f').replace('.', ',') 
    + random.choice([" EUR ", " € "]))
    #print(verwarngeld)

    #Variablen Tatort
    hersteller = random.choice(["TOYOTA"])
    stadt = "Fulda"
    strasse = "Miquelallee 128"
    zimmerNR = random.randint(1,999)
    aktenzeichen = "40293.042488-7"
    zulaessigeGeschwindigkeit = random.choice(["30", "50", "70", "100", "120"])
    ueberschriteneGeschwindigkeit = random.randint(6,100)
    festgestellteGeschwindigkeit = int(zulaessigeGeschwindigkeit) + ueberschriteneGeschwindigkeit
    
    #Variablen AdresseEmpfänger
    vornameEmpfaenger = "Robert "
    nachnameEmpfaenger = "Schneider"
    nameEmpfaengerArray = [vornameEmpfaenger, nachnameEmpfaenger]
    strassenNameEmpfaenger = "Am Bahnhof "
    hausNrEmpfaenger = "5"
    strasseEmpfaengerArray = [strassenNameEmpfaenger, hausNrEmpfaenger]
    plzEmpfaenger = "61502 "
    stadtEmpfaenger = "Berlin" 
    plzStadtEmpfaengerArray = [plzEmpfaenger, stadtEmpfaenger]
    
    #Stil
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    #Stil2
    styles2 = getSampleStyleSheet()
    styles2.add(ParagraphStyle(name='RIGHT', alignment=TA_RIGHT))

    #fusszeileStil
    styleN = styles['Normal']
    styleH = styles['Heading1']

    #Seite 1 - Anhörung/Fahrerfeststellung

    #Logo und Ueberschrift
    def get_image(path, width=1*cm):
        img = utils.ImageReader(r'C:\Users\soc4real\TesseractData\StadtFulda_Logo.jpg')
        iw, ih = img.getSize()
        aspect = ih / float(iw)
        return Image(r'C:\Users\soc4real\TesseractData\StadtFulda_Logo.jpg', width=width, height=(width * aspect))

    ueberschriftTxt = 'Stadtverwaltung'

    #21*6 Tabelle
    inhaltLogoUeberschrift = [  [ueberschriftTxt, '', '', '', '', '' , '', '', '', '', '', '' , '', '', '', '', '', '', '', '', ''],
                                ['', '', '', '', '', '' , '', '', '', '', '', '', '', '', '' , '', '', '', '', '', ''],
                                ['', '', '', '', '', '' , '', '', '', '', '', '' , '', '', '', '', '', '', '', '', ''],
                                [stadt, '', '', '', '', '' , '', '', '', '', '' , '', '', '', '', '', '', '', '', '', ''],
                                ['', '', '', '', '', '' , '', '', '', '', '', '' , '', '', '', '', '', '', '', '', ''],
                                ['', '', '', '', '', '' , '', '', '', '', '', '', '' , '', '', '', '', '', '', '', [get_image('StadtFulda_Logo.jpg', width=4*cm)]]]
    tabelleLogoUeberschrift = Table(inhaltLogoUeberschrift, hAlign='RIGHT', rowHeights= 12)
    tabelleLogoUeberschrift.setStyle(TableStyle([('ALIGN',(0,0),(0,0), 'CENTER'),
                    ('VALIGN',(0,0),(0,0),'TOP'),
                    ('FONTNAME',(0,0),(0,3), 'Helvetica-Bold'),
                    ('FONTSIZE',(0,0),(0,0), 24),
                    ('SPAN',(0,0),(13,2)),
                    ('ALIGN',(0,3),(0,3), 'CENTER'),
                    ('VALIGN',(0,3),(0,3),'TOP'),
                    ('FONTSIZE',(0,3),(0,3), 24),
                    ('SPAN',(0,3),(13,4))
                    ]))
    Story.append(tabelleLogoUeberschrift)
    Story.append(Spacer(1, 12))

    #Stadtverwaltung
    stadtverwaltungTxt = '<font size=8><u>Stadtverwaltung Fulda - Amt 31.12.35 - Postfach 21 35 31 -</u><br/> \
                            <b>AZ %s</b></font>' %(aktenzeichen)
    # später löschen
    Story.append(Paragraph(stadtverwaltungTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Adresse und Sachbearbeiter
    #23*5 Tabelle
    inhaltAdresseSachbearbeiter = [[''.join(nameEmpfaengerArray), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Auskunft erteilt:', 'Herr Schneider'],
        [''.join(strasseEmpfaengerArray), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Zimmer:', str(zimmerNR)],
        [''.join(plzStadtEmpfaengerArray), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Telefon:', '0521 / 124 4287'],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Telefax:', '0521 / 124 4290'],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', 'E-Mail:', 'bussgeldstelle@stadt.fulda.de'],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Datum:', '25.09.2019']]
    tabelleAdresseSachbearbeiter = Table(inhaltAdresseSachbearbeiter, hAlign='LEFT', rowHeights= 12)
    tabelleAdresseSachbearbeiter.setStyle(TableStyle([('ALIGN',(-1,-6),(-1,-1),'LEFT'),
                        ('ALIGN',(-2,-6),(-2,-1),'RIGHT'),
                        ('FONTSIZE',(0,0),(0,2), 10),
                        ('FONTSIZE',(-2,-6),(-1,-1), 9),
                        #('LINEBELOW',(22,4),(-1,-2), 1, colors.black),
                        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                        ('SPAN',(0,0),(12,0)),
                        ('SPAN',(0,1),(12,1)),
                        ('SPAN',(0,2),(12,2)),
                        ('SPAN',(0,3),(12,3)),
                        ('SPAN',(0,3),(12,4)),
                        #('BACKGROUND',(0,0),(12,0), colors.pink),
                        ]))
    # später löschen
    Story.append(tabelleAdresseSachbearbeiter)
    Story.append(Spacer(1, 12))

    #Aktenzeichen
    #aktenzeichenTxt = '<font size=14><b>Aktenzeichen: </b> 40293.042488-7</font>'
    # später löschen
    #Story.append(Paragraph(aktenzeichenTxt,styles2["RIGHT"]))
    #Story.append(Spacer(1, 12))

    #19*2
    inhaltAktenzeichen = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Aktenzeichen', aktenzeichen],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Bitte immer angeben!']]
    tabelleAktenzeichen = Table(inhaltAktenzeichen, hAlign='RIGHT', rowHeights= 12)
    tabelleAktenzeichen.setStyle(TableStyle([('ALIGN',(18,0),(18,0),'CENTER'),
                        ('ALIGN',(17,0),(17,0),'RIGHT'),
                        ('FONTSIZE',(0,0),(-1,-1), 11),
                        ('FONTSIZE',(18,1),(18,1), 9),
                        ('FONT',(18,1),(18,1), 'Helvetica-Oblique'),
                        ('FONTNAME',(17,0),(18,0), 'Helvetica-Bold'),
                        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                        #('BACKGROUND',(18,0),(18,0), colors.pink),
                        ('BOX',(18,0),(18,0), 0.25, colors.black),
                        ]))
    # später löschen
    Story.append(tabelleAktenzeichen)
    Story.append(Spacer(1, 12))

    #Betreff
    betreffTxt = '<font size=11><b>Anhörung / Fahrerfeststellung</b></font>'
    # später löschen
    Story.append(Paragraph(betreffTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Anrede
    anredeTxt = '<font size=10>Sehr geehrte Damen und Herren,</font>' #% full_name.split()[0].strip()
    # später löschen
    Story.append(Paragraph(anredeTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Verkehrsordnungswidrigkeit
    verkehrsordnungswidrigkeitTxt = '<font size=10>dieses Schreiben ergeht an Sie als Halter des PKW, amtliches Kennzeichen: %s, Hersteller: %s.\
            Der Fahrer dieses Fahrzeuges hat %s %s in %s, %s, folgende Verkehrsordnungswidrigkeit(en) begangen:\
                                                                                        </font>' % (kennzeichenGenerator, 
                                                                                                    hersteller,
                                                                                                    datumGenerator,
                                                                                                    uhrzeitGenerator,
                                                                                                    stadt,
                                                                                                    strasse)
    # später löschen
    Story.append(Paragraph(verkehrsordnungswidrigkeitTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))                                                                                                
    
    #Geschwindigkeit + Gesetz
    geschwindigkeitGesetzTxt = '<font size=10>Sie überschritten die zulässige Höchstgeschwindigkeit innerhalb geschlossener Ortschaften\
            um %s km/h in einem verkehrsberuhigten Bereich(Zeichen 321.5, 321.6). Zulässige Geschwindigkeit: %s km/h.\
            Festgestellte Geschwindigkeit (nach Toleranzabzug): %s km/h. § 42 Abs. 2 iVm. Anlage 3, § 49 StVO; §24 \
            StVG; 11.3.1 BKat.</font>' % (ueberschriteneGeschwindigkeit, zulaessigeGeschwindigkeit, festgestellteGeschwindigkeit)
    # später löschen
    Story.append(Paragraph(geschwindigkeitGesetzTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Beweismittel
    beweismittelTxt = '<font size=10><b>Beweismittel: </b>Messung mit Lasergerät und Frontfoto, Zeuge Film-Nr. 2025832 Bild-Nr. 89</font>'
    # später löschen
    Story.append(Paragraph(beweismittelTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Zeuge
    zeugeTxt = '<font size=10><b>Zeuge: </b>Herr Kneip</font>'
    # später löschen
    Story.append(Paragraph(zeugeTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Verwarnungsgeld
    verwarnungsgeldTxt = '<font size=10>Es wird ein Verwarnungsgeld in Höhe von <b>%s</b> erhoben(§§ 56,56 OWiG).</font>' % (verwarngeldGenerator)
    # später löschen
    Story.append(Paragraph(verwarnungsgeldTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Hinweise und Gruß
    hinweiseGrussTxt = '<font size=10>Wir bitten die weiteren Hinweise in der Anlage zu beachten. <br/> <br/> \
                            Im Auftrag <br/> <br/> \
                            Schneider</font>'
    # später löschen
    Story.append(Paragraph(hinweiseGrussTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Unterschrift
    unterschriftTxt = '<font size=9>- Dieses Schreiben wurde maschinell erstellt und trägt keine Unterschrift -</font>'
    # später löschen
    Story.append(Paragraph(unterschriftTxt,styles["Justify"]))
    Story.append(Spacer(1, 12))

    #Fussnote
    #8*6 Tabelle
    inhaltFussnote = [[' ', ' ' , ' ' , ' ', ' ' , ' ' , ' ', ' '],
        ['Postanschrift', ' ' , ' ' , 'Bankverbindung', ' ' , ' ' , 'Öffnungszeiten', ' '],
        ['Stadtverwaltung Fulda', ' ' , ' ' , 'Sparkasse Fulda', ' ' , ' ' , 'Montag und Dienstag', '08:00 - 12:00 '],
        ['-Ordnungsamt-', ' ' , ' ' , 'IBAN DE23530501800012345678', ' ' , ' ' , 'Mittwoch', '08:00 - 16:30'],
        ['Alexander-Erhard-Strasse 3', ' ' , ' ' , 'BIC HELADEF1FDS', ' ' , ' ' , 'Donnerstag und Freitag', '08:00 - 12:00'],
        ['50295 Fulda', ' ' , ' ' , ' ', ' ' , ' ' , ' ', ' ']]
    tabelleFussnote = Table(inhaltFussnote, hAlign='LEFT', rowHeights= 8)
    tabelleFussnote.setStyle(TableStyle([('ALIGN',(0,0),(0,-1),'RIGHT'),
                        ('ALIGN',(0,0),(-8,-1),'LEFT'),
                        ('LINEABOVE',(0,0),(-1,0), 1, colors.black),
                        ('FONTSIZE',(0,0),(-1,-1), 8),
                       ]))

    #footer
    def footer(canvas, dokument):
        canvas.saveState()
        #P = Paragraph("This is a multi-line footer.  It goes on every page.  " * 5,
        #            styleN)
        w, h = tabelleFussnote.wrap(dokument.width, dokument.bottomMargin)
        tabelleFussnote.drawOn(canvas, dokument.leftMargin, h)
        canvas.restoreState()
    frame = Frame(dokument.leftMargin, dokument.bottomMargin, dokument.width, dokument.height,
               id='normal')
    template = PageTemplate(id='fusszeile', frames=frame, onPage=footer)
    dokument.addPageTemplates([template])

    # listTexts = [aktenzeichenTxt, betreffTxt, anredeTxt, verkehrsordnungswidrigkeitTxt, geschwindigkeitGesetzTxt, \
    #     beweismittelTxt, zeugeTxt, verwarnungsgeldTxt, hinweiseGrussTxt, unterschriftTxt, tabelleAdresseSachbearbeiter, \
    #     bild, tabelleFussnote]
    # listTextsLength = len(listTexts)

    # while (len(listTexts) > 0):
    #     txt = random.choice(listTexts)
    #     if(txt == tabelleAdresseSachbearbeiter or txt == bild or txt == tabelleFussnote):
    #         Story.append(txt)
    #         Story.append(Spacer(1, 12))
    #     elif(txt != tabelleAdresseSachbearbeiter):
    #         Story.append(Paragraph(txt,styles["Justify"]))
    #     listTexts.remove(txt)
    #     Story.append(Spacer(1, 12))

    #Story.append(PageBreak())

    #Seite 2 - Anhörungsbogen
    
    #Aktenzeichen
    aktenzeichenTxt = '<font size=12>Aktenzeichen: <b>40293.042488-7</b></font>'
        # später löschen
    #Story.append(Paragraph(aktenzeichenTxt,styles["Justify"]))
    #Story.append(Spacer(1, 12))

    #Anhöhrungsbogen Überschrift
    anhörungsbogenUeberschriftText = '<font size=11><b>Anhöhrungsbogen zum Vorwurf einer Ordnungswidrigkeit (§ 55 OWiG)</b></font>'
        # später löschen
    #Story.append(Paragraph(anhörungsbogenUeberschriftText,styles["Justify"]))
    #Story.append(Spacer(1, 12))

    #Anhöhrungsbogen Text,
    anhörungsbogenText = '<font size=10> Nach § 55 OWiG wird Ihnen hiermit Gelegenheit gegeben, sich zu dem Vorwurf zu äußern. <br/><br/> \
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
        # später löschen
    #Story.append(Paragraph(anhörungsbogenText,styles["Justify"]))
    #Story.append(Spacer(1, 12))

    # listTextsAnhoerungsbogen = [aktenzeichenTxt, anhörungsbogenUeberschriftText, anhörungsbogenText]
    # listTextsLength = len(listTextsAnhoerungsbogen)

    # while (len(listTextsAnhoerungsbogen) > 0):
    #     txt = random.choice(listTextsAnhoerungsbogen)
    #     Story.append(Paragraph(txt,styles["Justify"]))
    #     listTextsAnhoerungsbogen.remove(txt)
    #     Story.append(Spacer(1, 12))

    dokument.build(Story)
    zaehlerPdf = zaehlerPdf + 1