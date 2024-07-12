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

        # Set the main window size, I have used a different method in the show_popup def
        self.resize(400, 300)  

        layout = QVBoxLayout()

        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.show_popup)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_popup(self):

        # Create a custom message box
        msg = QMessageBox(self)
        msg.setWindowTitle('Popup')
        msg.setText('all your base are belong to us')
        msg.setStandardButtons(QMessageBox.Ok)

        # Set the size of the popup window
        msg.setStyleSheet("QLabel{min-width: 350px; min-height: 50px;}")

        # Show the message box and wait for user interaction
        reply = msg.exec_()
        if reply == QMessageBox.Ok:
            self.show_popup()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PopupApp()
    ex.show()
    sys.exit(app.exec_())
