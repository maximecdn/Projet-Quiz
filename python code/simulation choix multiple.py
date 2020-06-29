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
file_name = 'simulation choix multiple'
file_name_txt = file_name + ".txt"
file_name_xml = file_name + ".XML"



nom_question = 'simulation choix multiple'
intitule_question = 'quelle est la bonne réponse ??'

note_par_defaut = '3'

feedback_general = 'le feedbackgeneral'
feedback_correcte = 'le feedback coorecte'
feedback_incorrecte = 'le feedback incorrecte'
feedback_partiellement_correcte = 'le feedback partiellement correcte'

penalite = '1'

une_seule_reponse = 'non'
reponse1 = 'oui'
feedback1 = ''
pourcentage1 = '50'

reponse2 = 'non'
feedback2 = ''
pourcentage2 = '0'

reponse3 = 'un peu'
feedback3 = ''
pourcentage3 = '50'

reponse4 = 'je sais pas'
feedback4 = ''
pourcentage4 = '0'

reponse5 = ''
feedback5 = ''
pourcentage5 = '0'

reponse6 = ''
feedback6 = ''
pourcentage6 = '0'

melange_reponse = 'oui'
numerotation = '123'
montrer_nombre_correcte = 'oui'


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
question.set('type','multichoice')

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

single = SubElement(question,'single')
if une_seule_reponse == 'oui':
    single.text = 'true'
else:
    single.text = 'false'

shuffleanswers = SubElement(question, 'shuffleanswers')
if melange_reponse == 'oui' :
    shuffleanswers.text = 'true'
else:
    shuffleanswers.text = 'false'

answer = SubElement(question,'answer')
answer.set('fraction','100')

answernumbering = SubElement(question,'answernumbering')
answernumbering.text = numerotation

correctfeedback = SubElement(question,'correctfeedback')
correctfeedback.set('format','html')

text = SubElement(correctfeedback,'text')
text.text = feedback_correcte

partiallycorrectfeedback = SubElement(question,'partiallycorrectfeedback')
partiallycorrectfeedback.set('format','html')

text = SubElement(partiallycorrectfeedback,'text')
text.text = feedback_partiellement_correcte

incorrectfeedback = SubElement(question,'correctfeedback')
incorrectfeedback.set('format','html')

text = SubElement(incorrectfeedback,'text')
text.text = feedback_incorrecte

if montrer_nombre_correcte == 'oui':
    shownumcorrect = SubElement(question,'shownumcorrect')


if reponse1 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage1)

    text = SubElement(answer,'text')
    text.text = '<![CDATA[<p>' + reponse1 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback1

   

if reponse2 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage2)

    text = SubElement(answer,'text')
    text.text ='<![CDATA[<p>' + reponse2 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback2

if reponse3 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage3)

    text = SubElement(answer,'text')
    text.text ='<![CDATA[<p>' + reponse3 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback3

if reponse4 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage4)

    text = SubElement(answer,'text')
    text.text ='<![CDATA[<p>' + reponse4 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback4

if reponse5 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage5)

    text = SubElement(answer,'text')
    text.text ='<![CDATA[<p>' + reponse5 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback5

if reponse6 != '' : 
    answer = SubElement(question,'answer')
    answer.set('fraction',pourcentage6)

    text = SubElement(answer,'text')
    text.text = '<![CDATA[<p>' + reponse6 + '</p>]]>'

    feedback = SubElement(answer,'feedback')
    feedback.set('format','html')

    text = SubElement(feedback,'text')
    text.text = feedback6



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