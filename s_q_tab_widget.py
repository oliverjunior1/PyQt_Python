import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QTabWidget, QLineEdit, QDateEdit, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        tab = QTabWidget(self)

        personal_page = QWidget(self)
        layout = QFormLayout()
        personal_page.setLayout(layout)
        layout.addRow('First Name:', QLineEdit(self))
        layout.addRow('Last Name:', QLineEdit(self))
        layout.addRow('DOB:', QDateEdit(self))

        contact_page = QWidget(self)
        layout = QFormLayout()
        contact_page.setLayout(layout)
        layout.addRow('Phone Number:', QLineEdit(self))
        layout.addRow('Email Address:', QLineEdit(self))

        tab.addTab(personal_page, 'Personal Info')
        tab.addTab(contact_page, 'Contact Info')

        main_layout.addWidget(tab, 0, 0, 2, 1)
        main_layout.addWidget(QPushButton('Save'), 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0, alignment=Qt.AlignmentFlag.AlignRight)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

