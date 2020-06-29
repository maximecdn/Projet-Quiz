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
file_name = 'simulation reponse courte'
file_name_txt = file_name + ".txt"
file_name_xml = file_name + ".XML"



nom_question = 'simulation reponse courte'
intitule_question = 'repondez...'

note_par_defaut = '3'

feedback_general = 'le feedback general'

penalite = '1'

reponse1 = 'oui'
feedback1 = ''
pourcentage1 = '100'

reponse2 = 'yes*'
feedback2 = ''
pourcentage2 = '100'

reponse3 = ''
feedback3 = ''
pourcentage3 = ''

majuscule = 'oui'


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

comment = Comment('question: reponse courte')
top.append(comment)

question = SubElement(top, 'question')
question.set('type','shortanswer')

name = SubElement(question,'name')

text = SubElement(name,'text')
text.text = nom_question

questiontext = SubElement(question,'questiontext')
questiontext.set('format','html')

text=SubElement(questiontext,'text')
text.text = '<![CDATA[<p>' + intitule_question + '</p>]]>'

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

usecase = SubElement(question,'usecase')
if majuscule == 'oui' :
    usecase.text = '1'
else :
    usecase.text = '0'

answer = SubElement(question,'answer')
answer.set('fraction',pourcentage1)
answer.set('format','moodle_auto_format')

text = SubElement(answer,'text')
text.text = reponse1

feedback = SubElement(answer,'feedback')
feedback.set('format','html')

text = SubElement(feedback,'text')
text.text = feedback1


if reponse2 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage2)
    answer.set('format','moodle_auto_format')

    text = SubElement(answer,'text')
    text.text = reponse2

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback2


if reponse3 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage3)
    answer.set('format','moodle_auto_format')

    text = SubElement(answer,'text')
    text.text = reponse3

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback3


#on cree un fichier txt qui contient toute les lignes du fichier xml que l'on va creer
fichier = open(file_name_txt, "w")
fichier.write(prettify(top))
fichier.close()

#on rajoute ' encoding="UTF-8" ' dans la premiere ligne 
fichier = open(file_name_txt, "r")
lignes= fichier.readlines()
fichier = open(file_name_txt, "w")
lignes[0] = '<?xml version="1.0" encoding="UTF-8"?>\n'
fichier.writelines(lignes)
fichier.close()

#on remplace les &lt; et les &gt; par < et > dans le fichier
f=open(file_name_txt,'r')
chaine=f.read().replace('&lt;','<')
chaine = chaine.replace ('&gt;','>')
f.close() 
f=open(file_name_txt,'w') 
f.write(chaine) 
f.close()

#on transforme le fichier txt en fichier xml
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    base_file, ext = os.path.splitext(filename)
    if ext == ".txt":
        if os.path.exists(file_name_xml):
            os.remove(file_name_xml)
        os.rename(filename, file_name + ".XML")