import sys
from PyQt6.QtWidgets import (
QApplication,
QWidget,
QLineEdit,
QPushButton,
QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        self.show()

    def button_clicked(self):
        print('clicked')

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())