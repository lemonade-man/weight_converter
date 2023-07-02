from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
	QApplication, QWidget, QGroupBox, QPushButton, QComboBox, QVBoxLayout,
	QHBoxLayout
)

from mainWindow import MainWindow

from sys import argv

app = QApplication(argv)

window = MainWindow()
window.show()

app.exec_()
