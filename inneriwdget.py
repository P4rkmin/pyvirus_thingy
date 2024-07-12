import sys
import innerwidget
from PyQt5.QtWidgets import *

class popup(QWidget):
    def __init__(self, title, image, text):
        self.title = title
        self.image = image
        self.text = text

class InnerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle()

        layout = QVBoxLayout()

        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.show_popup)

        layout.addWidget(self.button)

        self.setLayout(layout)