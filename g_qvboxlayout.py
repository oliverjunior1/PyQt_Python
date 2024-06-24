# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('PyQt QVBOxLayout')
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         titles = ['Find Next', 'Find all', 'Close']
#         buttons = [QPushButton(title) for title in titles]
#         for button in buttons:
#             layout.addWidget(button)
#
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QVBoxLayout')

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addStretch()

        titles = ['Find Next', 'Find all', 'Close']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        layout.addStretch()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

