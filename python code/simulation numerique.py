from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment
import os, sys

#fonction qui permet de mettre en forme le fichier xml avec les indexations
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#non du fichier xml que l'on veut creer
file_name = 'simulation numerique'
file_name_txt = file_name + ".txt"
file_name_xml = file_name + ".XML"
adresse = "Desktop/projet quiz/"



nom_question = 'simulation numerique'
intitule_question = 'combien ??'

note_par_defaut = '3'

feedback_general = 'le feedback general'

penalite = '1'

bonne_reponse = '12'
tolerance_bonne_reponse = '0.5'
feedback_bonne_reponse = 'feedback pour la reponse'

autre_reponse1 = ''
tolerance1 = ''
pourcentage1 = ''
feedback_autre_reponse1 = ''

autre_reponse2= '4'
tolerance2 = '0.5'
pourcentage2 = '50'
feedback_autre_reponse2 = 'feedback de la reponse 2'

unite = 'm'
penalite_unite = '0.1'

#'top' va contenir tout le document xml 
top = Element('quiz')

#on ajoute toutes les lignes du documents
comment = Comment('question: 0')
top.append(comment)

question = SubElement(top, 'question')
question.set('type','category')

category = SubElement(question,'category')

text  = SubElement(category,'text')
text.text = 'top'

comment = Comment('question: numerique')
top.append(comment)

question = SubElement(top, 'question')
question.set('type','numerical')

name = SubElement(question,'name')

text = SubElement(name,'text')
text.text = nom_question

questiontext = SubElement(question,'questiontext')
questiontext.set('format','html')

text=SubElement(questiontext,'text')
#text.text = '<![CDATA[<p>' + intitule_question + '</p>]]>'

generalfeedback = SubElement(question,'generalfeedback')
generalfeedback.set('format','html')

text = SubElement(generalfeedback,'text')
text.text = feedback_general

defaultgrade = SubElement(question,'defaultgrade')
defaultgrade.text = note_par_defaut

penalty = SubElement(question,'penalty')
penalty.text = penalite

hidden= SubElement(question,'hidden')
hidden.text = '0'

answer = SubElement(question,'answer')
answer.set('fraction','100')

text = SubElement(answer,'text')
text.text = bonne_reponse

feedback = SubElement(answer,'feedback')
feedback.set('format','html')

text = SubElement(feedback,'text')
text.text = feedback_bonne_reponse

tolerance = SubElement(answer,'tolerance')
tolerance.text = tolerance_bonne_reponse

if autre_reponse1 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage1)

    text = SubElement(answer,'text')
    text.text = autre_reponse1

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback_autre_reponse1

    tolerance = SubElement(answer,'tolerance')
    tolerance.text = tolerance1

if autre_reponse2 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage2)

    text = SubElement(answer,'text')
    text.text = autre_reponse2

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback_autre_reponse2

    tolerance = SubElement(answer,'tolerance')
    tolerance.text = tolerance2

units=SubElement(question,'units')

unit = SubElement(units,'unit')

multiplier = SubElement(unit,'multiplier')
multiplier.text = '1'

unit_name = SubElement(unit,'unit_name')
unit_name.text = unite

unitgradingtype = SubElement(question,'unitgradingtype')
unitgradingtype.text = '0'

unitpenalty = SubElement(question,'unitpenalty')
unitpenalty.text = penalite_unite

shownunits = SubElement(question,'shownunits')
shownunits.text = '0'

unitsleft = SubElement(question,'unitsleft')
unitsleft.text = "0"

#on cree un fichier txt qui contient toute les lignes du fichier xml que l'on va creer
fichier = open(adresse + file_name_txt, "w")
fichier.write(prettify(top))
fichier.close()

#on rajoute ' encoding="UTF-8" ' dans la premiere ligne 
fichier = open(adresse + file_name_txt, "r")
lignes= fichier.readlines()
fichier = open(adresse + file_name_txt, "w")
lignes[0] = '<?xml version="1.0" encoding="UTF-8"?>\n'
fichier.writelines(lignes)
fichier.close()

#on remplace les &lt; et les &gt; par < et > dans le fichier
f=open(adresse + file_name_txt,'r')
chaine=f.read().replace('&lt;','<')
chaine = chaine.replace ('&gt;','>')
f.close() 
f=open(adresse + file_name_txt,'w') 
f.write(chaine) 
f.close()

#on transforme le fichier txt en fichier xml
if os.path.exists(adresse + file_name_xml):
    os.remove(adresse + file_name_xml)
os.rename(adresse + file_name_txt, adresse + file_name_xml)