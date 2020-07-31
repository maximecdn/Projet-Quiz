''' Fenêtre qui sert à créer/modifier les question de type 'vrai faux' '''

from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QBoxLayout, QPushButton, QGroupBox, QGridLayout, QTextEdit, QLineEdit, QComboBox, QMessageBox, QLabel, QSpacerItem
from PySide2.QtGui import QIcon, QFont
import os, sys
import os.path

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment


class Window_vraifaux(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vrai-Faux")
        self.setGeometry(900,900,900,900)

        self.createVBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
 
        #self.show()

    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : vrai faux")
        VBoxLayout = QVBoxLayout()

        hbox_adresse = QHBoxLayout()
        VBoxLayout.addLayout(hbox_adresse)

        self.label_adresse = QLabel("adresse du fichier",self)
        self.label_adresse.setFixedWidth(150)
        hbox_adresse.addWidget(self.label_adresse)

        self.lineedit_adresse = QLineEdit(self)
        self.lineedit_adresse.setText(os.getcwd())
        hbox_adresse.addWidget(self.lineedit_adresse)
        hbox_adresse.insertSpacing(2,400)

        hbox_nom_fichier = QHBoxLayout()
        VBoxLayout.addLayout(hbox_nom_fichier)

        self.label_nom_fichier = QLabel("Nom fichier :",self)
        self.label_nom_fichier.setFixedWidth(150)
        
        hbox_nom_fichier.addWidget(self.label_nom_fichier)

        self.lineedit_nom_fichier = QLineEdit(self)
        hbox_nom_fichier.addWidget(self.lineedit_nom_fichier)
        hbox_nom_fichier.insertSpacing(2,400)

        hbox_nom_question = QHBoxLayout()
        VBoxLayout.addLayout(hbox_nom_question)

        self.label_nom_question = QLabel("Nom question :",self)
        self.label_nom_question.setFixedWidth(150)
        hbox_nom_question.addWidget(self.label_nom_question)

        self.lineedit_nom_question = QLineEdit(self)
        #self.lineedit_nom_question.setFixedWidth(500)
        hbox_nom_question.addWidget(self.lineedit_nom_question)
        hbox_nom_question.insertSpacing(2,400)
        
        hbox_intitule_question = QHBoxLayout()
        VBoxLayout.addLayout(hbox_intitule_question)

        self.label_intitule_question = QLabel("Intitulé de la question :", self)
        self.label_intitule_question.setFixedWidth(150)
        self.label_intitule_question.setWordWrap(True)
        hbox_intitule_question.addWidget(self.label_intitule_question)

        self.textedit_intitule_question = QTextEdit(self)
        self.textedit_intitule_question.setFixedHeight(150)
        hbox_intitule_question.addWidget(self.textedit_intitule_question)
        hbox_intitule_question.insertSpacing(2,100)

        hbox_bonne_reponse = QHBoxLayout()
        VBoxLayout.addLayout(hbox_bonne_reponse)
 
        self.label_vraifaux = QLabel("Bonne réponse :", self)
        self.label_vraifaux.setFixedWidth(150)
        hbox_bonne_reponse.addWidget(self.label_vraifaux)

        self.combobox_vraifaux = QComboBox()
        self.combobox_vraifaux.addItem("Vrai")
        self.combobox_vraifaux.addItem("Faux")
        hbox_bonne_reponse.addWidget(self.combobox_vraifaux)
        hbox_bonne_reponse.insertSpacing(2,1000)

        hbox_note_defaut = QHBoxLayout()
        VBoxLayout.addLayout(hbox_note_defaut)
        
        self.label_note_par_defaut = QLabel("Note par défaut :", self)
        self.label_note_par_defaut.setFixedWidth(150)
        hbox_note_defaut.addWidget(self.label_note_par_defaut)
        

        self.lineedit_note_par_defaut = QLineEdit(self)
        hbox_note_defaut.addWidget(self.lineedit_note_par_defaut)
        hbox_note_defaut.insertSpacing(2,700)
        
        hbox_penalite = QHBoxLayout()
        VBoxLayout.addLayout(hbox_penalite)

        self.label_penalite = QLabel("pénalité :", self)
        self.label_penalite.setFixedWidth(150)
        hbox_penalite.addWidget(self.label_penalite)

        self.combobox_penalite = QComboBox()
        self.combobox_penalite.addItem("100")
        self.combobox_penalite.addItem("75")
        self.combobox_penalite.addItem("66.66")
        self.combobox_penalite.addItem("50")
        self.combobox_penalite.addItem("25")
        self.combobox_penalite.addItem("33.333")
        self.combobox_penalite.addItem("0")
        hbox_penalite.addWidget(self.combobox_penalite)
        hbox_penalite.insertSpacing(2,1000)

        hbox_feedbackgeneral = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedbackgeneral)

        
        self.label_feedbackgeneral = QLabel("Feedback general :", self)
        self.label_feedbackgeneral.setFixedWidth(150)
        hbox_feedbackgeneral.addWidget(self.label_feedbackgeneral)

        self.lineedit_feedback_general = QLineEdit(self)
        hbox_feedbackgeneral.addWidget(self.lineedit_feedback_general)
        hbox_feedbackgeneral.insertSpacing(2,100)

        
        hbox_feedback_vrai = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_vrai)
        
        self.label_feedbackvrai = QLabel("Feedback pour la réponse 'vrai' :", self)
        self.label_feedbackvrai.setFixedWidth(150)
        self.label_feedbackvrai.setWordWrap(True)
        hbox_feedback_vrai.addWidget(self.label_feedbackvrai)

        self.lineedit_feedback_vrai = QLineEdit(self)
        hbox_feedback_vrai.addWidget(self.lineedit_feedback_vrai)


        hbox_feedback_faux = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_faux)

        self.label_feedbackfaux = QLabel("Feedback pour la réponse 'faux' :", self)
        self.label_feedbackfaux.setFixedWidth(150)
        self.label_feedbackfaux.setWordWrap(True)
        hbox_feedback_faux.addWidget(self.label_feedbackfaux)

        self.lineedit_feedback_faux = QLineEdit(self)
        hbox_feedback_faux.addWidget(self.lineedit_feedback_faux)

        hbox_bouton_question = QHBoxLayout()
        VBoxLayout.addLayout(hbox_bouton_question)

        self.button = QPushButton("créer la question")
        self.button.clicked.connect(self.creer_question) 
        hbox_bouton_question.addWidget(self.button)
        hbox_bouton_question.insertSpacing(2,400)
        hbox_bouton_question.insertSpacing(0,400)
        
        self.groupBox.setLayout(VBoxLayout)

    

    

    def creer_question(self):
        #Fonction qui va créer un fichier xml en qui correspond à une question 'vrai faux' en prenant en compte toutes les infos dans les champs remplis de la fenêtre
        
        #non du fichier xml que l'on veut creer
        file_name = self.lineedit_nom_fichier.text()
        file_name_txt = file_name + ".txt"
        file_name_xml = file_name + ".XML"
        adresse = self.lineedit_adresse.text() + '/'



        nom_question = self.lineedit_nom_question.text()
        intitule_question = self.textedit_intitule_question.toPlainText()

        note_par_defaut = self.lineedit_note_par_defaut.text()

        feedback_general = self.lineedit_feedback_general.text()
        feedback_vrai = self.lineedit_feedback_vrai.text()
        feedback_faux = self.lineedit_feedback_faux.text()

        penalite = self.combobox_penalite.currentText()

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

        


#fonction qui permet de mettre en forme le fichier xml avec les indexations
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
