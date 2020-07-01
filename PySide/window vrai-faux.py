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

        self.lineedit_nom_question = QLineEdit(self)
        self.lineedit_nom_question.setFont(QFont('Sanserif', 10))
        self.lineedit_nom_question.setPlaceholderText("nom question")
        
        
        gridLayout.addWidget(self.lineedit_nom_question, 0,0)

        self.lineedit_intitule_question = QLineEdit(self)
        self.lineedit_intitule_question.setFont(QFont('Sanserif', 10))
        self.lineedit_intitule_question.setPlaceholderText("intitule question")
        gridLayout.addWidget(self.lineedit_intitule_question, 1,0)
 
        self.combobox = QComboBox()
        self.combobox.addItem("vrai")
        self.combobox.addItem("faux")
        gridLayout.addWidget(self.combobox,2,0)

        self.bouton = QPushButton("créer la question")
        self.bouton.clicked.connect(self.creer_question)
        gridLayout.addWidget(self.bouton,3,0)
        
        self.groupBox.setLayout(gridLayout)

    

    

    def creer_question(self):
        print("creation des lignes du xml")
        #non du fichier xml que l'on veut creer
        file_name = " azerty"
        file_name_txt = file_name + ".txt"
        file_name_xml = file_name + ".XML"
        adresse = "Desktop/projet quiz/" 



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
        
        if os.path.exists(adresse + file_name_xml):
            os.remove(adresse + file_name_xml)
            print("le xml existe deja on le remplace par le nouveau")
        os.rename(adresse + file_name_txt, adresse + file_name_xml)

        '''#on transforme le fichier txt en fichier xml
        for filename in os.listdir(os.path.dirname(os.path.abspath(adresse + file_name_txt))):
            #print("le competeur vaut " + str(filename))
            #base_file, ext = os.path.splitext(filename)
            if filename == file_name_txt:
                #print("le competeur vaut " + str(filename))
                print("fichier txt deja present")
                if os.path.exists(file_name_xml):
                    print("le xml existe deja")
                    os.remove(file_name_xml)
                os.rename(filename, file_name + ".XML")
                print("transformation en xml")'''
            
        


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