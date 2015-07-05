# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from httptool import *
from register import *
import global_vars
import login_config
import ui.ui_login
import sys
import re

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class login(QDialog, ui.ui_login.Ui_Dialog):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)

        self.register_dlg = None
        self.netutil = NetUtil()
        result = self.get_client_access_token()
        if result.has_key("error"):
            login_config.client_access_token = None
            # logging.debug("fail to obtain client access token")
            sys.exit()
        else:
            login_config.client_access_token = result

    def get_client_access_token(self):
        client_param = {}
        client_param['client_id'] = login_config.client_id
        client_param['client_secret'] = login_config.client_secret
        client_param['grant_type'] = 'client_credentials'
        client_param['scope'] = 'user'
        url = login_config.client_token_url
        recv = self.netutil.http_post(url, 443, client_param, 30, True)
        if (recv):
            return json.loads(recv)
        else:
            return {u"error": u"fail to get client access token"}

    def get_user_access_token(self, email, password):
        client_param = {}
        client_param['client_id'] = login_config.client_id
        client_param['client_secret'] = login_config.client_secret
        client_param['grant_type'] = 'password'
        client_param['scope'] = 'user'
        client_param['email'] = email
        client_param['password'] = password
        url = login_config.user_token_url
        recv = self.netutil.http_post(url, 443, client_param, 30, True)
        if (recv):
            return json.loads(recv)
        else:
            return {u"error": u"fail to get user access token"}

    def on_btn_login_released(self):
        email = self.ledit_email.text()
        passwd = self.ledit_password.text()
        ismatch = bool(
            re.match(r"^(([a-zA-Z0-9]*\.[a-zA-Z0-9]*)|[a-zA-Z0-9]*)@([a-z0-9A-Z]+\.)+[a-zA-Z]{2,}$", email, re.VERBOSE))
        if ismatch == False:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("不合法的邮件地址！"))
            self.ledit_email.clear()
            return

        if (len(passwd) < login_config.passwd_min_len):
            QMessageBox.information(self, self.tr("信息提示"), self.tr("密码最小长度为 " + str(login_config.passwd_min_len)))
            return

        result = self.get_user_access_token(email, passwd)
        if result.has_key("error"):
            QMessageBox.information(self, self.tr("信息提示"), self.tr("登录失败!"))
            login_config.user_access_token = None
        else:
            QMessageBox.information(self, self.tr("信息提示"), self.tr("登录成功!"))
            login_config.user_access_token = result
            global_vars.user_access_token = result
            self.close()
            import main

    def on_btn_register_released(self):
        result = self.get_client_access_token()
        if result.has_key("error"):
            login_config.client_access_token = None
            # logging.debug("fail to obtain client access token")
            sys.exit()
        else:
            login_config.client_access_token = result
        self.register_dlg = register()
        self.register_dlg.show()

    def on_ledit_email_textEdited(self, text):
        if (len(text) > login_config.email_max_len):
            text = text[:login_config.email_max_len]
            self.ledit_email.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("邮件地址超过最大长度限制!"))

    def on_ledit_password_textEdited(self, text):
        if (len(text) > login_config.passwd_max_len):
            text = text[:login_config.passwd_max_len]
            self.ledit_password.setText(text)
            QMessageBox.information(self, self.tr("信息提示"), self.tr("密码过长!"))
        for char in str(text):
            if char not in login_config.passwd_charset:
                QMessageBox.information(self, self.tr("信息提示"), self.tr("不合法的密码字符!"))
                self.ledit_password.clear()
                break

# app = QtGui.QApplication(sys.argv)
# dialog = login()
# dialog.show()
# app.exit(app.exec_())
