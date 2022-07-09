from argparse import Action
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QMainWindow()
        base = QWidget()
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(30)
        label = QLabel("Primeira label aqui.")
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        botao = QPushButton("Botão aqui.")
        botao.setFont(font)
        layout.addWidget (label)
        layout.addWidget (botao)
        base.setLayout(layout)
        base.show()
        self.setCentralWidget(base)
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        action = QAction("Print!")
        file_menu.addAction(action)    

app = QApplication()
window = Window()
window.show()
app.exec()