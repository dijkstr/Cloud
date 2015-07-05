# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_success.ui'
#
# Created: Mon Jun 29 20:36:16 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(250, 190)
        Dialog.setMinimumSize(QtCore.QSize(250, 190))
        Dialog.setMaximumSize(QtCore.QSize(250, 190))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 77, 77))
        self.toolButton.setMinimumSize(QtCore.QSize(77, 77))
        self.toolButton.setMaximumSize(QtCore.QSize(77, 77))
        self.toolButton.setStyleSheet(_fromUtf8("background-image: url(:/images/yes.png);\n"
"border-style: flat;"))
        self.toolButton.setText(_fromUtf8(""))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(120, 50, 109, 25))
        self.toolButton_2.setStyleSheet(_fromUtf8("background-image: url(:/images/login_success.png);\n"
"border-style: flat;"))
        self.toolButton_2.setText(_fromUtf8(""))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.btn_success = QtGui.QToolButton(Dialog)
        self.btn_success.setGeometry(QtCore.QRect(73, 120, 109, 44))
        self.btn_success.setStyleSheet(_fromUtf8("background-image: url(:/images/confirm.png);\n"
"border-style: flat;"))
        self.btn_success.setText(_fromUtf8(""))
        self.btn_success.setObjectName(_fromUtf8("btn_success"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

import resource_rc
