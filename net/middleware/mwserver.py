import socket
import os
import mwDaemon
import mwController 
    
daemon = mwDaemon.Daemon('/tmp/daemon.pid')
daemon.start()  
s=socket.socket()
s.bind(('127.0.0.1',10000))
s.listen(5)

print 'socket ok!'
cs,address=s.accept()
while True:
    print 'got connected from'
    print address
    #cs.send('I have got your socket')
    data = cs.recv(40000)
    print data
    controller = mwController.Controller(data)
    result = controller.req(data)
    #print result
    cs.send(result)
    # cs.close

