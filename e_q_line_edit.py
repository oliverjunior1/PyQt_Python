# import sys
# from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout)
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('PyQt QLineEdit Widget')
#         self.setGeometry(100,100,320,210)
#
#         search_box = QLineEdit(
#             self,
#             placeholderText= 'Enter a keyword to search...',
#             clearButtonEnabled = True
#         )
#
#         layout = QVBoxLayout()
#         layout.addWidget(search_box)
#         self.setLayout(layout)
#
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import(QApplication, QWidget, QLineEdit, QVBoxLayout)
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('PyQt QLineEdit Widget')
#         self.setGeometry(100,100,320,210)
#
#         password = QLineEdit(self, echoMode = QLineEdit.EchoMode.Password)
#
#         layout = QVBoxLayout()
#         layout.addWidget(password)
#         self.setLayout(layout)
#
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QVBoxLayout, QCompleter)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit Widget')
        self.setGeometry(100,100,320,210)

        common_fruits = QCompleter([
            'Apple',
            'Apricot'
            'Banana',
            'Carambola',
            'Olive',
            'Oranges',
            'Papaya',
            'Peach',
            'Pineaple',
            'Pomegranade',
            'Rambutan',
            'Ramphal',
            'Raspberries',
            'Rose apples',
            'Starfruit',
            'Strawberries',
            'Water apple',

        ])
        fruit = QLineEdit(self)
        fruit.setCompleter(common_fruits)

        layout = QVBoxLayout()
        layout.addWidget(fruit)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())