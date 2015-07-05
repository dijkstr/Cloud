#!/user/bin/python
import os
import sys
import commands
import random
import ConfigParser
import json
from httptool import *

class bridgeUtil(object):
    def __init__(self):
        self.client = NetUtil()

    def get_client_access_token(self,url='', input = {}):
        recv = self.client.http_post(url,443,input,30,True)
        return json.loads(recv)

    def register_user(self,url='', input = {}):
        recv = self.client.http_post(url,443,input,30,True)
        return json.loads(recv)

    def get_user_access_token(self, url='', input = {}):
        recv = self.client.http_post(url,443,input,30,True)
        return json.loads(recv)

    def verify_user(self, url='', input = {}):
        recv = self.client.http_post(url,443,input,30,True)
        return json.loads(recv)

if __name__ == '__main__':
    client_param = {}
    client_param['client_id'] = 'seAgentClient'
    client_param['client_secret'] = 'g2sbeDfvms3sCGql'
    client_param['grant_type'] = 'client_credentials'
    client_param['scope'] = 'user'
    client = bridgeUtil()
    url = 'https://124.16.141.142/oauth/access_token'
    client_token = client.get_client_access_token(url, client_param)

    register_param = {}
    register_param['name'] = 'ronghua.he'
    register_param['username'] = 'heronghua'
    register_param['email'] = 'ronghua.he@samsung.com'
    register_param['password'] = '123456'
    register_param['password_confirmation'] = '123456'
    register_param['access_token'] = client_token['access_token']
    url = 'https://124.16.141.142/api/register'
    #result = client.register_user(url, register_param)
    #print result

    user_param = {}
    user_param['client_id'] = 'seAgentClient'
    user_param['client_secret'] = 'g2sbeDfvms3sCGql'
    user_param['email'] = 'ronghua.he@samsung.com'
    user_param['password'] = '123456'
    user_param['grant_type'] = 'password'
    user_param['scope'] = 'user'
    url = 'https://124.16.141.142/oauth/access_token'
    result = client.get_user_access_token(url, user_param)
    print result

    verify_param = {}
    verify_param['resourcename'] = 'SeAgent'
    verify_param['secret'] = '123456'
    verify_param['access_token'] = result['access_token']
    url = 'https://124.16.141.142/api/token-validation'
    result = client.verify_user(url, verify_param)
    print result
