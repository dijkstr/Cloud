#!/user/bin/python
import uuid
import rsa
import os
import sys
import commands
import base64
import random
import hashlib
import string
import ConfigParser
from Crypto.Cipher import AES

class pyUtil(object):
    def __init__(self):
        pass

    def get_config(self):
        config=ConfigParser.ConfigParser()
        with open("config.ini","rw") as cfgfile:
            config.readfp(cfgfile)
        return config

    """
    The key can be 16 characters, also can be 24 or 32 characters,
    it corresponding to AES-128, AES-196 and AES-256.
    """
    def getNetKey(self, num):
        if num <= 16:
            num = 16
        elif num > 16 and num <= 24:
            num = 24
        else:
            num = 32

        st = ''
        source = string.ascii_lowercase + string.ascii_uppercase
        while len(st) < num:
            temp = source[0 + random.randint(0,51)]
            if st.find(temp) == -1:
                st = st.join(['',temp])
        return st

    def get_md5(self,inputStr):
        return hashlib.md5(inputStr).hexdigest()

    def sumfile(fobj):
        m = md5.new()
        while True:
            d = fobj.read(8096)
            if not d:
                break
            m.update(d)
        return m.hexdigest()

    def get_file_md5(self,fname):
        if fname == '-':
            ret = sumfile(sys.stdin)
        else:
            try:
                f = file(fname, 'rb')
            except:
                return 'Failed to open file'
            ret = sumfile(f)
            f.close()
        return ret

    def get_sha1(self,inputStr):
        return hashlib.sha1(inputStr).hexdigest()

    def get_dynamical_uuid(self):
        my_id = uuid.uuid1()
        return str(my_id).encode("utf-8")

    def get_user_fixed_uuid(self,user = ''):
        my_id = uuid.uuid5(uuid.NAMESPACE_DNS, user)
        return str(my_id).encode("utf-8")

    def generate_keypair_by_openssl(self,basePath = '', taskid = ''):
        '''system call'''
        cmd = 'mkdir -p ' + basePath
        (status,result) = commands.getstatusoutput(cmd)

        '''generate keypair'''
        pubkey = basePath + '/' + 'public.pem'
        privkey = basePath + '/' + 'private.pem'

        cmd = 'openssl genrsa -out ' + privkey +' 1024'
        (status,result) = commands.getstatusoutput(cmd)

        cmd = 'openssl rsa -in ' + privkey + ' -RSAPublicKey_out -out ' + pubkey
        (status,result) = commands.getstatusoutput(cmd)

    def generate_keypair(self,basePath = '', taskid = ''):
        '''generate keypair'''
        (pubkey,privkey) = rsa.newkeys(1024)

        pubPath = basePath + '/' + 'public.pem'
        pub = pubkey.save_pkcs1()
        pubfile = open(pubPath,'w+')
        pubfile.write(pub)
        pubfile.close()

        priPath = basePath + '/' + 'private.pem'
        pri = privkey.save_pkcs1()
        prifile = open(priPath,'w+')
        prifile.write(pri)
        prifile.close()

    def get_rsa_publickey(self, KeyPath = ''):
        with open(KeyPath) as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1(p)
            return (p, pubkey)

    def get_rsa_encrypt(self,basePath = '', message = ''):
        pubKeyPath = basePath + '/' + 'public.pem'
        (keystr, pubkey) = self.get_rsa_publickey(pubKeyPath)
        crypto = rsa.encrypt(message, pubkey)
        return crypto

    def get_rsa_privatekey(self, KeyPath = ''):
        with open(KeyPath) as privatefile:
            p = privatefile.read()
            privkey = rsa.PrivateKey.load_pkcs1(p)
            return (p, privkey)

    def get_rsa_decrypt(self,KeyPath = '', crypto = ''):
        priKeyPath = KeyPath + '/' + 'private.pem'
        (keystr,privkey) = self.get_rsa_privatekey(priKeyPath)
        message = rsa.decrypt(crypto, privkey) 
        return message

    def pkcs1_unpad(text):
        if len(text) > 0 and text[0] == '\x02':
            # Find end of padding marked by nul
            pos = text.find('\x00')
            if pos > 0:
                return text[pos+1:]
        return text

    """
    The key can be 16 characters, also can be 24 or 32 characters, 
    it corresponding to AES-128, AES-196 and AES-256.
    """
    def get_aes_encrypt(self, key = '', plain = ''):
        mode = AES.MODE_CBC
        iv = b'0000000000000000'
        encryptor = AES.new(key, mode, iv)

        '''
        We use AES-128 then input strings must be a multiple of 16 in length.
        If < 16 then append space to match 16, if > 16 but not a multiple of 16 
        then append space to match a multiple of 16
        '''
        length = 16
        count = len(plain)
        if count < length:
            add = (length-count)
            #\0 backspace
            plain = plain + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            plain = plain + ('\0' * add)

        ciphertext = encryptor.encrypt(plain)
        return ciphertext

    def get_aes_decrypt(self, key = '', ciphertext = ''):
        mode = AES.MODE_CBC
        iv = b'0000000000000000'
        decryptor = AES.new(key, mode, iv)
        plain = decryptor.decrypt(ciphertext)
        return plain.rstrip('\0')

    def test_signature(self,basePath = '', message = ''):
        '''get public key'''
        pubKeyPath = basePath + '/' + 'public.pem'
        (pubkeystr, pubkey) = self.get_rsa_publickey(pubKeyPath)

        '''get private key'''
        priKeyPath = basePath + '/' + 'private.pem'
        (prikeystr, privkey) = self.get_rsa_privatekey(priKeyPath)

        signature = rsa.sign(message, privkey, 'SHA-1')
        rsa.verify(message, signature, pubkey)

    def get_base64_encode(self, text):
        return base64.encodestring(text)

    def get_base64_decode(self, text):
        return base64.decodestring(text)
