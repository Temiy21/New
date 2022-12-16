import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle("Test")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
