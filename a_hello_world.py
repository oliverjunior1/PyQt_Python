import sys
from PyQt6.QtWidgets import QApplication, QWidget

# app = QApplication([])
#
# window = QWidget(windowTitle = 'Hello World')
# window.show()
#
# app.exec()

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Hello World')
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())