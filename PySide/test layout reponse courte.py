from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vrai-Faux")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        
 
 
        self.show()

    def createVBoxLayout(self):
        self.groupBox = QGroupBox("Type de question : réponse courte")
        VBoxLayout = QVBoxLayout()
        #VBoxLayout.setSpacing(50)

        #scrollbar = QScrollArea()
        #scrollbar.setLayout(VBoxLayout)

        self.groupBox_generaux = QGroupBox("Généraux")
        VBoxlayout_generaux = QVBoxLayout()

        hbox_nom_fichier = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_nom_fichier)

        self.label_nom_fichier = QLabel("Nom fichier :",self)
        self.label_nom_fichier.setFixedWidth(150)
        
        hbox_nom_fichier.addWidget(self.label_nom_fichier)

        self.lineedit_nom_fichier = QLineEdit(self)
        hbox_nom_fichier.addWidget(self.lineedit_nom_fichier)
        hbox_nom_fichier.insertSpacing(2,400)

        hbox_nom_question = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_nom_question)

        self.label_nom_question = QLabel("Nom question :",self)
        self.label_nom_question.setFixedWidth(150)
        hbox_nom_question.addWidget(self.label_nom_question)

        self.lineedit_nom_question = QLineEdit(self)
        #self.lineedit_nom_question.setFixedWidth(500)
        hbox_nom_question.addWidget(self.lineedit_nom_question)
        hbox_nom_question.insertSpacing(2,400)

        
        
        hbox_intitule_question = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_intitule_question)

        self.label_intitule_question = QLabel("Intitulé de la question :", self)
        self.label_intitule_question.setFixedWidth(150)
        self.label_intitule_question.setWordWrap(True)
        hbox_intitule_question.addWidget(self.label_intitule_question)

        self.textedit_intitule_question = QTextEdit(self)
        self.textedit_intitule_question.setFixedHeight(150)
        hbox_intitule_question.addWidget(self.textedit_intitule_question)
        hbox_intitule_question.insertSpacing(2,100)


        hbox_note_defaut = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_note_defaut)
        

        self.label_note_par_defaut = QLabel("Note par défaut :", self)
        self.label_note_par_defaut.setFixedWidth(150)
        hbox_note_defaut.addWidget(self.label_note_par_defaut)
        

        self.lineedit_note_par_defaut = QLineEdit(self)
        hbox_note_defaut.addWidget(self.lineedit_note_par_defaut)
        hbox_note_defaut.insertSpacing(2,600)
        
        

        hbox_feedbackgeneral = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_feedbackgeneral)


        

        self.label_feedbackgeneral = QLabel("Feedback general :", self)
        self.label_feedbackgeneral.setFixedWidth(150)
        hbox_feedbackgeneral.addWidget(self.label_feedbackgeneral)

        self.lineedit_feedback_general = QLineEdit(self)
        hbox_feedbackgeneral.addWidget(self.lineedit_feedback_general)
        hbox_feedbackgeneral.insertSpacing(2,100)

        hbox_maj = QHBoxLayout()
        VBoxlayout_generaux.addLayout(hbox_maj)

        self.label_maj = QLabel("sensible à la case :",self)
        self.label_maj.setFixedWidth(150)
        hbox_maj.addWidget(self.label_maj)

        self.combobox_maj = QComboBox()
        self.combobox_maj.addItem("non, la case n'est pas importante")
        self.combobox_maj.addItem("oui la case doit correspondre")
        hbox_maj.addWidget(self.combobox_maj)
        hbox_maj.insertSpacing(2,450)

        
        

        VBoxLayout.addLayout(VBoxlayout_generaux)
        VBoxlayout_generaux.
        #self.groupBox_generaux.setLayout(VBoxlayout_generaux)

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

        self.groupBox.setLayout(VBoxLayout)
    

    

    def creer_question(self):
        print("creation des lignes du xml")

myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)