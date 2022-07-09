from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication()
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
app.exec()