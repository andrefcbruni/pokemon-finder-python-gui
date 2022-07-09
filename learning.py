from argparse import Action
from subprocess import call
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from qdarktheme import load_stylesheet

def callback():
    print("Cliquei no botão!")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QMainWindow()
        base = QWidget()
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(30)
        self.label = QLabel("Primeira label aqui.")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        botao = QPushButton("Botão aqui.")
        botao.setFont(font)
        botao.clicked.connect(self.muda_label)
        layout.addWidget (self.label)
        layout.addWidget (botao)
        base.setLayout(layout)
        base.show()
        self.setCentralWidget(base)

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        action = QAction("Print!")
        action.triggered.connect(callback)
        file_menu.addAction(action)    

    def muda_label(self):
        self.label.setText("Clicado")
app = QApplication()
app.setStyleSheet(load_stylesheet())
window = Window()
window.show()
app.exec()