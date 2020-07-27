from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Window_calculeesimple(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculée simple")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        
 
 
        #self.show()

    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : calculée simple")
        VBoxLayout = QVBoxLayout()
        #VBoxLayout.setSpacing(50)

        scrollbar = QScrollArea()
        scrollbar.setLayout(VBoxLayout)

        hbox_adresse = QHBoxLayout()
        VBoxLayout.addLayout(hbox_adresse)

        self.label_adresse = QLabel("adresse du fichier",self)
        self.label_adresse.setFixedWidth(150)
        hbox_adresse.addWidget(self.label_adresse)

        self.lineedit_adresse = QLineEdit(self)
        self.lineedit_adresse.setText("Desktop\projet juillet 2020")
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
        self.combobox_selection_unite.addItem("la zone de saisie")
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

        self.groupBox.setLayout(VBoxLayout)

    def creer_question(self):
        print("creation des lignes du xml")


"""myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)"""