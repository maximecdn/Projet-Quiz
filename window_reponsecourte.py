''' Fenêtre qui sert à créer/modifier les question de type 'réponse courte' '''

from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Window_reponsecourte(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Réponse courte")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)


    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : réponse courte")
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

        hbox_note_defaut = QHBoxLayout()
        VBoxLayout.addLayout(hbox_note_defaut)
        

        self.label_note_par_defaut = QLabel("Note par défaut :", self)
        self.label_note_par_defaut.setFixedWidth(150)
        hbox_note_defaut.addWidget(self.label_note_par_defaut)
        

        self.lineedit_note_par_defaut = QLineEdit(self)
        hbox_note_defaut.addWidget(self.lineedit_note_par_defaut)
        hbox_note_defaut.insertSpacing(2,600)

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

        hbox_maj = QHBoxLayout()
        VBoxLayout.addLayout(hbox_maj)

        self.label_maj = QLabel("sensible à la case :",self)
        self.label_maj.setFixedWidth(150)
        hbox_maj.addWidget(self.label_maj)

        self.combobox_maj = QComboBox()
        self.combobox_maj.addItem("non, la case n'est pas importante")
        self.combobox_maj.addItem("oui la case doit correspondre")
        hbox_maj.addWidget(self.combobox_maj)
        hbox_maj.insertSpacing(2,450)

        self.label_espace_reponse1 = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_reponse1)

        hbox_reponse1 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_reponse1)

        self.label_reponse1 = QLabel("Réponse 1 :", self)
        self.label_reponse1.setFixedWidth(150)
        hbox_reponse1.addWidget(self.label_reponse1)

        self.LineEditReponse1 = QLineEdit(self)
        hbox_reponse1.addWidget(self.LineEditReponse1)

        self.label_note1 = QLabel("note (%) :",self)
        hbox_reponse1.addWidget(self.label_note1)

        self.combobox_reponse1 = QComboBox()
        self.combobox_reponse1.addItem("100")
        self.combobox_reponse1.addItem("75")
        self.combobox_reponse1.addItem("66.66")
        self.combobox_reponse1.addItem("50")
        self.combobox_reponse1.addItem("25")
        self.combobox_reponse1.addItem("33.333")
        self.combobox_reponse1.addItem("0")
        hbox_reponse1.addWidget(self.combobox_reponse1)
        hbox_reponse1.insertSpacing(4,70)

        hbox_feedback_reponse1 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_reponse1)

        self.label_feedback_reponse1 = QLabel("Feedback pour la réponse 1 :", self)
        self.label_feedback_reponse1.setWordWrap(True)
        self.label_feedback_reponse1.setFixedWidth(150)
        hbox_feedback_reponse1.addWidget(self.label_feedback_reponse1)

        self.lineedit_feedback_reponse1 = QLineEdit(self)
        hbox_feedback_reponse1.addWidget(self.lineedit_feedback_reponse1)
        hbox_feedback_reponse1.insertSpacing(2,100)

        self.label_espace_reponse2 = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_reponse2)

        hbox_reponse2 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_reponse2)

        self.label_reponse2 = QLabel("Réponse 2 :", self)
        self.label_reponse2.setFixedWidth(150)
        hbox_reponse2.addWidget(self.label_reponse2)

        self.LineEditReponse2 = QLineEdit(self)
        hbox_reponse2.addWidget(self.LineEditReponse2)

        self.label_note2 = QLabel("note (%) :",self)
        hbox_reponse2.addWidget(self.label_note2)

        self.combobox_reponse2 = QComboBox()
        self.combobox_reponse2.addItem("100")
        self.combobox_reponse2.addItem("75")
        self.combobox_reponse2.addItem("66.66")
        self.combobox_reponse2.addItem("50")
        self.combobox_reponse2.addItem("25")
        self.combobox_reponse2.addItem("33.333")
        self.combobox_reponse2.addItem("0")
        hbox_reponse2.addWidget(self.combobox_reponse2)
        hbox_reponse2.insertSpacing(4,70)

        hbox_feedback_reponse2 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_reponse2)

        self.label_feedback_reponse2 = QLabel("Feedback pour la réponse 2 :", self)
        self.label_feedback_reponse2.setWordWrap(True)
        self.label_feedback_reponse2.setFixedWidth(150)
        hbox_feedback_reponse2.addWidget(self.label_feedback_reponse2)

        self.lineedit_feedback_reponse2 = QLineEdit(self)
        hbox_feedback_reponse2.addWidget(self.lineedit_feedback_reponse2)
        hbox_feedback_reponse2.insertSpacing(4,100) 

        self.label_espace_bouton = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_bouton)

        hbox_bouton_question = QHBoxLayout()
        VBoxLayout.addLayout(hbox_bouton_question)

        self.button = QPushButton("créer la question")
        self.button.clicked.connect(self.creer_question) 
        hbox_bouton_question.addWidget(self.button)
        hbox_bouton_question.insertSpacing(2,400)
        hbox_bouton_question.insertSpacing(0,400)

        self.groupBox.setLayout(VBoxLayout)
    

    

    def creer_question(self):
        #Fonction qui va créer un fichier xml en qui correspond à une question 'réponse courte' en prenant en compte toutes les infos dans les champs remplis de la fenêtre

        #non du fichier xml que l'on veut creer
        file_name = self.lineedit_nom_fichier.text()
        file_name_txt = file_name + ".txt"
        file_name_xml = file_name + ".XML"
        adresse = self.lineedit_adresse.text() + '/'



        nom_question = self.lineedit_nom_question.text()
        intitule_question = self.textedit_intitule_question.toPlainText()

        note_par_defaut = self.lineedit_note_par_defaut.text()

        feedback_general = self.lineedit_feedback_general.text()

        penalite = str(float(self.combobox_penalite.currentText()) / 100)

        reponse1 = self.LineEditReponse1.text()
        feedback1 = self.lineedit_feedback_reponse1.text()
        pourcentage1 = self.combobox_reponse1.currentText()

        reponse2 = self.LineEditReponse2.text()
        feedback2 = self.lineedit_feedback_reponse2.text()
        pourcentage2 = self.combobox_reponse2.currentText()

        reponse3 = ''
        feedback3 = ''
        pourcentage3 = ''

        majuscule = ''
        if self.combobox_maj.currentIndex() == 1 :
            majuscule = 'oui' # mettre 'oui' si on veut prendre en compte les majuscules dans la réponse 


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




def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
