#!/usr/bin/python3
# -*- coding : utf-8 -*-

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
import sys
from PySide2.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("first button")
        self.setGeometry(300,300,300,300)

        self.setButton()
        self.pushButton()

        self.center()

    def setButton(self):
        btn1 = QPushButton("Quit", self)
        btn1.move(50,100)
 
        btn1.clicked.connect(self.quiteApp)  

    def pushButton(self):
        self.aboutButtton = QPushButton("Open About Box", self)
        self.aboutButtton.move(50,100)
        self.aboutButtton.clicked.connect(self.aboutBox)  

    def quiteApp(self):
        userInfo = QMessageBox.question(self, "Confirmation", "Do You Want To Quit The Application",
                                        QMessageBox.Yes | QMessageBox.No)
 
 
 
        if userInfo == QMessageBox.Yes:
            myApp.quit()
 
        elif userInfo == QMessageBox.No:
            pass

    
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def aboutBox(self):
        QMessageBox.about(self.aboutButtton, "About Pyside2", "Pyside2 is a Cross Platform GUI Library For Python Programming Language")  
        
myApp = QApplication(sys.argv)
window = Window()

window.show()

myApp.exec_()
sys.exit(0)