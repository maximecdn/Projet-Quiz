from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PySide2.QtGui import QIcon, QFont
 
a=0
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Layout Managment")
        self.setGeometry(300,200,500,400)
 
        self.setIcon()
 
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
 
 
 
 
        self.show()
 
 
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
 
 
    def createLayout(self):
        self.groupBox = QGroupBox("Please Choose One Language")
        self.groupBox.setFont(QFont("Sanserif", 13))
        
        hbox =QVBoxLayout()
 
        button = QPushButton("CSS", self)
        button.setIcon(QIcon("css.png"))
        button.setMinimumHeight(40)
        hbox.addWidget(button)
 
        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("cpp.png"))
        button1.setMinimumHeight(40)
        hbox.addWidget(button1)
 
        button2 = QPushButton("Javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        button2.setMinimumHeight(40)
        hbox.addWidget(button2)
 
        self.groupBox.setLayout(hbox)
 
 
 
 
#print(a) 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()