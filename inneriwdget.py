import sys
import innerwidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

#Main widget
class PopupApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Popup Example')

        layout = QVBoxLayout()

        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.show_popup)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_popup(self):
        QMessageBox.information(self, 'Popup', 'Button Pressed!')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PopupApp()
    ex.show()
    sys.exit(app.exec_())