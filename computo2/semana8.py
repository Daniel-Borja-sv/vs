import sys
from PyQt5.Qtwidgets import (QApplication, QMainWindow, QWidget, QPushbutton, QLineEdit, QHBoxLayout)


class ventanam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica semana 8")
        boton = QPushbutton("haz click aqui")
        boton.clicked.connect(self.evento_click)
        inputxt = QLineEdit()
        inputxt.textChanged.connect(self.evento_click)
        central = QWidget()
        layout= QHBoxLayout()
        layout.addWidget(boton)
        layout.addWidget(inputxt)
        central.setLayout(layout)
        self.setCentralWidget(central)
        #self.setCentralWidget(boton)


    def evento_click(self):
        print("haz hecho click")

    def evento_txt(self):
        pass


app = QApplication(sys.argv)
ventana = ventanam()
ventana.show()
app.exec()