###this is controller.
###first.request(string curl),to get upload/download/session/transfer,need parse to get the type
###second.upload(string curl),use compress module and encrypt module,then call uploader module
###third.download(string curl),the same as upload
###fourth.session(string curl)
###fifth.transfer(string curl)
from ctypes import *
import mwParser
import os
import json
import mwCompresser
import hashlib
import mwEncrypter
import commands
import sys

class Controller():
    request = ''

    def __init__(self,r):
	self.request = r

    ###request:to parse the request
    def req(self,rq):
	parser = mwParser.Parser(self.request)
	n = parser.parse()
	result = ''
	if(n == 'UPLOAD'):
	    #upload:compress and encrypt
	    print 'you can upload+compress+encrypt!'
            path_start = rq.find('/')
	    path_end = rq.find(' ',path_start,-1)
	    path = rq[path_start:path_end]
	    #compress	
	    compress_path = '/tmp/' + hashlib.md5(path).hexdigest() + '.zip'
	    compresser = mwCompresser.Compresser()
	    compresser.compress_file(path,compress_path)
	    #encrypt
	    encrypt_path = '/tmp/' + hashlib.md5(path).hexdigest() + '.en'
	    dll = CDLL("/usr/lib/libsecrypto.so")
	    acces_token = mwEncrypter.accessToken(dll)
	    mwEncrypter.sAES_encrypt(compress_path,encrypt_path,dll,acces_token)
	    #upload
	    rq = rq.replace(path,encrypt_path)
	    result = self.upload(rq,path)

	elif(n == 'DOWNLOAD'):
	    #download:decrypt and decompress
	    print 'you can download+decrypt+decompress!'
	    download_start = rq.find('-o')
	    path_start = rq.find('/',download_start,-1)
	    path = rq[path_start:]
	    #download	    
	    decrypt_path = '/tmp/' + hashlib.md5(path).hexdigest() + '.de'    
	    rq = rq.replace(path,decrypt_path)
	    result = self.download(rq,path)
	    #decrypt
	    decompress_path = '/tmp/' + hashlib.md5(path).hexdigest() + '.zip'
	    dll = CDLL("/usr/lib/libsecrypto.so")
	    acces_token = mwEncrypter.accessToken(dll)
	    mwEncrypter.sAES_decrypt(decrypt_path,decompress_path,dll,acces_token)
	    #decompress	    
	    compresser = mwCompresser.Compresser()
	    compresser.decompress_file(decompress_path,path)
	else:
	    #transfer
	    print 'transfer!'
	    result = self.transfer(rq)

	result = result + self.request
	return result

    ###upload:call uploader module
    def upload(self,rq,path):
	#find path
	logpath = hashlib.md5(path).hexdigest()	
	logpath = '/tmp/' + logpath + '.log'    #record log to get information
	#curl
	upload_req = 'curl ' + rq + ' 2>&1 | tee ' + logpath
	print 'upload!!!!'
	print upload_req
	#get return
	result = commands.getoutput(upload_req)
	result_start = result.find('{')
	result = result[result_start:] 
	return result

    ###download:call downloader module
    def download(self,rq,path):
	#find path
	logpath = hashlib.md5(path).hexdigest()	
	logpath = '/tmp/' + logpath + '.log'    #record log to get information
	#curl
	download_req = 'curl ' + rq + ' 2>&1 | tee ' + logpath
	os.system(download_req)
	result = path + ' download success!'
        return result

    ###transfer
    def transfer(self,rq):
	#curl
	transfer_req = 'curl ' + rq
	print transfer_req
	result = os.popen(transfer_req) 
	result = result.read()
	
	return result


