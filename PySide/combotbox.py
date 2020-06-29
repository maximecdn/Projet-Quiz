from PySide2.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QFontComboBox
import sys
from PySide2.QtGui import QIcon
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Pyside2 FontCombo Box")
        self.setGeometry(300,200,300,250)
 
        self.setFontBox()
 
        self.setIcon()
        self.show()
 
 
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
 
 
    def setFontBox(self):
        vbox = QVBoxLayout()
        fontcombobox = QFontComboBox()
        fontcombobox.setFontFilters(QFontComboBox.MonospacedFonts)
 
        vbox.addWidget(fontcombobox)
 
        self.setLayout(vbox)
 
 
 
myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()