import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class PopupExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Got some bad news..')

        # Create a button to trigger the popup
        self.popup_button = QPushButton('What?', self)
        self.popup_button.clicked.connect(self.show_popup)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.popup_button)
        self.setLayout(layout)
        self.resize(350, 50)

    def show_popup(self):
        # Create a QMessageBox
        popup = QMessageBox()
        popup.setWindowTitle(':(')
        popup.setText("You're a dingus :(")
        popup.setIcon(QMessageBox.Information)
        popup.setStandardButtons(QMessageBox.Ok)

        # Executing the popup
        popup.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    popup_example = PopupExample()
    popup_example.show()
    sys.exit(app.exec_())
