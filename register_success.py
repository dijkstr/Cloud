from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui.ui_register_success
import sys

class register_success(QDialog, ui.ui_register_success.Ui_Dialog):
	def __init__(self, parent = None):
		super(register_success, self).__init__(parent)
		self.setupUi(self)

	def on_btn_success_released(self):
		self.close()

# app = QtGui.QApplication(sys.argv)
# dialog = register_success()
# dialog.show()
# app.exit(app.exec_())
