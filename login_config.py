# -*- coding: utf-8 -*-

client_id = 'hnuclient1'
client_secret = '34ulL811ANtS70Te'

client_token_url = 'https://124.16.141.142/oauth/access_token'
register_url = 'https://124.16.141.142/api/register'
user_token_url = 'https://124.16.141.142/oauth/access_token'

client_access_token = None
user_access_token = None

#email address rules
email_max_len = 32

#password rules
passwd_min_len = 6
passwd_max_len = 32
passwd_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

#username and nickname rules
username_max_len = 32
nickname_max_len = 32