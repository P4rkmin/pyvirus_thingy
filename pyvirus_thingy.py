import sys
import inneriwdget
from PyQt5.QtWidgets import *

#Main widget
class PopupApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('meep')

        layout = QVBoxLayout()

        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.show_popup)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_popup(self):
        reply = QMessageBox.information(self, 'Popup', 'Button Pressed!', QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.show_popup()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PopupApp()
    ex.show()
    sys.exit(app.exec_())
