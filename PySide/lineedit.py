from PySide2.QtWidgets import QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout, QTextEdit, QLineEdit, QComboBox, QMessageBox
from PySide2.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("first button")
        self.setGeometry(300,300,300,300)

        self.setButton()
        self.pushButton()

        self.lineedit = QLineEdit(self)
        self.lineedit.move(50,50)

        self.btnaffiche = QPushButton("affiche",self)
        self.btnaffiche.clicked.connect(self.affiche)

        self.combobox = QComboBox(self)
        self.combobox.move(150,0)
        self.combobox.addItems(["vrai","faux"])

    def affiche(self):
        print(self.lineedit.text())
        print(self.combobox.currentText())        

    def setButton(self):
        self.btn1 = QPushButton("Quit", self)
        self.btn1.move(50,100)
 
        self.btn1.clicked.connect(self.quiteApp)  

    def pushButton(self):
        self.aboutButtton = QPushButton("Open About Box", self)
        self.aboutButtton.move(50,200)
        self.aboutButtton.clicked.connect(self.aboutBox)  

    def quiteApp(self):
        userInfo = QMessageBox.question(self, "Confirmation", "Do You Want To Quit The Application",
                                        QMessageBox.Yes | QMessageBox.No)
 
 
 
        if userInfo == QMessageBox.Yes:
            myApp.quit()
 
        elif userInfo == QMessageBox.No:
            pass

    

    def aboutBox(self):
        QMessageBox.about(self.aboutButtton, "About Pyside2", "Pyside2 is a Cross Platform GUI Library For Python Programming Language")  
        
myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)