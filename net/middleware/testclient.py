import mwclient

request = '-X GET -H "X-Auth-Token: " http://192.168.68.108:443/v1/AUTH_glfs'

# request = '-i -X HEAD -H "X-Auth-Token: " "http://192.168.68.108:443/v1/AUTH_glfs/recycle/meta"'

request = '-i -X DELETE -H "X-Auth-Token: " http://192.168.68.108:443/v1/AUTH_glfs/recycle'
# register  segments   user   versions

result = mwclient.sendmsg_mw(request)

print ('client recv msg: ' + result)
