import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login Form')

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Password: '), 1, 0)
        layout.addWidget(QLineEdit(echoMode=QLineEdit.EchoMode.Password), 1, 1)

        layout.addWidget(QPushButton('Log in'), 2, 0,
                         alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QPushButton('Clocse'),2, 1,
                         alignment=Qt.AlignmentFlag.AlignRight)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())