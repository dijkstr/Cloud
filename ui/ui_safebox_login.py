# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'safebox_login.ui'
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

class Ui_dlg_login(object):
    def setupUi(self, dlg_login):
        dlg_login.setObjectName(_fromUtf8("dlg_login"))
        dlg_login.resize(420, 210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlg_login.sizePolicy().hasHeightForWidth())
        dlg_login.setSizePolicy(sizePolicy)
        dlg_login.setMinimumSize(QtCore.QSize(420, 210))
        dlg_login.setMaximumSize(QtCore.QSize(420, 210))
        self.gridLayoutWidget = QtGui.QWidget(dlg_login)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 361, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ledit_password = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ledit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.ledit_password.setObjectName(_fromUtf8("ledit_password"))
        self.gridLayout.addWidget(self.ledit_password, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ledit_email = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ledit_email.setObjectName(_fromUtf8("ledit_email"))
        self.gridLayout.addWidget(self.ledit_email, 0, 1, 1, 1)
        self.btn_login = QtGui.QPushButton(dlg_login)
        self.btn_login.setGeometry(QtCore.QRect(170, 160, 85, 27))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_exit = QtGui.QPushButton(dlg_login)
        self.btn_exit.setGeometry(QtCore.QRect(300, 160, 85, 27))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))

        self.retranslateUi(dlg_login)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), dlg_login.close)
        QtCore.QMetaObject.connectSlotsByName(dlg_login)
        dlg_login.setTabOrder(self.ledit_email, self.ledit_password)
        dlg_login.setTabOrder(self.ledit_password, self.btn_login)
        dlg_login.setTabOrder(self.btn_login, self.btn_exit)

    def retranslateUi(self, dlg_login):
        dlg_login.setWindowTitle(_translate("dlg_login", "用户登录", None))
        self.label_2.setText(_translate("dlg_login", "密码", None))
        self.label.setText(_translate("dlg_login", "邮箱", None))
        self.btn_login.setText(_translate("dlg_login", "登录", None))
        self.btn_exit.setText(_translate("dlg_login", "退出", None))

