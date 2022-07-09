from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

font = QFont()
font.setPixelSize(30)

label = QLabel("Primeira label aqui.")
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
label.show()


app.exec()