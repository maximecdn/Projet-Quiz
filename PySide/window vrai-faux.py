from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout, QTextEdit, QLineEdit, QComboBox, QMessageBox
from PySide2.QtGui import QIcon, QFont
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vrai-Faux")
        #self.setGeometry(300,300,300,300)

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
 
        self.show()

    def createGridLayout(self):
        self.groupBox = QGroupBox("type de question : vrai faux")
        gridLayout = QGridLayout()

        self.lineedit_nom_fichier = QLineEdit(self)
        self.lineedit_nom_fichier.setPlaceholderText("nom du fichier")
        gridLayout.addWidget(self.lineedit_nom_fichier,0 ,0)

        self.lineedit_nom_question = QLineEdit(self)
        self.lineedit_nom_question.setFont(QFont('Sanserif', 10))
        self.lineedit_nom_question.setPlaceholderText("nom question")
        gridLayout.addWidget(self.lineedit_nom_question,1 ,0)

        self.lineedit_intitule_question = QLineEdit(self)
        self.lineedit_intitule_question.setFont(QFont('Sanserif', 10))
        self.lineedit_intitule_question.setPlaceholderText("intitule question")
        gridLayout.addWidget(self.lineedit_intitule_question,2 ,0)

        self.lineedit_feedback_general = QLineEdit(self)
        self.lineedit_feedback_general.setPlaceholderText("feedback general")
        gridLayout.addWidget(self.lineedit_feedback_general,3 ,0)
 
        self.combobox_vraifaux = QComboBox()
        self.combobox_vraifaux.addItem("vrai")
        self.combobox_vraifaux.addItem("faux")
        gridLayout.addWidget(self.combobox_vraifaux,4 ,0)

        self.lineedit_note_par_defaut = QLineEdit(self)
        self.lineedit_note_par_defaut.setPlaceholderText("note par defaut")
        gridLayout.addWidget(self.lineedit_note_par_defaut,5 ,0)

        self.lineedit_penalite = QLineEdit(self)
        self.lineedit_penalite.setPlaceholderText("pénalité")
        gridLayout.addWidget(self.lineedit_penalite,6 ,0)

        self.lineedit_feedback_vrai = QLineEdit(self)
        self.lineedit_feedback_vrai.setPlaceholderText("feedback vrai")
        gridLayout.addWidget(self.lineedit_feedback_vrai,7 ,0)

        self.lineedit_feedback_faux = QLineEdit(self)
        self.lineedit_feedback_faux.setPlaceholderText("feedback faux")
        gridLayout.addWidget(self.lineedit_feedback_faux,8 ,0)

        self.bouton = QPushButton("créer la question")
        self.bouton.clicked.connect(self.creer_question)
        gridLayout.addWidget(self.bouton,9 ,0)
        
        self.groupBox.setLayout(gridLayout)

    

    

    def creer_question(self):
        print("creation des lignes du xml")
        #non du fichier xml que l'on veut creer
        file_name = self.lineedit_nom_fichier.text()
        file_name_txt = file_name + ".txt"
        file_name_xml = file_name + ".XML"
        adresse = "Desktop/projet quiz/" 



        nom_question = self.lineedit_nom_question.text()
        intitule_question = self.lineedit_intitule_question.text()

        note_par_defaut = self.lineedit_note_par_defaut.text()

        feedback_general = self.lineedit_feedback_general.text()
        feedback_vrai = self.lineedit_feedback_vrai.text()
        feedback_faux = self.lineedit_feedback_faux.text()

        penalite = self.lineedit_penalite.text()

        bonne_reponse = self.combobox_vraifaux.currentText()

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
        fichier = open(adresse + file_name_txt, "w")
        print("creation du txt")
        fichier.write(prettify(top))
        fichier.close()

        #on rajoute ' encoding="UTF-8" ' dans la premiere ligne 
        fichier = open(adresse + file_name_txt, "r")
        lignes= fichier.readlines()
        fichier = open(adresse + file_name_txt, "w")
        lignes[0] = '<?xml version="1.0" encoding="UTF-8"?>\n'
        fichier.writelines(lignes)
        print("modification du txt 1")
        fichier.close()

        #on remplace les &lt; et les &gt; par < et > dans le fichier
        f=open(adresse + file_name_txt,'r')
        chaine=f.read().replace('&lt;','<')
        chaine = chaine.replace ('&gt;','>')
        f.close() 
        f=open(adresse + file_name_txt,'w') 
        f.write(chaine) 
        print("modification du txt 2")
        f.close()
        
        #on transforme le fichier txt en fichier xml
        if os.path.exists(adresse + file_name_xml):
            os.remove(adresse + file_name_xml)
            print("le xml existe deja on le remplace par le nouveau")
        os.rename(adresse + file_name_txt, adresse + file_name_xml)

        


#fonction qui permet de mettre en forme le fichier xml avec les indexations
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)