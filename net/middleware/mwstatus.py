import multiprocessing
import time
import sys
import commands
import os
import json

def get_status(logpath):
    p = multiprocessing.current_process()
    with open(path) as f:
        lines=f.readlines()
        curr=lines[-1]
        arr = curr.split('\r')
        lastline=arr[-1]
        lastlinejson=lastline.split()
        if (lastlinejson[0]=='{"path":'):
            curr=lines[-2]
            arr = curr.split('\r')
            lastline=arr[-1]
            lastlinejson=lastline.split()
        
        speedresult= '{"TotalPercent": "' + lastlinejson[0] + ' ","Total":"' + lastlinejson[1] + '","Received":"' + lastlinejson[3] + ' ","Average Upload":"' + lastlinejson[6] + '","Speed Upload":"' + lastlinejson[7] + '","Time Spent":"' + lastlinejson[9]+' ","Time Left":"' + lastlinejson[10] + ' ","Current Speed":"' + lastlinejson[11] +'"}'
        return speedresult
        
    f.close()
    return speedresult

   
if __name__ == '__main__':
    result = get_status('/tmp/b84b756fd8274228eec61936ec4ef9a0.log')
    print result
