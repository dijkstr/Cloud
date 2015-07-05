#!/usr/bin/python
import httplib,urllib
import json
import rsa
from urlparse import urlparse
from util.tools import *

class NetUtil:
    def __init__(self):
        self.errcode=''
        self.errmsg=''

    def http_get(self,url,port=80,timeout=5,is_https=False):
        domain=query_str=data=''
        o=urlparse(url)
        domain=o.netloc

        if ''!=o.path:
            query_str=o.path

        if ''!=o.query:
            query_str=query_str+'?'+o.query

        if is_https:
            conn=httplib.HTTPSConnection(domain,port)
        else:
            conn=httplib.HTTPConnection(domain,port,timeout)

        conn.request('GET',query_str)
        resp=conn.getresponse()
        status=resp.status
        if 200==status:
            data=resp.read()
        else:
            self.errcode=''
            self.errmsg='http response code(%s):%s' % (status,resp.reason)
            data=resp.read()
            
        conn.close()
        return data
    
    def http_post(self,url,port=80,ps={},timeout=5,is_https=False):
        headers={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        domain=query_str=data=''
        o=urlparse(url)
        domain=o.netloc

        if ''!=o.path:
            query_str=o.path

        if ''!=o.query:
            query_str=query_str+'?'+o.query

        if is_https:
            conn=httplib.HTTPSConnection(domain,port)
        else:
            conn=httplib.HTTPConnection(domain,port,timeout)     
        ps=urllib.urlencode(ps)
        conn.request('POST',query_str,ps,headers)
        resp=conn.getresponse()
        status=resp.status
        if 200==status:
            data=resp.read()
        else:
            self.errcode=''
            self.errmsg='http response code(%s):%s' % (status,resp.reason)
            data=resp.read()
            
        conn.close()
        return data
