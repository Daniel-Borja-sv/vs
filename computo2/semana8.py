import sys
from PyQt5.QtWidgets import (QApplication, QMainwindow, QWidget, QPushbutton)


class ventanam(QMainwindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica semana 8")


app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()