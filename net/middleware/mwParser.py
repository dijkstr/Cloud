class Parser():
    request = ''
    def __init__(self,r):
	self.request = r
    
    ###parse:
    def parse(self):
	#parse the request
	##default  compress_encrypt_upload
	##default  download_decrypt_decompress
        if(self.request.find('PUT') != -1 and self.request.find('fype=f') != -1):    #create file
	    return 'UPLOAD'
        elif(self.request.find('GET') != -1 and self.request.find('fype=f') != -1):    #download file
	    return 'DOWNLOAD'
	else:
	    return 'OTHERS'	    
        ##end

	
