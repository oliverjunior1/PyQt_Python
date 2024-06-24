import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QPushButton, QGroupBox, QLineEdit, QDateEdit
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PuQt QGroupBox')

        layout = QFormLayout(self)
        self.setLayout(layout)

        person_groupbox = QGroupBox('Persona1 Information')
        form_layout =QFormLayout()
        person_groupbox.setLayout(form_layout)

        form_layout.addRow('First Name:', QLineEdit(person_groupbox))
        form_layout.addRow('Last Name', QLineEdit(person_groupbox))
        form_layout.addRow('DOB:', QDateEdit(person_groupbox))

        contact_groupbox = QGroupBox('Contact Information')
        form_layout = QFormLayout()
        contact_groupbox.setLayout(form_layout)
        form_layout.addRow('Phone Number:', QLineEdit(contact_groupbox))
        form_layout.addRow('Email Address', QLineEdit(contact_groupbox))

        layout.addWidget(person_groupbox)
        layout.addWidget(contact_groupbox)
        layout.addWidget(QPushButton('Save'))

        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
