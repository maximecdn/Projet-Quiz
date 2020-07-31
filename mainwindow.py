# -*- coding: utf-8 -*-

'''Fenêtre principale de l'application
   Permet de creer une question ou de modifier une question existante'''


from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit, QComboBox, QLabel, QCheckBox, QScrollBar, QScrollArea
from PySide2.QtGui import QIcon, QFont
from PySide2 import QtCore
import os, sys
import os.path
import time

from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

#on importe toute les fenêtres qui correspondent aux différentes sortes de questions
from window_numerique import Window_numerique
from window_reponsecourte import Window_reponsecourte
from window_calculeesimple import Window_calculeesimple
from window_vraifaux import Window_vraifaux
from window_choixmultiple import Window_choixmultiple


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("fenêtre principale")
        self.setGeometry(500,500,500,500)
        

        self.createVBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox_creerquestion)
        vbox.addWidget(self.groupBox_modifierquestion)
        self.setLayout(vbox)


    def createVBoxLayout(self):
        self.groupBox_creerquestion = QGroupBox("Créer quetion")
        VBoxLayout_creerquestion = QVBoxLayout()

        self.button_vraifaux = QPushButton("vrai faux")
        self.button_vraifaux.clicked.connect(self.vraifaux)
        VBoxLayout_creerquestion.addWidget(self.button_vraifaux)

        self.button_reponsecourte = QPushButton("réponse courte")
        self.button_reponsecourte.clicked.connect(self.reponsecourte)
        VBoxLayout_creerquestion.addWidget(self.button_reponsecourte)

        self.button_choixmultiple = QPushButton("choix multiple")
        self.button_choixmultiple.clicked.connect(self.choixmultiple)
        VBoxLayout_creerquestion.addWidget(self.button_choixmultiple)

        self.button_numerique = QPushButton("numérique")
        self.button_numerique.clicked.connect(self.numerique)
        VBoxLayout_creerquestion.addWidget(self.button_numerique)

        self.button_calculeesimple = QPushButton("calculée simple")
        self.button_calculeesimple.clicked.connect(self.calculeesimple)
        VBoxLayout_creerquestion.addWidget(self.button_calculeesimple)

        self.groupBox_creerquestion.setLayout(VBoxLayout_creerquestion)

        self.groupBox_modifierquestion = QGroupBox("modifier question")
        VBoxLayout_modifier_question = QVBoxLayout()

        self.lineedit_adresse = QLineEdit()
        self.lineedit_adresse.setText(os.getcwd())
        VBoxLayout_modifier_question.addWidget(self.lineedit_adresse)


        self.button = QPushButton("Modifier")
        self.button.clicked.connect(self.modifier)
        VBoxLayout_modifier_question.addWidget(self.button)

        self.groupBox_modifierquestion.setLayout(VBoxLayout_modifier_question)

    def vraifaux(self):
        window_vraifaux_creation.show()

    def reponsecourte(self):
        window_reponsecourte_creation.show()

    def choixmultiple(self):
        window_choixmultiple_creation.show()

    def numerique(self):
        window_numerique_creation.show()

    def calculeesimple(self):
        window_calculeesimple_creation.show()

    def modifier(self):

        #la fonction va lire une fichier xml et ouvre une fenetre de création de question en pré remplissant les champs de cette fenêtre en fonction du fichier xml

        type_question = ""

        nom_fichier = os.path.basename(self.lineedit_adresse.text())
        adresse_fichier = os.path.dirname(self.lineedit_adresse.text())

        nom_question = ""
        intitule_question = ""
        note_defaut = ""
        penalite = ""
        feedback_general = ""

        tree = ET.parse(self.lineedit_adresse.text())
        root = tree.getroot()
        
        for question in root.iter('question'):

            if question.attrib["type"] != "category":
                type_question = question.attrib["type"]

        for note in root.iter('defaultgrade'):
            note_defaut = note.text

        for penalty in root.iter('penalty'):
            penalite = penalty.text

        for name in root.iter('name'):
            for nom in name.iter('text'):
                nom_question = nom.text

        for question in root.iter('questiontext'):
            for intitule in question.iter('text'):
                intitule_question = intitule.text[3:len(intitule.text)-4]

        for general in root.iter('generalfeedback'):
            for feedback in general.iter('text'):
                feedback_general = feedback.text

        
        if type_question == "truefalse" :

            window_vraifaux_modification.lineedit_nom_fichier.setText(nom_fichier[0:len(nom_fichier)-4])
            window_vraifaux_modification.lineedit_adresse.setText(adresse_fichier)

            window_vraifaux_modification.lineedit_nom_question.setText(nom_question)
            window_vraifaux_modification.textedit_intitule_question.setText(intitule_question)
            window_vraifaux_modification.lineedit_note_par_defaut.setText(note_defaut)
            window_vraifaux_modification.combobox_penalite.setCurrentText(str(int(float(penalite)*100)))
            window_vraifaux_modification.lineedit_feedback_general.setText(feedback_general)

            bonne_reponse = 'Vrai'
            for answer in root.iter('answer'):
                note_faux = answer.attrib["fraction"]
            if note_faux == '100':
                bonne_reponse = 'Faux'
            window_vraifaux_modification.combobox_vraifaux.setCurrentText(bonne_reponse)

            liste_feedback = []
            for answer in root.iter('answer'):
                for feedback in answer.iter('text'):
                    liste_feedback.append(feedback.text)
            window_vraifaux_modification.lineedit_feedback_vrai.setText(liste_feedback[1])
            window_vraifaux_modification.lineedit_feedback_faux.setText(liste_feedback[3])

            window_vraifaux_modification.show()

        if type_question == "shortanswer" :
            
            majuscule = ''
            for usecase in root.iter('usecase'):
                majuscule = usecase.text

            window_reponsecourte_modification.lineedit_adresse.setText(adresse_fichier)
            window_reponsecourte_modification.lineedit_nom_fichier.setText(nom_fichier[0:len(nom_fichier)-4])

            window_reponsecourte_modification.lineedit_nom_question.setText(nom_question)
            window_reponsecourte_modification.textedit_intitule_question.setText(intitule_question)
            window_reponsecourte_modification.lineedit_note_par_defaut.setText(note_defaut)
            window_reponsecourte_modification.combobox_penalite.setCurrentText(str(int(float(penalite)*100)))
            window_reponsecourte_modification.lineedit_feedback_general.setText(feedback_general)
            window_reponsecourte_modification.show()

            if majuscule != '0':
                window_reponsecourte_modification.combobox_maj.setCurrentIndex(1)
            
            liste_reponse = []
            liste_note = []
            liste_feedback = []
            for answer in root.iter('answer'):
                liste_note.append(answer.attrib["fraction"])
                for question in answer.iter('text'):
                    liste_reponse.append(question.text)
                for feedback in answer.iter('feedback'):
                    for feed in feedback.iter('text'):
                        liste_feedback.append(feed.text)
            for k in range (3):
                liste_reponse.append("")
                liste_note.append("")
                liste_feedback.append("")

            

            window_reponsecourte_modification.LineEditReponse1.setText(liste_reponse[0])
            window_reponsecourte_modification.combobox_reponse1.setCurrentText(liste_note[0])
            window_reponsecourte_modification.lineedit_feedback_reponse1.setText(liste_feedback[0])

            window_reponsecourte_modification.LineEditReponse2.setText(liste_reponse[2])
            window_reponsecourte_modification.combobox_reponse2.setCurrentText(liste_note[1])
            window_reponsecourte_modification.lineedit_feedback_reponse2.setText(liste_feedback[1])


            
        if type_question == "multichoice" :

            window_choixmultiple_modification.lineedit_nom_fichier.setText(nom_fichier[0:len(nom_fichier)-4])
            window_choixmultiple_modification.lineedit_adresse.setText(adresse_fichier)

            window_choixmultiple_modification.lineedit_nom_question.setText(nom_question)
            window_choixmultiple_modification.textedit_intitule_question.setText(intitule_question)
            window_choixmultiple_modification.lineedit_note_par_defaut.setText(note_defaut)
            window_choixmultiple_modification.combobox_penalite.setCurrentText(str(int(float(penalite)*100)))
            window_choixmultiple_modification.lineedit_feedback_general.setText(feedback_general)

            nb_reponse = ''
            for single in root.iter('single'):
                nb_reponse = single.text
            if nb_reponse == 'false' :
                window_choixmultiple_modification.combobox_nbreponse.setCurrentIndex(1)
            else:
                window_choixmultiple_modification.combobox_nbreponse.setCurrentIndex(0)

            melange_reponse = ''
            for shuffleanswers in root.iter('shuffleanswers'):
                melange_reponse = shuffleanswers.text
            if melange_reponse != 'false':
                window_choixmultiple_modification.check_melange.setChecked(True)

            numerotation = ''
            for answernumbering in root.iter('answernumbering'):
                numerotation = answernumbering.text
            if numerotation == '123':
                window_choixmultiple_modification.combobox_numerotation.setCurrentIndex(1)
            elif numerotation == 'abc':
                window_choixmultiple_modification.combobox_numerotation.setCurrentIndex(0)
            else:
                window_choixmultiple_modification.combobox_numerotation.setCurrentIndex(2)

            liste_reponse = []
            liste_note = []
            liste_feedback = []
            for answer in root.iter('answer'):
                liste_note.append(answer.attrib["fraction"])
                for question in answer.iter('text'):
                    liste_reponse.append(question.text[3:len(question.text)-4])
                for feedback in answer.iter('feedback'):
                    for feed in feedback.iter('text'):
                        liste_feedback.append(feed.text)
            for k in range(3):
                liste_reponse.append("")
                liste_note.append("")
                liste_feedback.append("")

            liste_feedback_principaux = []
            for feedback in root.iter('text'):
                liste_feedback_principaux.append(feedback.text)
            window_choixmultiple_modification.lineedit_feedback_corecte.setText(liste_feedback_principaux[4])
            window_choixmultiple_modification.lineedit_feedback_partiellement_corecte.setText(liste_feedback_principaux[5])
            window_choixmultiple_modification.lineedit_feedback_incorecte.setText(liste_feedback_principaux[6])
            

            window_choixmultiple_modification.LineEditReponse1.setText(liste_reponse[0])
            window_choixmultiple_modification.combobox_reponse1.setCurrentText(liste_note[0])
            window_choixmultiple_modification.lineedit_feedback_reponse1.setText(liste_feedback[0])

            window_choixmultiple_modification.LineEditReponse2.setText(liste_reponse[2])
            window_choixmultiple_modification.combobox_reponse2.setCurrentText(liste_note[1])
            window_choixmultiple_modification.lineedit_feedback_reponse2.setText(liste_feedback[1])

            window_choixmultiple_modification.LineEditReponse3.setText(liste_reponse[4])
            window_choixmultiple_modification.combobox_reponse3.setCurrentText(liste_note[2])
            window_choixmultiple_modification.lineedit_feedback_reponse3.setText(liste_feedback[2])

            window_choixmultiple_modification.LineEditReponse4.setText(liste_reponse[6])
            window_choixmultiple_modification.combobox_reponse4.setCurrentText(liste_note[3])
            window_choixmultiple_modification.lineedit_feedback_reponse4.setText(liste_feedback[3])
        
            window_choixmultiple_modification.show()




        if type_question == "numerical" :

            window_numerique_modification.lineedit_nom_fichier.setText(nom_fichier[0:len(nom_fichier)-4])
            window_numerique_modification.lineedit_adresse.setText(adresse_fichier)

            window_numerique_modification.lineedit_nom_question.setText(nom_question)
            window_numerique_modification.textedit_intitule_question.setText(intitule_question)
            window_numerique_modification.lineedit_note_par_defaut.setText(note_defaut)
            window_numerique_modification.combobox_penalite.setCurrentText(str(int(float(penalite)*100)))
            window_numerique_modification.lineedit_feedback_general.setText(feedback_general)

            traitement_unite = ''
            for unit in root.iter('unitgradingtype'):
                traitement_unite = unit.text

            saisie_unite = ''
            for showunits in root.iter('showunits'):
                saisie_unite = showunits.text

            position_unite = '' 
            for unitsleft in root.iter('unitsleft'):
                position_unite = unitsleft.text

            liste_unite_nom = []
            for unit_name in root.iter('unit_name'):
                liste_unite_nom.append(unit_name.text)
            for k in range(3):
                liste_unite_nom.append('')

            liste_unite_coef = []
            for multiplier in root.iter('multiplier'):
                liste_unite_coef.append(multiplier.text)
            for k in range(3):
                liste_unite_coef.append('')

            
            if traitement_unite == '0' and saisie_unite == '3' :
                window_numerique_modification.combobox_traitementunite.setCurrentIndex(0)

            if traitement_unite == '0' and saisie_unite != '3' :
                window_numerique_modification.combobox_traitementunite.setCurrentIndex(1)
                window_numerique_modification.combobox_position_unite.setCurrentIndex(int(position_unite))

                window_numerique_modification.lineedit_unite1.setText(liste_unite_nom[0])
                window_numerique_modification.lineedit_coef1.setText(liste_unite_coef[0])

                window_numerique_modification.lineedit_unite2.setText(liste_unite_nom[1])
                window_numerique_modification.lineedit_coef2.setText(liste_unite_coef[1])

            if traitement_unite != '0' :
                window_numerique_modification.combobox_traitementunite.setCurrentIndex(2)
                window_numerique_modification.combobox_position_unite.setCurrentIndex(int(position_unite))
                window_numerique_modification.combobox_selection_unite.setCurrentIndex(int(saisie_unite))

                window_numerique_modification.lineedit_unite1.setText(liste_unite_nom[0])
                window_numerique_modification.lineedit_coef1.setText(liste_unite_coef[0])

                window_numerique_modification.lineedit_unite2.setText(liste_unite_nom[1])
                window_numerique_modification.lineedit_coef2.setText(liste_unite_coef[1])

            liste_reponse = []
            liste_note = []
            liste_feedback = []
            liste_erreur = []
            for answer in root.iter('answer'):
                liste_note.append(answer.attrib["fraction"])
                for question in answer.iter('text'):
                    liste_reponse.append(question.text)
                for feedback in answer.iter('feedback'):
                    for feed in feedback.iter('text'):
                        liste_feedback.append(feed.text)
                for tolerance in answer.iter('tolerance'):
                    liste_erreur.append(tolerance.text)

            for k in range (3):
                liste_reponse.append("")
                liste_note.append("")
                liste_feedback.append("")
                liste_feedback

            window_numerique_modification.LineEditReponse1.setText(liste_reponse[0])
            window_numerique_modification.lineedit_erreur_reponse1.setText(liste_erreur[0])
            window_numerique_modification.combobox_reponse1.setCurrentText(liste_note[0])
            window_numerique_modification.lineedit_feedback_reponse1.setText(liste_feedback[0])

            window_numerique_modification.LineEditReponse2.setText(liste_reponse[2])
            window_numerique_modification.lineedit_erreur_reponse2.setText(liste_erreur[1])
            window_numerique_modification.combobox_reponse2.setCurrentText(liste_note[1])
            window_numerique_modification.lineedit_feedback_reponse2.setText(liste_feedback[1])

                

            window_numerique_modification.show()
            

        if type_question == 'calculatedsimple':
            
            window_calculeesimple_modification.lineedit_nom_fichier.setText(nom_fichier[0:len(nom_fichier)-4])
            window_calculeesimple_modification.lineedit_adresse.setText(adresse_fichier)

            window_calculeesimple_modification.lineedit_nom_question.setText(nom_question)
            window_calculeesimple_modification.textedit_intitule_question.setText(intitule_question)
            window_calculeesimple_modification.lineedit_note_par_defaut.setText(note_defaut)
            window_calculeesimple_modification.combobox_penalite.setCurrentText(str(int(float(penalite)*100)))
            window_calculeesimple_modification.lineedit_feedback_general.setText(feedback_general)

            traitement_unite = ''
            for unit in root.iter('unitgradingtype'):
                traitement_unite = unit.text

            saisie_unite = ''
            for showunits in root.iter('showunits'):
                saisie_unite = showunits.text

            position_unite = '' 
            for unitsleft in root.iter('unitsleft'):
                position_unite = unitsleft.text

            liste_unite_nom = []
            for unit_name in root.iter('unit_name'):
                liste_unite_nom.append(unit_name.text)
            for k in range(3):
                liste_unite_nom.append('')

            liste_unite_coef = []
            for multiplier in root.iter('multiplier'):
                liste_unite_coef.append(multiplier.text)
            for k in range(3):
                liste_unite_coef.append('')
            
            if traitement_unite == '0' and saisie_unite == '3' :
                window_calculeesimple_modification.combobox_traitementunite.setCurrentIndex(0)

            if traitement_unite == '0' and saisie_unite != '3' :
                window_calculeesimple_modification.combobox_traitementunite.setCurrentIndex(1)
                window_calculeesimple_modification.combobox_position_unite.setCurrentIndex(int(position_unite))

                window_calculeesimple_modification.lineedit_unite1.setText(liste_unite_nom[0])
                window_calculeesimple_modification.lineedit_coef1.setText(liste_unite_coef[0])

                window_calculeesimple_modification.lineedit_unite2.setText(liste_unite_nom[1])
                window_calculeesimple_modification.lineedit_coef2.setText(liste_unite_coef[1])

            if traitement_unite != '0' :
                
                window_calculeesimple_modification.combobox_traitementunite.setCurrentIndex(2)
                window_calculeesimple_modification.combobox_position_unite.setCurrentIndex(int(position_unite))
                window_calculeesimple_modification.combobox_selection_unite.setCurrentIndex(int(saisie_unite))

                window_calculeesimple_modification.lineedit_unite1.setText(liste_unite_nom[0])
                window_calculeesimple_modification.lineedit_coef1.setText(liste_unite_coef[0])

                window_calculeesimple_modification.lineedit_unite2.setText(liste_unite_nom[1])
                window_calculeesimple_modification.lineedit_coef2.setText(liste_unite_coef[1])

            liste_reponse = []
            liste_note = []
            liste_feedback = []
            liste_erreur = []
            for answer in root.iter('answer'):
                liste_note.append(answer.attrib["fraction"])
                for question in answer.iter('text'):
                    liste_reponse.append(question.text)
                for feedback in answer.iter('feedback'):
                    for feed in feedback.iter('text'):
                        liste_feedback.append(feed.text)
                for tolerance in answer.iter('tolerance'):
                    liste_erreur.append(tolerance.text)
            
            

            for k in range (3):
                liste_reponse.append("")
                liste_note.append("")
                liste_feedback.append("")
                liste_feedback

            window_calculeesimple_modification.lineedit_reponse.setText(liste_reponse[0])
            window_calculeesimple_modification.lineedit_erreur_reponse1.setText(liste_erreur[0])
            window_calculeesimple_modification.combobox_reponse1.setCurrentText(liste_note[0])
            window_calculeesimple_modification.lineedit_feedbackreponse.setText(liste_feedback[0])

                

            window_calculeesimple_modification.show()



    
        
        
'''Quand le programme s'execute, on crée la fenetre principale(mainwindow) et on l'affiche.

   On crée également des fenetres de création de questions(window_vraifaux, window_reponsecourte, ...). 
   Ces dernières ne sont pas visibles au lancement de l'application. On les rend visibles lorsque l'on appuie sur les différents boutons de la fenetre principale
'''

myApp = QApplication(sys.argv)

window = Window()
window.show()

#fenêtres qui serviront à la création de questions
window_numerique_creation = Window_numerique()
window_vraifaux_creation = Window_vraifaux()
window_reponsecourte_creation = Window_reponsecourte()
window_calculeesimple_creation = Window_calculeesimple()
window_choixmultiple_creation = Window_choixmultiple()

#fenêtres qui serviront à la modification de questions
window_numerique_modification = Window_numerique()
window_vraifaux_modification = Window_vraifaux()
window_reponsecourte_modification = Window_reponsecourte()
window_calculeesimple_modification = Window_calculeesimple()
window_choixmultiple_modification = Window_choixmultiple()


myApp.exec_()
sys.exit()