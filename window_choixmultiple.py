''' Fenêtre qui sert à créer/modifier les question de type 'choix multiple' '''

from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Window_choixmultiple(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Choix Multiple")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        
 
 
        #self.show()

    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : Choix multiple")
        VBoxLayout = QVBoxLayout()
        scrollbar = QScrollArea()
        scrollbar.setLayout(VBoxLayout)

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

        hbox_nbreponse = QHBoxLayout()
        VBoxLayout.addLayout(hbox_nbreponse)

        self.label_nbreponse = QLabel("plusieurs réponses ou" +"\n" "une seule ?",self)
        self.label_nbreponse.setWordWrap(True)
        self.label_nbreponse.setFixedWidth(150)
        hbox_nbreponse.addWidget(self.label_nbreponse)

        self.combobox_nbreponse = QComboBox()
        self.combobox_nbreponse.addItem("une seule réponse")
        self.combobox_nbreponse.addItem("réponses multiples autorisées")
        hbox_nbreponse.addWidget(self.combobox_nbreponse)

        self.check_melange = QCheckBox("mélanger l'ordre des réponses", self)
        hbox_nbreponse.addWidget(self.check_melange)

        self.label_numerotation = QLabel("numérotation :")
        hbox_nbreponse.addWidget(self.label_numerotation)

        self.combobox_numerotation = QComboBox()
        self.combobox_numerotation.addItem("a, b, c ...")
        self.combobox_numerotation.addItem("1, 2, 3 ...")
        self.combobox_numerotation.addItem("sans numerotation")
        hbox_nbreponse.addWidget(self.combobox_numerotation)
        hbox_nbreponse.insertSpacing(5,250)
        hbox_nbreponse.insertSpacing(4,50)
        hbox_nbreponse.insertSpacing(3,100)
        hbox_nbreponse.insertSpacing(2,50)

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

        self.label_espace_reponse3 = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_reponse3)

        hbox_reponse3 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_reponse3)

        self.label_reponse3 = QLabel("Réponse 3 :", self)
        self.label_reponse3.setFixedWidth(150)
        hbox_reponse3.addWidget(self.label_reponse3)

        self.LineEditReponse3 = QLineEdit(self)
        hbox_reponse3.addWidget(self.LineEditReponse3)

        self.label_note3 = QLabel("note (%) :",self)
        hbox_reponse3.addWidget(self.label_note3)

        self.combobox_reponse3 = QComboBox()
        self.combobox_reponse3.addItem("100")
        self.combobox_reponse3.addItem("75")
        self.combobox_reponse3.addItem("66.66")
        self.combobox_reponse3.addItem("50")
        self.combobox_reponse3.addItem("25")
        self.combobox_reponse3.addItem("33.333")
        self.combobox_reponse3.addItem("0")
        hbox_reponse3.addWidget(self.combobox_reponse3)
        hbox_reponse3.insertSpacing(4,70)

        hbox_feedback_reponse3 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_reponse3)

        self.label_feedback_reponse3 = QLabel("Feedback pour la réponse 3 :", self)
        self.label_feedback_reponse3.setWordWrap(True)
        self.label_feedback_reponse3.setFixedWidth(150)
        hbox_feedback_reponse3.addWidget(self.label_feedback_reponse3)
        self.lineedit_feedback_reponse3 = QLineEdit(self)
        hbox_feedback_reponse3.addWidget(self.lineedit_feedback_reponse3)
        hbox_feedback_reponse3.insertSpacing(2,100) 

        self.label_espace_reponse4 = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_reponse4)

        hbox_reponse4 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_reponse4)

        self.label_reponse4 = QLabel("Réponse 4 :", self)
        self.label_reponse4.setFixedWidth(150)
        hbox_reponse4.addWidget(self.label_reponse4)

        self.LineEditReponse4 = QLineEdit(self)
        hbox_reponse4.addWidget(self.LineEditReponse4)

        self.label_note4 = QLabel("note (%) :",self)
        hbox_reponse4.addWidget(self.label_note4)

        self.combobox_reponse4 = QComboBox()
        self.combobox_reponse4.addItem("100")
        self.combobox_reponse4.addItem("75")
        self.combobox_reponse4.addItem("66.66")
        self.combobox_reponse4.addItem("50")
        self.combobox_reponse4.addItem("25")
        self.combobox_reponse4.addItem("33.333")
        self.combobox_reponse4.addItem("0")
        hbox_reponse4.addWidget(self.combobox_reponse4)
        hbox_reponse4.insertSpacing(4,70)

        hbox_feedback_reponse4 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_reponse4)

        self.label_feedback_reponse4 = QLabel("Feedback pour la réponse 4 :", self)
        self.label_feedback_reponse4.setWordWrap(True)
        self.label_feedback_reponse4.setFixedWidth(150)
        hbox_feedback_reponse4.addWidget(self.label_feedback_reponse4)

        self.lineedit_feedback_reponse4 = QLineEdit(self)
        hbox_feedback_reponse4.addWidget(self.lineedit_feedback_reponse4)
        hbox_feedback_reponse4.insertSpacing(2,100)

        self.label_espace_feedback = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_feedback)

        hbox_feedback_corecte = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_corecte)

        self.label_feedback_corecte = QLabel("Feedback réponse \ncorecte :", self)
        self.label_feedback_corecte.setWordWrap(True)
        self.label_feedback_corecte.setFixedWidth(150)
        hbox_feedback_corecte.addWidget(self.label_feedback_corecte)

        self.lineedit_feedback_corecte = QLineEdit(self)
        hbox_feedback_corecte.addWidget(self.lineedit_feedback_corecte)
        hbox_feedback_corecte.insertSpacing(2,100)

        hbox_feedback_partiellement_corecte = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_partiellement_corecte)

        self.label_feedback_partiellement_corecte = QLabel("Feedback réponse partiellement corecte :", self)
        self.label_feedback_partiellement_corecte.setWordWrap(True)
        self.label_feedback_partiellement_corecte.setFixedWidth(150)
        hbox_feedback_partiellement_corecte.addWidget(self.label_feedback_partiellement_corecte)

        self.lineedit_feedback_partiellement_corecte = QLineEdit(self)
        hbox_feedback_partiellement_corecte.addWidget(self.lineedit_feedback_partiellement_corecte)
        hbox_feedback_partiellement_corecte.insertSpacing(2,100)

        hbox_feedback_incorecte = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_incorecte)

        self.label_feedback_incorecte = QLabel("Feedback réponse \nincorecte :", self)
        self.label_feedback_incorecte.setWordWrap(True)
        self.label_feedback_incorecte.setFixedWidth(150)
        hbox_feedback_incorecte.addWidget(self.label_feedback_incorecte)

        self.lineedit_feedback_incorecte = QLineEdit(self)
        hbox_feedback_incorecte.addWidget(self.lineedit_feedback_incorecte)
        hbox_feedback_incorecte.insertSpacing(2,100)

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
        #Fonction qui va créer un fichier xml en qui correspond à une question 'choix multiple' en prenant en compte toutes les infos dans les champs remplis de la fenêtre

        #non du fichier xml que l'on veut creer
        file_name = self.lineedit_nom_fichier.text()
        file_name_txt = file_name + ".txt"
        file_name_xml = file_name + ".XML"
        adresse = self.lineedit_adresse.text() + '/'



        nom_question = self.lineedit_nom_question.text()
        intitule_question = self.textedit_intitule_question.toPlainText()

        note_par_defaut = self.lineedit_note_par_defaut.text()

        feedback_general = self.lineedit_feedback_general.text()
        feedback_corecte = self.lineedit_feedback_corecte.text()
        feedback_incorecte = self.lineedit_feedback_incorecte.text()
        feedback_partiellement_corecte = self.lineedit_feedback_partiellement_corecte.text()

        penalite = str(float(self.combobox_penalite.currentText()) / 100)

        une_seule_reponse = ''
        if self.combobox_nbreponse.currentIndex() == 0:
            une_seule_reponse = 'oui'
        
        reponse1 = self.LineEditReponse1.text()
        feedback1 = self.lineedit_feedback_reponse1.text()
        pourcentage1 = self.combobox_reponse1.currentText()

        reponse2 = self.LineEditReponse2.text()
        feedback2 = self.lineedit_feedback_reponse2.text()
        pourcentage2 = self.combobox_reponse2.currentText()

        reponse3 = self.LineEditReponse3.text()
        feedback3 = self.lineedit_feedback_reponse3.text()
        pourcentage3 = self.combobox_reponse3.currentText()

        reponse4 = self.LineEditReponse4.text()
        feedback4 = self.lineedit_feedback_reponse4.text()
        pourcentage4 = self.combobox_reponse4.currentText()

        reponse5 = ''
        feedback5 = ''
        pourcentage5 = '0'

        reponse6 = ''
        feedback6 = ''
        pourcentage6 = '0'

        melange_reponse = ''
        if self.check_melange.isChecked() == True :
            melange_reponse = 'oui' #mettre 'oui' si on veut mélanger l'ordre des reponses

        numerotation = 'none'
        if self.combobox_numerotation.currentIndex() == 0:
            numerotation = 'abc' 
        if self.combobox_numerotation.currentIndex() == 1:
            numerotation = '123'     

        montrer_nombre_correcte = 'oui'    # mettre 'oui' si on veut indiquer le nombre de bonne reponses correctes


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

        answernumbering = SubElement(question,'answernumbering')
        answernumbering.text = numerotation

        correctfeedback = SubElement(question,'correctfeedback')
        correctfeedback.set('format','html')

        text = SubElement(correctfeedback,'text')
        text.text = feedback_corecte

        partiallycorrectfeedback = SubElement(question,'partiallycorrectfeedback')
        partiallycorrectfeedback.set('format','html')

        text = SubElement(partiallycorrectfeedback,'text')
        text.text = feedback_partiellement_corecte

        incorrectfeedback = SubElement(question,'incorrectfeedback')
        incorrectfeedback.set('format','html')

        text = SubElement(incorrectfeedback,'text')
        text.text = feedback_incorecte

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
