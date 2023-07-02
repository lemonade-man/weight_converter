from PySide2.QtWidgets import (
	QMainWindow, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton,
	QLineEdit, QComboBox
)

from converter import units
from converter import convert

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Weight Converter")

		root = QWidget()
		rootLayout = QVBoxLayout()
		root.setLayout(rootLayout)
		self.setCentralWidget(root)

		groupsCont = QWidget()
		groupsContLayout = QHBoxLayout()
		groupsCont.setLayout(groupsContLayout)

		self.convertFromWrapper = ConvertFrom()
		self.convertToWrapper = ConvertTo()

		convertBtn = QPushButton("Convert")
		convertBtn.clicked.connect(self.doConvert)

		groupsContLayout.addWidget(self.convertFromWrapper)
		groupsContLayout.addWidget(self.convertToWrapper)
		rootLayout.addWidget(groupsCont)
		rootLayout.addWidget(convertBtn)

	def getInfo(self):
		print(self.convertFromWrapper.getNum())
		print(self.convertFromWrapper.getUnit())

	def doConvert(self):
		self.convertToWrapper.setLineText(convert(
			self.convertFromWrapper.getNum(),
			self.convertFromWrapper.getUnit(),
			self.convertToWrapper.getUnit())
		)

class ConvertBox(QGroupBox):
	def __init__(self, title):
		super().__init__()

		self.setTitle(title)

		layout = QVBoxLayout()
		self.setLayout(layout)

		self.lineEdit = QLineEdit()
		self.unitCombo = QComboBox()

		for unit in units.keys():
			self.unitCombo.insertItem(0, unit)

		layout.addWidget(self.lineEdit)
		layout.addWidget(self.unitCombo)

	def getNum(self):
		return self.lineEdit.text()

	def getUnit(self):
		return self.unitCombo.currentText()

	def setLineText(self, text):
		self.lineEdit.setText(text)

class ConvertFrom(ConvertBox):
	def __init__(self):
		super().__init__("From")

class ConvertTo(ConvertBox):
	def __init__(self):
		super().__init__("To")
