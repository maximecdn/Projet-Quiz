from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Pyside2 QCheckBox")
        self.setGeometry(300,200,400,100)
 
        self.setIcon()
 
        self.createCheckBox()
 
        self.show()
 
 
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
 
    def createCheckBox(self):
        vbox = QVBoxLayout()
 
        self.label = QLabel("", self)
 
        check = QCheckBox("I Like Football", self)
        check.stateChanged.connect(self.checkBoxChange)
        check.toggle()
 
        vbox.addWidget(check)
        vbox.addWidget(self.label)
 
        self.setLayout(vbox)
 
 
 
    def checkBoxChange(self, oui):
        if oui == Qt.Checked:
            self.label.setText("Yes I Like Football")
 
        else:
            self.label.setText("No I Dont Like Football")
 
 
 
 
 
myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()