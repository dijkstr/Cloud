# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.setWindowModality(QtCore.Qt.NonModal)
        dialog.resize(500, 295)
        dialog.setMinimumSize(QtCore.QSize(500, 295))
        dialog.setMaximumSize(QtCore.QSize(500, 295))
        dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame = QtGui.QFrame(dialog)
        self.frame.setGeometry(QtCore.QRect(0, -1, 501, 30))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(32,117,218);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 6, 61, 16))
        self.label.setStyleSheet(_fromUtf8("font: 11pt \"Droid Sans Fallback\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.headportrait_show = QtGui.QLabel(dialog)
        self.headportrait_show.setGeometry(QtCore.QRect(362, 40, 127, 165))
        self.headportrait_show.setMinimumSize(QtCore.QSize(75, 115))
        self.headportrait_show.setStyleSheet(_fromUtf8("background-image: url(:/images/uploadhead_icon.png);"))
        self.headportrait_show.setText(_fromUtf8(""))
        self.headportrait_show.setObjectName(_fromUtf8("headportrait_show"))
        self.btn_reg = QtGui.QToolButton(dialog)
        self.btn_reg.setGeometry(QtCore.QRect(180, 240, 111, 46))
        self.btn_reg.setStyleSheet(_fromUtf8("background-image: url(:/images/register.png);\n"
"border-style: flat;"))
        self.btn_reg.setText(_fromUtf8(""))
        self.btn_reg.setObjectName(_fromUtf8("btn_reg"))
        self.upload_headportrait = QtGui.QToolButton(dialog)
        self.upload_headportrait.setGeometry(QtCore.QRect(385, 210, 85, 28))
        self.upload_headportrait.setStyleSheet(_fromUtf8("background-image: url(:/images/uploadhead.png);\n"
"border-style: flat;"))
        self.upload_headportrait.setText(_fromUtf8(""))
        self.upload_headportrait.setObjectName(_fromUtf8("upload_headportrait"))
        self.layoutWidget = QtGui.QWidget(dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 38, 321, 201))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 10pt \"Droid Sans Fallback\";\n"
"color: rgb(112, 112, 112);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.ledit_email = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_email.setStyleSheet(_fromUtf8("border-style:  flat;"))
        self.ledit_email.setObjectName(_fromUtf8("ledit_email"))
        self.gridLayout.addWidget(self.ledit_email, 0, 1, 1, 1)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);\n"
"font: 10pt \"Droid Sans Fallback\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.ledit_username = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_username.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.ledit_username.setObjectName(_fromUtf8("ledit_username"))
        self.gridLayout.addWidget(self.ledit_username, 2, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);\n"
"font: 10pt \"Droid Sans Fallback\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.ledit_pwd = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_pwd.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.ledit_pwd.setObjectName(_fromUtf8("ledit_pwd"))
        self.gridLayout.addWidget(self.ledit_pwd, 4, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);\n"
"font: 10pt \"Droid Sans Fallback\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.ledit_pwdc = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_pwdc.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.ledit_pwdc.setObjectName(_fromUtf8("ledit_pwdc"))
        self.gridLayout.addWidget(self.ledit_pwdc, 6, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet(_fromUtf8("font: 10pt \"Droid Sans Fallback\";\n"
"color: rgb(112, 112, 112);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.ledit_nickname = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_nickname.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.ledit_nickname.setObjectName(_fromUtf8("ledit_nickname"))
        self.gridLayout.addWidget(self.ledit_nickname, 8, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 9, 0, 1, 2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Register ", None))
        self.label.setText(_translate("dialog", "用户注册", None))
        self.label_3.setText(_translate("dialog", "邮        箱：", None))
        self.label_4.setText(_translate("dialog", "用  户  名：", None))
        self.label_5.setText(_translate("dialog", "密        码：", None))
        self.label_6.setText(_translate("dialog", "确认密码：", None))
        self.label_7.setText(_translate("dialog", "昵        称：", None))

import resource_rc
