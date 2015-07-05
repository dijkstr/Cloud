# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Mon Jun 29 20:36:15 2015
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
        Dialog.resize(453, 330)
        Dialog.setMinimumSize(QtCore.QSize(453, 330))
        Dialog.setMaximumSize(QtCore.QSize(453, 330))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(70, 20, 101, 91))
        self.toolButton.setStyleSheet(_fromUtf8("background-image: url(:/images/yunlogo.png);\n"
"border-style: flat;"))
        self.toolButton.setText(_fromUtf8(""))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(204, 40, 191, 61))
        self.toolButton_2.setStyleSheet(_fromUtf8("background-image: url(:/images/yuncunchu.png);\n"
"border-style: flat;"))
        self.toolButton_2.setText(_fromUtf8(""))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.ledit_email = QtGui.QLineEdit(Dialog)
        self.ledit_email.setGeometry(QtCore.QRect(80, 130, 308, 51))
        self.ledit_email.setStyleSheet(_fromUtf8("background-image: url(:/images/enter.png);\n"
"color: rgb(132, 132, 132);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"border-style: flat;"))
        self.ledit_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_email.setObjectName(_fromUtf8("ledit_email"))
        self.ledit_password = QtGui.QLineEdit(Dialog)
        self.ledit_password.setGeometry(QtCore.QRect(80, 190, 308, 51))
        self.ledit_password.setStyleSheet(_fromUtf8("background-image: url(:/images/enter.png);\n"
"border-style: flat;\n"
"color: rgb(132, 132, 132);\n"
"font: 12pt \"Droid Sans Fallback\";"))
        self.ledit_password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_password.setObjectName(_fromUtf8("ledit_password"))
        self.btn_register = QtGui.QToolButton(Dialog)
        self.btn_register.setGeometry(QtCore.QRect(140, 260, 111, 45))
        self.btn_register.setStyleSheet(_fromUtf8("background-image: url(:/images/register.png);\n"
"border-style: flat;"))
        self.btn_register.setText(_fromUtf8(""))
        self.btn_register.setObjectName(_fromUtf8("btn_register"))
        self.btn_login = QtGui.QToolButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(270, 260, 111, 45))
        self.btn_login.setStyleSheet(_fromUtf8("background-image: url(:/images/login.png);\n"
"border-style: flat;"))
        self.btn_login.setText(_fromUtf8(""))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.ledit_email.setText(_translate("Dialog", "      请输入帐号", None))
        self.ledit_password.setText(_translate("Dialog", "      请输入密码", None))

import resource_rc
