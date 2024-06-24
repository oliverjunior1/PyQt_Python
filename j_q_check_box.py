# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
# from PyQt6.QtCore import Qt
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('PyQt QCheckBox')
#         self.setGeometry(100,100,320,210)
#
#         layout = QGridLayout()
#         self.setLayout(layout)
#
#         checkbox = QCheckBox('I agree', self)
#
#         layout.addWidget(checkbox, 0,0, Qt.AlignmentFlag.AlignCenter)
#
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100,100,320,210)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox = QCheckBox('I agree', self)

        check_button = QPushButton('Check', self)
        check_button.clicked.connect(self.check)

        uncheck_button = QPushButton('Uncheck', self)
        uncheck_button.clicked.connect(self.uncheck)

        layout.addWidget(self.checkbox, 0,0,0,2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(check_button,1,0)
        layout.addWidget(uncheck_button,1,1)

        self.show()

        def check(self):
            self.checkbox.setChecked(True)

        def check(self):
            self.checkbox.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())