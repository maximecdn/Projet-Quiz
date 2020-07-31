''' Fenêtre qui sert à créer/modifier les question de type 'numériques' '''

from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Window_numerique(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Numérique")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)


    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : Numérique")
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

        scrollbar = QScrollArea()
        scrollbar.setLayout(VBoxLayout)


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

        self.label_erreur_reponse1 = QLabel("erreur :",self)
        hbox_reponse1.addWidget(self.label_erreur_reponse1)

        self.lineedit_erreur_reponse1 = QLineEdit(self)
        hbox_reponse1.addWidget(self.lineedit_erreur_reponse1)
        hbox_reponse1.insertSpacing(6,70)
        hbox_reponse1.insertSpacing(4,70)
        hbox_reponse1.insertSpacing(2,70)

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
        

        self.label_erreur_reponse2 = QLabel("erreur :",self)
        hbox_reponse2.addWidget(self.label_erreur_reponse2)

        self.lineedit_erreur_reponse2 = QLineEdit(self)
        hbox_reponse2.addWidget(self.lineedit_erreur_reponse2)
        hbox_reponse2.insertSpacing(6,70)
        hbox_reponse2.insertSpacing(4,70)
        hbox_reponse2.insertSpacing(2,70)

        hbox_feedback_reponse2 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_feedback_reponse2)

        self.label_feedback_reponse2 = QLabel("Feedback pour la réponse 2 :", self)
        self.label_feedback_reponse2.setWordWrap(True)
        self.label_feedback_reponse2.setFixedWidth(150)
        hbox_feedback_reponse2.addWidget(self.label_feedback_reponse2)

        self.lineedit_feedback_reponse2 = QLineEdit(self)
        hbox_feedback_reponse2.addWidget(self.lineedit_feedback_reponse2)
        hbox_feedback_reponse2.insertSpacing(4,100) 

        self.label_espace_unite = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_unite)

        hbox_traitementunite = QHBoxLayout()
        VBoxLayout.addLayout(hbox_traitementunite)

        self.labeltraitementunite = QLabel("traitement de l'unité",self)
        self.labeltraitementunite.setFixedWidth(150)
        hbox_traitementunite.addWidget(self.labeltraitementunite)

        self.combobox_traitementunite = QComboBox(self)
        self.combobox_traitementunite.addItem("les unités ne sont pas utilisées. Seule la valeur numérique est évaluée")
        self.combobox_traitementunite.addItem("les unités sont optionnelles. Si une unité est saisie elle est utilisée pour la conversion vers l'unité 1 ")
        self.combobox_traitementunite.addItem("l'unite doit être indiquée et sera prise en compte dans la note")
        hbox_traitementunite.addWidget(self.combobox_traitementunite)
        hbox_traitementunite.insertSpacing(2,400)

        hbox_penalite_unite = QHBoxLayout()
        VBoxLayout.addLayout(hbox_penalite_unite)

        self.label_penalite_unite = QLabel("pénalité unité \n(fraction entre 0 et 1)",self)
        self.label_penalite_unite.setFixedWidth(150)
        hbox_penalite_unite.addWidget(self.label_penalite_unite)

        self.lineedit_penalite_unite = QLineEdit(self)
        self.lineedit_penalite_unite.setEnabled(False)
        hbox_penalite_unite.addWidget(self.lineedit_penalite_unite)
        hbox_penalite_unite.insertSpacing(2,700)

        hbox_selection_unites = QHBoxLayout()
        VBoxLayout.addLayout(hbox_selection_unites)

        self.label_selection_unite = QLabel("les unités sont saisie en utilisant",self)
        self.label_selection_unite.setFixedWidth(150)
        self.label_selection_unite.setWordWrap(True)
        hbox_selection_unites.addWidget(self.label_selection_unite)

        self.combobox_selection_unite = QComboBox()
        self.combobox_selection_unite.addItem("la zone de saisie")
        self.combobox_selection_unite.addItem("une sélection de choix multiple")
        self.combobox_selection_unite.addItem("un menu déroulant")
        self.combobox_selection_unite.setEnabled(False)
        hbox_selection_unites.addWidget(self.combobox_selection_unite)
        hbox_selection_unites.insertSpacing(2,700)

        hbox_position_unite = QHBoxLayout()
        VBoxLayout.addLayout(hbox_position_unite)

        self.label_position_unite = QLabel("position de l'unité",self)
        self.label_position_unite.setFixedWidth(150)
        hbox_position_unite.addWidget(self.label_position_unite)

        self.combobox_position_unite = QComboBox()
        self.combobox_position_unite.addItem("à droite, comme 12.5 cm ou 10.5 Km")
        self.combobox_position_unite.addItem("à gauche, comme $ 1.5 ou £ 2.5")
        self.combobox_position_unite.setEnabled(False)
        hbox_position_unite.addWidget(self.combobox_position_unite)
        hbox_position_unite.insertSpacing(2,700)

        hbox_unite1 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_unite1)

        self.label_unite1 = QLabel("unité 1", self)
        self.label_unite1.setFixedWidth(150)
        hbox_unite1.addWidget(self.label_unite1)

        self.lineedit_unite1 = QLineEdit(self)
        self.lineedit_unite1.setEnabled(False)
        hbox_unite1.addWidget(self.lineedit_unite1)

        self.label_coef1 = QLabel("Coefficient")
        self.label_coef1.setFixedWidth(90)
        hbox_unite1.addWidget(self.label_coef1)

        self.lineedit_coef1 = QLineEdit(self)
        self.lineedit_coef1.setEnabled(False)
        hbox_unite1.addWidget(self.lineedit_coef1)
        hbox_unite1.insertSpacing(2,200)
        hbox_unite1.insertSpacing(5,200)

        hbox_unite2 = QHBoxLayout()
        VBoxLayout.addLayout(hbox_unite2)

        self.label_unite2 = QLabel("unité 2", self)
        self.label_unite2.setFixedWidth(150)
        hbox_unite2.addWidget(self.label_unite2)

        self.lineedit_unite2 = QLineEdit(self)
        self.lineedit_unite2.setEnabled(False)
        hbox_unite2.addWidget(self.lineedit_unite2)

        self.label_coef2 = QLabel("Coefficient")
        self.label_coef2.setFixedWidth(90)
        hbox_unite2.addWidget(self.label_coef2)

        self.lineedit_coef2 = QLineEdit(self)
        self.lineedit_coef2.setEnabled(False)
        hbox_unite2.addWidget(self.lineedit_coef2)
        hbox_unite2.insertSpacing(2,200)
        hbox_unite2.insertSpacing(5,200)

        self.label_espace_bouton = QLabel("",self)
        VBoxLayout.addWidget(self.label_espace_bouton)

        hbox_bouton_question = QHBoxLayout()
        VBoxLayout.addLayout(hbox_bouton_question)

        self.button = QPushButton("créer la question")
        self.button.clicked.connect(self.creer_question) 
        hbox_bouton_question.addWidget(self.button)
        hbox_bouton_question.insertSpacing(2,400)
        hbox_bouton_question.insertSpacing(0,400)
        

        self.combobox_traitementunite.currentIndexChanged.connect(self.traitement_unite)
        

        self.groupBox.setLayout(VBoxLayout)
    

    def traitement_unite(self,index):
        #Fonction qui permet de rendre actif/inactif certains champs en fonction du traitement de l'unité (comme sur Celene)

        if self.combobox_traitementunite.currentIndex() == 0:
            self.lineedit_penalite_unite.setEnabled(False)
            self.lineedit_penalite_unite.setText("")
            self.combobox_selection_unite.setEnabled(False)
            self.combobox_position_unite.setEnabled(False)
            self.lineedit_unite1.setEnabled(False)
            self.lineedit_unite1.setText("")
            self.lineedit_coef1.setEnabled(False)
            self.lineedit_coef1.setText("")
            self.lineedit_unite2.setEnabled(False)
            self.lineedit_unite2.setText("")
            self.lineedit_coef2.setEnabled(False)
            self.lineedit_coef2.setText("")
       
        if self.combobox_traitementunite.currentIndex() == 1:
            self.lineedit_penalite_unite.setEnabled(False)
            self.lineedit_penalite_unite.setText("")
            self.combobox_selection_unite.setEnabled(False)
            self.combobox_position_unite.setEnabled(True)
            self.lineedit_unite1.setEnabled(True)
            self.lineedit_coef1.setEnabled(True)
            self.lineedit_unite2.setEnabled(True)
            self.lineedit_coef2.setEnabled(True)

        if self.combobox_traitementunite.currentIndex() == 2:
            self.lineedit_penalite_unite.setEnabled(True)
            self.combobox_selection_unite.setEnabled(True)
            self.combobox_position_unite.setEnabled(True)
            self.lineedit_unite1.setEnabled(True)
            self.lineedit_coef1.setEnabled(True)
            self.lineedit_unite2.setEnabled(True)
            self.lineedit_coef2.setEnabled(True)

    def creer_question(self):
        #Fonction qui va créer un fichier xml en qui correspond à une question 'numérique' en prenant en compte toutes les infos dans les champs remplis de la fenêtre

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
        tolerance1 = self.lineedit_erreur_reponse1.text()
        pourcentage1 = self.combobox_reponse1.currentText()
        feedback_reponse1 = self.lineedit_feedback_reponse1.text()

        reponse2 = self.LineEditReponse2.text()
        tolerance2 = self.lineedit_erreur_reponse2.text()
        pourcentage2 = self.combobox_reponse2.currentText()
        feedback_reponse2 = self.lineedit_feedback_reponse2.text()

        traitement_unite = 'sans'     # mettre 'avec', 'optionnel' ou 'sans' 
        if self.combobox_traitementunite.currentIndex() == 1 :
            traitement_unite = 'optionnel'
        
        if self.combobox_traitementunite.currentIndex() == 2 :
            traitement_unite = 'avec'


        penalite_unite = self.lineedit_penalite_unite.text()

        saisie_unite = 'texte'        # mettre 'texte', 'menu', ou 'selection' 
        if self.combobox_selection_unite.currentIndex() == 1:
            saisie_unite = 'selection'

        if self.combobox_selection_unite.currentIndex() == 2:
            saisie_unite = 'menu'
            

        position_unite = 'R'          # mettre 'R' ou 'L' 
        if self.combobox_position_unite.currentIndex() == 1 :
            position_unite = 'L'

        unite1 = self.lineedit_unite1.text()
        coef1 = self.lineedit_coef1.text()

        unite2 = self.lineedit_unite2.text()
        coef2 = self.lineedit_coef2.text()


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


        if reponse1 != '' : 
            answer = SubElement(question,'answer')
            answer.set('fraction',pourcentage1)

            text = SubElement(answer,'text')
            text.text = reponse1

            feedback = SubElement(answer,'feedback')
            feedback.set('format','html')

            text = SubElement(feedback,'text')
            text.text = feedback_reponse1

            tolerance = SubElement(answer,'tolerance')
            tolerance.text = tolerance1

        if reponse2 != '' : 
            answer = SubElement(question,'answer')
            answer.set('fraction',pourcentage2)

            text = SubElement(answer,'text')
            text.text = reponse2

            feedback = SubElement(answer,'feedback')
            feedback.set('format','html')

            text = SubElement(feedback,'text')
            text.text = feedback_reponse2

            tolerance = SubElement(answer,'tolerance')
            tolerance.text = tolerance2

        units=SubElement(question,'units')



        if unite1 != '':
            unit = SubElement(units,'unit')

            multiplier = SubElement(unit,'multiplier')
            multiplier.text = coef1

            unit_name = SubElement(unit,'unit_name')
            unit_name.text = unite1

        if unite2 != '':
            unit = SubElement(units,'unit')

            multiplier = SubElement(unit,'multiplier')
            multiplier.text = coef2

            unit_name = SubElement(unit,'unit_name')
            unit_name.text = unite2


        if traitement_unite == 'sans' :
            unitgradingtype = SubElement(question,'unitgradingtype')
            unitgradingtype.text = '0'

            unitpenalty = SubElement(question,'unitpenalty')
            unitpenalty.text = '0.1'

        if traitement_unite == 'optionnel' :
            unitgradingtype = SubElement(question,'unitgradingtype')
            unitgradingtype.text = '0'

            unitpenalty = SubElement(question,'unitpenalty')
            unitpenalty.text = '0.1'

        if traitement_unite == 'avec' :
            unitgradingtype = SubElement(question,'unitgradingtype')
            unitgradingtype.text = '2'

            unitpenalty = SubElement(question,'unitpenalty')
            unitpenalty.text = penalite_unite

        if saisie_unite == 'texte' :
            showunits = SubElement(question,'showunits')
            showunits.text = '0'

        if saisie_unite == 'selection' :
            showunits = SubElement(question,'showunits')
            showunits.text = '1'

        if saisie_unite == 'menu' :
            showunits = SubElement(question,'showunits')
            showunits.text = '2'

        if traitement_unite == 'sans':
            showunits = SubElement(question,'showunits')
            showunits.text = '3'

        if position_unite == 'L':
            unitsleft = SubElement(question,'unitsleft')
            unitsleft.text = '1'
        else :
            unitsleft = SubElement(question,'unitsleft')
            unitsleft.text = '0'

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
