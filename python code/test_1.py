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
file_name = 'simulation vrai faux'
file_name_txt = file_name + ".txt"
file_name_xml = file_name + ".XML"



nom_question = 'simulation vrai faux'
intitule_question = 'vrai ou faux ??'

note_par_defaut = '3'

feedback_general = 'le feedback general'
feedback_vrai = 'feedback pour vrai'
feedback_faux = 'feedback pour faux'

penalite = '1'

bonne_reponse = 'faux'

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

comment = Comment('question: vrai faux')
top.append(comment)

question = SubElement(top, 'question')
question.set('type','truefalse')

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

answer = SubElement(question,'answer')
if bonne_reponse == 'vrai':
    answer.set('fraction','100')
else:
    answer.set('fraction','0')
answer.set('format','moodle_auto_format')

text = SubElement(answer,'text')
text.text = 'true'

feedback = SubElement(answer,'feedback')
feedback.set('format','html')

text = SubElement(feedback,'text')
text.text = feedback_vrai

answer = SubElement(question,'answer')
if bonne_reponse == 'vrai':
    answer.set('fraction','0')
else:
    answer.set('fraction','100')
answer.set('format','moodle_auto_format')

text = SubElement(answer,'text')
text.text = 'false'

feedback = SubElement(answer,'feedback')
feedback.set('format','html')

text = SubElement(feedback,'text')
text.text = feedback_faux


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
        
