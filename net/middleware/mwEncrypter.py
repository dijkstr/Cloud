#!/usr/bin/env python
#coding=utf8

##########################################################################
# File Name: client.py
# Author: zhangcheng
# mail: zhangc1_os@sari.ac.cn
# Created Time: 2015.3.31
#########################################################################'''

from ctypes import *
import time
import json
from bridge import *
import os
import string

'''Get User Access Token'''
def accessToken(dll):
    client = bridgeUtil()
    user_param = {}
    url = 'https://124.16.141.142/oauth/access_token'
    user_param['client_id'] = 'seAgentClient'
    user_param['client_secret'] = 'g2sbeDfvms3sCGql'
    user_param['email'] = 'herh_os@sari.ac.cn'
    user_param['password'] = '123456'
    user_param['grant_type'] = 'password'
    user_param['scope'] = 'user'
    result = client.get_user_access_token(url, user_param)
    STR_LEN = 1024
    output = create_string_buffer(STR_LEN)
    input_txt = c_char_p(json.dumps(result))
    dll.convert_ukey2_cloudtoken(input_txt, output)
    print "return from lib:" + output.value
    return json.dumps(result)

#encrypt file
def sAES_encrypt(inputFile,mildFile,dll,acces_token):
    mildFile = open(mildFile,'wb')
    with open(inputFile,'rb') as f:
        while True:
            mild = create_string_buffer(1024)
            chunk = f.read(1024)
            if not chunk:
                break
            lens = len(chunk)
            if  lens < 1024:
                chunk = "%s%s" % (chunk,'\001' * (1024 - lens))
            inputs = c_char_p(chunk)
            user_token = c_char_p(acces_token)
            dll.sAES_encrypt(inputs,mild,user_token)
            mildFile.write(mild.raw)
    mildFile.close()
    
            
#decrypt file
def sAES_decrypt(mildFile,outFile,dll,acces_token):
    out = open(outFile,'wb')
    with open(mildFile,'rb') as f:
        f.seek(0,2)
        blocks = f.tell() / 1024
        f.seek(0,0)
        while True:
            outPoin = create_string_buffer(1024)
            chunk = f.read(1024)
            if not chunk:
                break
            inputs = c_char_p(chunk)
            user_token = c_char_p(acces_token)
            dll.sAES_decrypt(inputs,outPoin,user_token)

            if blocks == 1:
                out.write(outPoin.raw.rstrip('\001'))
            else:
                out.write(outPoin.raw)
            blocks = blocks -1
    out.close()
            
            
def main(dll,inputf,mild,out):
    start = time.time()
    dll.load_padlock()
    acces_token = accessToken(dll)
    sAES_encrypt(inputf,mild,dll,acces_token)
    sAES_decrypt(mild,out,dll,acces_token)
    print 'all time:',time.time() - start
    
               

if __name__ == '__main__':
    dll = CDLL("/usr/lib/libsecrypto.so")
    inputf = sys.argv[1] #source
    mild = sys.argv[2]  #encrypt
    out = sys.argv[3]   #decrypt
    if not inputf:
        sys.exit(1)
    if not mild:
        sys.exit(2)
    if not out:    
        sys.exit(3)
    main(dll,inputf,mild,out)
    
