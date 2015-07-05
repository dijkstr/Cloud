import zipfile 
import os

class Compresser():
 
    def compress_file(self,filename, tofilename):
        os.chdir(os.path.dirname(filename))
        (filenames,filename)=os.path.split(filename)
        f = zipfile.ZipFile(tofilename,'w',zipfile.ZIP_DEFLATED) 
        f.write(filename) 
        f.close()
	print 'compress_file'

    def decompress_file(self,filename,tofilename):
        zfile = zipfile.ZipFile(filename,'r')
        for filename in zfile.namelist():
            data = zfile.read(filename)
	    #print filename
            file = open(tofilename, 'w+b')
            file.write(data)
            file.close()
	print 'decompress_file'

if __name__ == '__main__':
    compresser = Compresser()
    compresser.compress_file('/home/liangjiao/mytest/version1.txt','/home/liangjiao/mytest/version111.zip')
    compresser.decompress_file('/home/liangjiao/mytest/version111.zip','/home/liangjiao/mytest/version00.txt')
    print 'ok'
