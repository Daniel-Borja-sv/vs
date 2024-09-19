import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QLineEdit, QHBoxLayout,
                              QLabel, QComboBox)

from PyQt5 import uic

class ventanam(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("designl.ui",self)
        self.boton = self.findChild(QPushButton, "btnSuma")
        self.boton.clicked.connect(self.evento_click)
        self.num1 = self.findChild(QLineEdit, "num1")
        self.num2 = self.findChild(QLineEdit, "num2")
        self.lblr = self.findChild(QLabel, "label1")
        self.combo = self.findChild(Qcombobox, )


    def evento_click():




app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()