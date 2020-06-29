from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout, QTextEdit, QLineEdit
from PySide2.QtGui import QIcon, QFont
import sys

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
        #self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        lineedit_nom_question = QLineEdit(self)
        lineedit_nom_question.setFont(QFont('Sanserif', 10))
        lineedit_nom_question.setPlaceholderText("nom question")
        
        gridLayout.addWidget(lineedit_nom_question, 0,0)

        lineedit_intitule_question = QLineEdit(self)
        lineedit_intitule_question.setFont(QFont('Sanserif', 10))
        lineedit_intitule_question.setPlaceholderText("intitule question")
        gridLayout.addWidget(lineedit_intitule_question, 1,0)
 
 
 
        self.groupBox.setLayout(gridLayout)

myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)