import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QFormLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QSpinBox')
        self.setMinimumWidth(300)

        layout = QFormLayout()
        self.setLayout(layout)

        amount = QSpinBox(minimun=1, maximum=100, value=20, prefix='$')

        amount.valueChanged.connect(self.update)

        self.result_Label = QLabel('', self)

        layout.addRow('Amount', amount)
        layout.addRow(self.result_Label)
        
        self.show()

    def update(self, value):
        self.result_Label.setText(f'Current Value {value}')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())