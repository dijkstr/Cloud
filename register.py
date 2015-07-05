# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from httptool import *
from register_success import *
import login_config
import ui.ui_register
import sys
import re


class register(QDialog, ui.ui_register.Ui_dialog):
    def __init__(self, parent=None):
        super(register, self).__init__(parent)
        self.setupUi(self)
        self.ledit_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.ledit_pwdc.setEchoMode(QtGui.QLineEdit.Password)
        self.netutil = NetUtil()
        self.register_success_dlg = None

    def register_user(self, input_param={}):
        url = login_config.register_url
        recv = self.netutil.http_post(url, 443, input_param, 30, True)

        if (recv):
            return json.loads(recv)
        else:
            return {u"error": u"fail to register"}

    def on_btn_reg_released(self):
        input_param = {}
        input_param['email'] = self.ledit_email.text()
        input_param['name'] = self.ledit_username.text()
        input_param['username'] = self.ledit_nickname.text()
        input_param['password'] = self.ledit_pwd.text()
        input_param['password_confirmation'] = self.ledit_pwdc.text()
        input_param['access_token'] = login_config.client_access_token['access_token']
        ismatch = bool(re.match(r"^(([a-zA-Z0-9]*\.[a-zA-Z0-9]*)|[a-zA-Z0-9]*)@([a-z0-9A-Z]+\.)+[a-zA-Z]{2,}$",
                                input_param['email'], re.VERBOSE))
        if ismatch == False:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("不合法的邮件地址！"))
            self.ledit_email.clear()
            return

        if len(self.ledit_nickname.text()) == 0:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("请输入昵称！"))
            return

        if input_param['password'] != input_param['password_confirmation']:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("两次输入密码不一致!"))
            return

        if len(input_param['password']) < login_config.passwd_min_len:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("密码长度至少为 " + str(login_config.passwd_min_len)))
            return

        result = self.register_user(input_param)
        if result.has_key("error"):
            if result["error"] == "frobidden":
                QMessageBox.information(self, self.tr("信息提示"), self.tr("请重新点击注册！"))
                self.btn_cancel.click()
            error_message = result["error_message"]
            if "username" in error_message and "email" in error_message:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("用户名和邮箱已存在！"))
                self.ledit_email.clear()
                self.ledit_username.clear()
                self.ledit_pwd.clear()
                self.ledit_pwdc.clear()
            elif "username" in error_message:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("用户名已存在！"))
                self.ledit_username.clear()
                self.ledit_pwd.clear()
                self.ledit_pwdc.clear()
            elif "email" in error_message:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("邮箱已存在！"))
                self.ledit_email.clear()
                self.ledit_pwd.clear()
                self.ledit_pwdc.clear()
            else:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("注册失败！"))
                self.ledit_email.clear()
                self.ledit_username.clear()
                self.ledit_pwd.clear()
                self.ledit_pwdc.clear()
                self.ledit_nickname.clear()
        else:
            self.close()
            self.register_success_dlg = register_success()
            self.register_success_dlg.show()

    def on_ledit_email_textEdited(self, text):
        if (len(text) > login_config.email_max_len):
            text = text[:login_config.email_max_len]
            self.ledit_email.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("邮件地址过长!"))

    def on_ledit_username_textEdited(self, text):
        if (len(text) > login_config.username_max_len):
            text = text[:login_config.username_max_len]
            self.ledit_username.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("用户名过长!"))

    def on_ledit_nickname_textEdited(self, text):
        if (len(text) > login_config.nickname_max_len):
            text = text[:login_config.nickname_max_len]
            self.ledit_nickname.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("昵称过长!"))

    def on_ledit_pwd_textEdited(self, text):
        if (len(text) > login_config.passwd_max_len):
            text = text[:login_config.passwd_max_len]
            self.ledit_pwd.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("密码过长!"))
        for char in str(text):
            if char not in login_config.passwd_charset:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("不合法的密码字符!"))
                self.ledit_pwd.clear()
                break

    def on_ledit_pwdc_textEdited(self, text):
        if (len(text) > login_config.passwd_max_len):
            text = text[:login_config.passwd_max_len]
            self.ledit_pwdc.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("密码过长!"))
        for char in str(text):
            if char not in login_config.passwd_charset:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("不合法的密码字符!"))
                self.ledit_pwdc.clear()
                break

# app = QtGui.QApplication(sys.argv)
# dialog = register()
# dialog.show()
# app.exit(app.exec_())
