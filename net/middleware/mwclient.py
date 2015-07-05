import sys
import socket

def sendmsg_mw(request):
    s=socket.socket()
    s.connect(('127.0.0.1',10000))
    s.send(request)
    data = 'The data received is '
    while(1):
        recdata=s.recv(500)
        data = data + recdata
        if(data.find(request) != -1):
	       data = data.replace(request,'')
	    break

    #print data
    s.close()
    return data

if __name__ == '__main__':
    request = '-X PUT -H "X-Auth-Token: " -T /home/liangjiao/mytest/test.py "http://10.131.250.153:443/v1/AUTH_glfs/test/test.py?fype=f&type=NORMAL"'
    result = sendmsg_mw(request)
    print result

