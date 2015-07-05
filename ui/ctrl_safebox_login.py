from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import safebox_login
import sys

class ctrl_safebox_login(QDialog, safebox_login.Ui_dlg_login):
	def __init__(self, parent = None):
		super(ctrl_safebox_login, self).__init__(parent)
		self.setupUi(self)

